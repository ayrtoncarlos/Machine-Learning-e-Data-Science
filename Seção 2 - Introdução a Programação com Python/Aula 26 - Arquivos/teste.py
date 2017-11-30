#arq = open("arquivo.txt", 'w')
#arq.write("Machine Learning")
#arq.write("\nLinguagem Python")
#arq.close()

"""
arq = open("arquivo.txt", 'w')

texto = '''Aprendendo Python,
        Machine Learning
        Python é muito legal'''

with open("arquivo.txt", 'w') as f:
    f.write(texto)
"""

with open("arquivo.txt", 'r') as arq:
    #print(arq.readlines())
    
    #for linha in arq.readlines():
        #print(linha)

    #conteudo = arq.readlines()
    #print(conteudo)

    lista = arq.read().splitlines()
    print(lista[0])
