def count_users(input_file="input.txt"):
	# print('dojo')
	with open(input_file) as f:
		lines = f.readlines()
		
	emails_normalizados = {
        normalizar(l) for l in lines[1:]
    }
	return len(emails_normalizados)
        

def normalizar(email):
	# print("email", email)
	splited = email.split('@')
	limpo = splited[0].replace('.', "")
	# print(limpo)
	nome_sem_mais = limpo.split('+')[0]
	print(nome_sem_mais)
	resultado = nome_sem_mais + "@" + splited[1]
	print(resultado)
	return resultado