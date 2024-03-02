direita=["s", "b", "p", "w"]
esquerda=["z", "d", "q", "m"]
cD=0
cE=0
guerra=[]
while True:
	k=input("Digite uma letra: ")
	guerra.append(k)
	r=input("Quer continuar?[S/N] ")
	if r in "Nn":
		break
	while r not in "Ss":
			r = input("Quer continuar?[S/N] ")
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