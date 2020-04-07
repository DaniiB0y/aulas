from random import randint
ppt = ['', 'pedra', 'papel', 'tesoura']
while True:
	choice = int(input("Pedra: 1\n Papel: 2\n Tesoura: 3\n~>"))
	bot = randint(1, 3)
	if choice == bot:
		print(f"Bot jogou {ppt[bot]}")
		print("Empatou")
	elif choice == 1 and bot != 2:
		print(f"Bot jogou {ppt[bot]}")
		print("Ganhou")
	elif choice == 2 and bot != 3:
		print(f"Bot jogou {ppt[bot]}")
		print("Ganhou")
	elif choice == 3 and bot != 1:
		print(f"Bot jogou {ppt[bot]}")
		print("Ganhou")
	else:
		print(f"Bot jogou {ppt[bot]}")
		print("Perdeu")