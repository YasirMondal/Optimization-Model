# Linear Optimization Project – Production Planning

## Problem Statement
This project demonstrates solving a *business optimization problem* using *Linear Programming (LP)* in Python.  
A company produces *Product A* and *Product B*. Each product uses limited resources (labor and materials) and generates profit:

| Product   | Profit per Unit | Labor Hours | Material Units |
|-----------|----------------|------------|----------------|
| A         | 40             | 2          | 1              |
| B         | 30             | 1          | 2              |

*Goal:* Maximize total profit without exceeding available resources:  
- Total labor hours ≤ 100  
- Total material units ≤ 80  


## Solution Approach
1. *Decision Variables:*  
   - x1 = Units of Product A to produce  
   - x2 = Units of Product B to produce  

2. *Objective Function:
   Maximize Profit = 40*x1 + 30*x2

3. Constraints:

2*x1 + 1*x2 <= 100  # Labor constraint
1*x1 + 2*x2 <= 80   # Material constraint
x1, x2 >= 0          # Non-negativity


4. Tool Used: Python with PuLP library to model and solve the LP problem.


How to Run

1. Clone the repository:

git clone <repository-link>
cd linear-optimization-project


2. Create and activate virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate


3. Install dependencies:
pip install -r requirements.txt

4. Run the optimization script:
python optimization.py


5. Output:
Optimal units to produce for Product A and Product B
Maximum achievable profit
Optional bar chart visualization of production plan



Insights

The solution identifies the optimal production quantities for maximizing profit.
Resource constraints (labor and materials) limit production.
Businesses can use this model to analyze “what-if” scenarios, e.g., adding more labor or materials to increase profit.



Tech Stack

Python 3.8+
PuLP – Linear Programming
Matplotlib – Visualization



Author

Yasir Mondal – mondalyasir386@gmail.com

License: 2025 Yasir Mondal

This README is *complete, professional, and fully explains the problem, solution, and usage*.
