"""
AI Crop Recommendation System (Dynamic Programming - Knapsack)
"""

import json

# ------------------------------
# 🔹 DATA HANDLING
# ------------------------------
def load_data(filename="data.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except:
        return None


def get_user_input():
    crops = []
    n = int(input("\nEnter number of crops: "))

    for i in range(n):
        print(f"\nEnter details for crop {i+1}:")
        name = input("Crop name: ")
        cost = int(input("Cost (₹): "))
        profit = int(input("Expected Profit (₹): "))

        crops.append({
            "name": name,
            "cost": cost,
            "profit": profit
        })

    return crops


# ------------------------------
# 🔹 DYNAMIC PROGRAMMING (KNAPSACK)
# ------------------------------
def recommend_crops(crops, budget):
    n = len(crops)

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = crops[i - 1]["cost"]
        profit = crops[i - 1]["profit"]

        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - cost] + profit)
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtracking
    w = budget
    selected = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(crops[i - 1])
            w -= crops[i - 1]["cost"]

    return selected[::-1], dp[n][budget]


# ------------------------------
# 🔹 DISPLAY RESULTS
# ------------------------------
def display_results(selected, max_profit):
    print("\n Recommended Crops:\n")

    total_cost = 0

    for crop in selected:
        print(f"- {crop['name']} | Cost: ₹{crop['cost']} | Profit: ₹{crop['profit']}")
        total_cost += crop['cost']

    print("\n Total Investment:", total_cost)
    print(" Maximum Profit:", max_profit)


# ------------------------------
# 🔹 MAIN PROGRAM
# ------------------------------
def main():
    print(" AI Crop Recommendation System (DP-Based)\n")

    print("Choose input method:")
    print("1. Load from data.json")
    print("2. Enter manually")

    choice = input("\nEnter choice (1/2): ")

    if choice == "1":
        crops = load_data()
        if not crops:
            print(" data.json not found. Switching to manual input.")
            crops = get_user_input()
    else:
        crops = get_user_input()

    print("\nAvailable Crops:\n")
    for crop in crops:
        print(f"{crop['name']} (Cost: ₹{crop['cost']}, Profit: ₹{crop['profit']})")

    budget = int(input("\nEnter your budget (₹): "))

    selected, max_profit = recommend_crops(crops, budget)

    display_results(selected, max_profit)


# ------------------------------
# 🔹 RUN
# ------------------------------
if __name__ == "__main__":
    main()
