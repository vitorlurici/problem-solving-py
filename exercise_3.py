from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, lpSum, value # type: ignore

# Exercício 3: Empresa Politoy S/A
prob3 = LpProblem("Politoy", LpMaximize)
x1 = LpVariable("Soldados", lowBound=0, cat="Integer")
x2 = LpVariable("Trens", lowBound=0, cat="Integer")
prob3 += 3*x1 + 2*x2, "Lucro"
prob3 += 2*x1 + x2 <= 100, "Acabamento"
prob3 += x1 + x2 <= 80, "Carpintaria"
prob3 += x1 <= 40, "Demanda_Soldados"
prob3.solve()
print("Exercício 3:")
print(f"Soldados: {value(x1)}, Trens: {value(x2)}, Lucro: {value(prob3.objective)}")
