import random
direita=["s", "b", "p", "w"]
esquerda=["z", "d", "q", "m"]
cD=0
cE=0
guerra=[]
z=int(input("Quantas letras? "))
alfa=["s", "b", "p", "w", "z", "d", "q", "m"]
for n in range(0,z):
	c=random.choice(alfa)
	guerra.append(c)
for n in range(1,z):
	print(guerra[n], end="")
print(guerra[len(guerra)-1])
for n in guerra:
	if n in direita:
		k=direita.index(n)+1
		cD=cD+k
	if n in esquerda:
		k=esquerda.index(n)+1
		cE=cE+k
if cD>cE:
	print(f"A direita venceu! {cD}x{cE}")
if cD<cE:
	print(f"A esquerda venceu! {cD}x{cE}")
if cD==cE:
	print(f"Empate! {cD}x{cE}")