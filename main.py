"""
AI Crop Recommendation System
Dynamic Programming - 0/1 Knapsack Algorithm
"""

import json


# ─── DATA HANDLING ────────────────────────────────────────────────────────────

def load_data(filename="data.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print("  Error: data.json is malformed.")
        return None


def get_user_input():
    crops = []
    n = int(input("\nEnter number of crops: "))
    for i in range(n):
        print(f"\nCrop {i + 1}:")
        name   = input("  Name:             ")
        cost   = int(input("  Cost (₹):         "))
        profit = int(input("  Expected Profit (₹): "))
        crops.append({"name": name, "cost": cost, "profit": profit})
    return crops


# ─── DYNAMIC PROGRAMMING ─────────────────────────────────────────────────────

def recommend_crops(crops, budget):
    n  = len(crops)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost   = crops[i - 1]["cost"]
        profit = crops[i - 1]["profit"]
        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + profit)
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find selected crops
    w, selected = budget, []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(crops[i - 1])
            w -= crops[i - 1]["cost"]

    return selected[::-1], dp[n][budget]


# ─── DISPLAY ──────────────────────────────────────────────────────────────────

def display_results(selected, max_profit, budget):
    print("\n" + "=" * 45)
    print("  RECOMMENDED CROPS")
    print("=" * 45)

    if not selected:
        print("  No crops fit within the budget.")
        return

    total_cost = 0
    for crop in selected:
        roi = ((crop["profit"] - crop["cost"]) / crop["cost"] * 100)
        print(f"  🌿 {crop['name']:<12} Cost: ₹{crop['cost']:>6,}  "
              f"Profit: ₹{crop['profit']:>6,}  ROI: {roi:.0f}%")
        total_cost += crop["cost"]

    print("-" * 45)
    print(f"  Total Investment : ₹{total_cost:,}")
    print(f"  Maximum Profit   : ₹{max_profit:,}")
    print(f"  Budget Remaining : ₹{budget - total_cost:,}")
    net = max_profit - total_cost
    overall_roi = (net / total_cost * 100) if total_cost else 0
    print(f"  Net Gain         : ₹{net:,}  ({overall_roi:.1f}% ROI)")
    print("=" * 45)


# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    print("\n" + "=" * 45)
    print("  🌾 AI Crop Recommendation System")
    print("  Algorithm: Dynamic Programming (Knapsack)")
    print("=" * 45)

    print("\nInput method:")
    print("  1. Load from data.json")
    print("  2. Enter manually")
    choice = input("\nChoice (1/2): ").strip()

    if choice == "1":
        crops = load_data()
        if not crops:
            print("  data.json not found. Switching to manual input.")
            crops = get_user_input()
    else:
        crops = get_user_input()

    print("\nAvailable crops:")
    for c in crops:
        print(f"  {c['name']:<12} Cost ₹{c['cost']:,}  Profit ₹{c['profit']:,}")

    budget = int(input("\nEnter your budget (₹): "))

    selected, max_profit = recommend_crops(crops, budget)
    display_results(selected, max_profit, budget)


if __name__ == "__main__":
    main()
    
