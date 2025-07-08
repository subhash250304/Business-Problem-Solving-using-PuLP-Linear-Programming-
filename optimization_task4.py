# optimization_task4.py

import pulp

# Create the Linear Programming problem
model = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Decision variables
chairs = pulp.LpVariable("Chairs", lowBound=0, cat="Integer")
tables = pulp.LpVariable("Tables", lowBound=0, cat="Integer")

# Objective function
model += 20 * chairs + 30 * tables, "Total Profit"

# Constraints
model += 4 * chairs + 3 * tables <= 240, "Wood Constraint"
model += 2 * chairs + 4 * tables <= 160, "Labor Constraint"

# Solve the problem
model.solve()

# Results
print("Status:", pulp.LpStatus[model.status])
print("Optimal number of Chairs to produce:", chairs.varValue)
print("Optimal number of Tables to produce:", tables.varValue)
print("Maximum Profit: ₹", pulp.value(model.objective))
