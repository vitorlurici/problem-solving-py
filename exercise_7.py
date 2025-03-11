from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, lpSum, value # type: ignore

# Exercício 7: Alimentação com Carne e Ovos
prob7 = LpProblem("Alimentacao", LpMinimize)
x1 = LpVariable("Carne", lowBound=0)
x2 = LpVariable("Ovos", lowBound=0)
prob7 += 3*x1 + 2.5*x2, "Custo"
prob7 += 4*x1 + 8*x2 >= 32, "Vitaminas"
prob7 += 6*x1 + 6*x2 >= 36, "Proteinas"
prob7.solve()
print("Exercício 7:")
print(f"Carne: {value(x1)}, Ovos: {value(x2)}, Custo: {value(prob7.objective)}")