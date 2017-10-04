
def filhos(nomes):
	print ('Filho:' + nomes )

meninos = ['Eduardo','Leonardo','Fernando']

for nomes in meninos:
	filhos(nomes)

	if nomes == 'Eduardo':
		print ("Tem 11 anos")
	elif nomes == 'Leonardo':
		print ("Tem 5 anos")
	elif nomes == 'Fernando':
		print ("Tem 2 meses")
