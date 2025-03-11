from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, lpSum, value # type: ignore

# Exercício 9: Empresa com Recursos Produtivos
prob9 = LpProblem("Empresa", LpMaximize)
x1 = LpVariable("P1", lowBound=0)
x2 = LpVariable("P2", lowBound=0)
prob9 += 120*x1 + 150*x2, "Lucro"
prob9 += 2*x1 + 4*x2 <= 100, "Recurso_R1"
prob9 += 3*x1 + 2*x2 <= 90, "Recurso_R2"
prob9 += 5*x1 + 3*x2 <= 120, "Recurso_R3"
prob9.solve()
print("Exercício 9:")
print(f"P1: {value(x1)}, P2: {value(x2)}, Lucro: {value(prob9.objective)}")