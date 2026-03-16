from __future__ import annotations

from collections import Counter
from itertools import combinations
from typing import Any

import pandas as pd


def _frequent_itemsets(
    transactions: list[list[str]],
    min_support: float,
    max_length: int,
) -> dict[tuple[str, ...], float]:
    transaction_count = len(transactions)
    frequent: dict[tuple[str, ...], float] = {}

    for length in range(1, max_length + 1):
        counter: Counter[tuple[str, ...]] = Counter()
        for items in transactions:
            unique_items = sorted(set(items))
            if len(unique_items) < length:
                continue
            counter.update(combinations(unique_items, length))

        for itemset, count in counter.items():
            support = count / transaction_count
            if support >= min_support:
                frequent[itemset] = support

    return frequent


def _generate_rules(
    frequent_itemsets: dict[tuple[str, ...], float],
    min_confidence: float,
    min_lift: float,
) -> list[dict[str, Any]]:
    rules: list[dict[str, Any]] = []
    for itemset, support in frequent_itemsets.items():
        if len(itemset) < 2:
            continue

        items = list(itemset)
        for antecedent_size in range(1, len(items)):
            for antecedent in combinations(items, antecedent_size):
                antecedent = tuple(sorted(antecedent))
                consequent = tuple(sorted(set(items) - set(antecedent)))
                antecedent_support = frequent_itemsets.get(antecedent)
                consequent_support = frequent_itemsets.get(consequent)
                if not antecedent_support or not consequent_support:
                    continue

                confidence = support / antecedent_support
                lift = confidence / consequent_support
                if confidence < min_confidence or lift < min_lift:
                    continue

                rules.append(
                    {
                        "antecedent": ", ".join(antecedent),
                        "consequent": ", ".join(consequent),
                        "antecedent_size": len(antecedent),
                        "consequent_size": len(consequent),
                        "support": round(support, 6),
                        "confidence": round(confidence, 6),
                        "lift": round(lift, 6),
                    }
                )
    return rules


def mine_association_rules(
    transactions_df: pd.DataFrame,
    config: dict[str, Any],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    transactions = transactions_df["items"].tolist()
    if not transactions:
        return pd.DataFrame(), pd.DataFrame()

    association_cfg = config["association"]
    frequent = _frequent_itemsets(
        transactions=transactions,
        min_support=float(association_cfg["min_support"]),
        max_length=int(association_cfg["max_length"]),
    )

    itemsets_df = pd.DataFrame(
        [
            {
                "itemset": ", ".join(itemset),
                "length": len(itemset),
                "support": round(support, 6),
                "algorithm": association_cfg.get("algorithm", "apriori"),
                "item_level": transactions_df["item_level"].iloc[0] if "item_level" in transactions_df.columns else "",
            }
            for itemset, support in frequent.items()
        ]
    )
    if not itemsets_df.empty:
        itemsets_df = itemsets_df.sort_values(["length", "support"], ascending=[True, False]).reset_index(drop=True)

    rules = _generate_rules(
        frequent_itemsets=frequent,
        min_confidence=float(association_cfg["min_confidence"]),
        min_lift=float(association_cfg["min_lift"]),
    )
    rules_df = pd.DataFrame(rules)
    if not rules_df.empty:
        rules_df["algorithm"] = association_cfg.get("algorithm", "apriori")
        rules_df["item_level"] = (
            transactions_df["item_level"].iloc[0] if "item_level" in transactions_df.columns else ""
        )
        rules_df = rules_df.sort_values(
            ["lift", "confidence", "support"], ascending=[False, False, False]
        ).reset_index(drop=True)
        rules_df = rules_df.head(int(association_cfg["top_n_rules"])).reset_index(drop=True)

    return itemsets_df, rules_df
