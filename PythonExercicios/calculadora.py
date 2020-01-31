i = 1
    
while i == 1:
    
	print('Calculadora Iniciando...')
    
	n1 = float(input('Digite um n�mero: '))
    
	n2 = float(input('Digite outro n�mero: '))
    
	print('ESCOLHA UMA OPERA��O \n')
    
	print('Adi��o digite add: ')
    
	print('Subtra��o digite sub: ')
    
	print('Multiplica��o digite mult: ')
    
	print('Divis�o digite div: ')
    
	print('Para sair digite exit')
    
	operador = input(': ')
    
	while (operador != exit):
        
		if operador == 'add':
            
			result = n1 + n2
            
			print('A soma dos n�meros �: {:0.2f}'.format(result))
            
			break
            
			continue
        
		elif operador == 'sub':
            
			result = n1 - n2
            
			print('A subtra��o dos n�meros �: {:0.2f}'.format(result))
            
			break
            
			continue
        
		elif operador == 'mult':
            
			result = n1 * n2
            
			print('A Multiplica��o dos n�meros �: {:0.2f}'.format(result))
            
			break
            
			continue
        
		elif operador == 'div':
            
			result = n1 / n2
            
			print('A Divis�o dos n�meros �: {:0.2f}'.format(result))
            
			break
            
			continue
        
		elif operador == 'exit':
            
			i = 0
            
			break