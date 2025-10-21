# Production Planning Problem
# Goal: Maximize profit by deciding how many units of Product A and B to produce
# Constraints:
# 1. Labor hours: 100 hours available
# 2. Material units: 80 units available
# Profit per unit: A = 40, B = 30
# Resource usage per unit: 
#   A -> 2 labor, 1 material
#   B -> 1 labor, 2 material

import pulp

# Step 1: Define the problem
# We are maximizing profit
prob = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Step 2: Define decision variables
# x1 = units of Product A
# x2 = units of Product B
x1 = pulp.LpVariable('Product_A', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('Product_B', lowBound=0, cat='Continuous')

# Step 3: Define the objective function
# Maximize profit = 40*x1 + 30*x2
prob += 40*x1 + 30*x2, "Total_Profit"

# Step 4: Define constraints

# Labor constraint: 2*x1 + 1*x2 <= 100
prob += 2*x1 + 1*x2 <= 100, "Labor_Constraint"

# Material constraint: 1*x1 + 2*x2 <= 80
prob += 1*x1 + 2*x2 <= 80, "Material_Constraint"

# Step 5: Solve the problem
prob.solve()

# Step 6: Display results
print("Status:", pulp.LpStatus[prob.status])  # Shows if optimal solution is found

print("\nOptimal Production Plan:")
for v in prob.variables():
    print(f"{v.name} = {v.varValue}")

print("\nMaximum Profit =", pulp.value(prob.objective))

# Step 7: Visualization (Optional)

import matplotlib.pyplot as plt

# Products and their optimal units
products = ['Product_A', 'Product_B']
units = [x1.varValue, x2.varValue]

# Bar chart
plt.bar(products, units, color='skyblue')
plt.title('Optimal Production Plan')
plt.xlabel('Products')
plt.ylabel('Units to Produce')
plt.show()