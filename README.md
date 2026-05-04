🌾 AI Crop Recommendation System

> Dynamic Programming · 0/1 Knapsack Algorithm
A web-based GUI tool that helps farmers optimize crop selection within a given budget to maximize agricultural profit.




---

Overviewa

The AI Crop Recommendation System uses the 0/1 Knapsack algorithm (a classic Dynamic Programming technique) to recommend the best combination of crops a farmer should plant — given a fixed budget — in order to maximize total expected profit.

This mirrors a real-world agricultural decision: a farmer has limited capital and must choose which crops to invest in. Not all crops fit within the budget, and each has a different cost and yield. The Knapsack algorithm finds the optimal subset.


---

Algorithm Used — Dynamic Programming (0/1 Knapsack)

Problem Formulation

Variable	Meaning

n	Number of available crops
W	Total budget (capacity)
cost[i]	Investment required for crop i
profit[i]	Expected return from crop i


We want to select a subset of crops such that:

Total cost ≤ Budget W

Total profit is maximized


Recurrence Relation

dp[i][w] = max(    
    dp[i-1][w],                          // don't plant crop i    
    dp[i-1][w - cost[i]] + profit[i]    // plant crop i (if cost[i] ≤ w)    
)

Time & Space Complexity

Metric	Value

Time Complexity	O(n × W)
Space Complexity	O(n × W)


Why Dynamic Programming?

A brute-force approach would check all 2ⁿ subsets of crops — exponential time. DP avoids this by storing solutions to sub-problems (smaller budgets, fewer crops) and building up to the full solution. This is a bottom-up tabulation approach.

Backtracking to Find Selected Crops

After filling the DP table, we trace back from dp[n][W] to identify which crops were selected:

w = budget    
for i in range(n, 0, -1):    
    if dp[i][w] != dp[i-1][w]:    
        selected.append(crops[i-1])    
        w -= crops[i-1]["cost"]


---

Features

Interactive GUI — runs in any web browser, no installation needed

Budget slider — set your investment from ₹1,000 to ₹5,00,000

Add/remove crops — with name, cost, and expected profit

Quick presets — load Kharif, Rabi, or Cash crop datasets instantly

Live ROI badges — color-coded return-on-investment per crop

Results dashboard — shows recommended crops, max profit, total investment, ROI

Profit bar chart — compare all crops visually

DP Table viewer — inspect the full dynamic programming table

Python TUI fallback — command-line version also included



---

Project Structure

ai-crop-recommendation/    
│    
├── index.html          # GUI application (open in browser)    
├── main.py             # TUI / command-line version    
├── data.json           # Sample crop dataset for Python version    
└── README.md           # This file (project report)


---

How to Run

Option 1 — GUI (Recommended)

1. Download or clone this repository


2. Open index.html in any modern web browser (Chrome, Firefox, Edge)


3. Set your budget using the slider or input field


4. Add crops manually or click a preset (Kharif / Rabi / Cash)


5. Click "Find Best Crops" to run the algorithm


6. View recommended crops, profit stats, and the DP table



Option 2 — Python TUI

python main.py

Choose to load from data.json or enter crop data manually

Enter your budget

View recommended crops and maximum profit in the terminal


Requirements: Python 3.x (no external libraries needed)


---

Sample Output

Input:

Crop	Cost (₹)	Expected Profit (₹)

Rice	3,000	5,500
Maize	2,000	4,000
Cotton	4,000	7,000
Soybean	1,500	2,800
Groundnut	2,500	4,500


Budget: ₹8,000

Output (Recommended Crops):

Crop	Cost	Profit

Rice	₹3,000	₹5,500
Maize	₹2,000	₹4,000
Groundnut	₹2,500	₹4,500


Total Investment: ₹7,500

Maximum Profit: ₹14,000

ROI: 86.7%



---

Real-World Relevance

This system models a genuine problem faced by small and marginal farmers who must make careful decisions about which crops to invest in each season. The Knapsack formulation captures:

Limited capital → knapsack capacity

Crop investment → item weight

Expected yield/market value → item value

Best crop portfolio → optimal item selection


The same DP approach is used in financial portfolio optimization, resource allocation in cloud computing, and logistics planning.


---

Concepts Covered

Dynamic Programming (tabulation / bottom-up)

0/1 Knapsack Problem

Backtracking on DP table

Time-space complexity analysis

Greedy vs. DP trade-offs



---

Technologies Used

Layer	Technology

Algorithm	Python 3 / Vanilla JavaScript
GUI	HTML5, CSS3, JavaScript (no frameworks)
Data	JSON
Fonts	Google Fonts (Playfair Display, DM Sans)



---

CCC — AI Crop Recommendation System
