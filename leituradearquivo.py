with open('arquivo.txt', 'w')as arquivo:
     arquivo.write("ola, mundo!\n")
     arquivo.write("estou aqui!\n")
     linhas = ['proxima linha', 'outra linha']
     arquivo.writelines(linhas)

texto = "Aqui vai uma mensagem."
with open('arquivoteste.teste', 'w') as arquivo:
     arquivo.write(texto)

arquivo = open('teste2.txt', 'w')
arquivo.write(texto)
arquivo.write("\nOutra linha\n")
arquivo.write("finalizei o texto.")
arquivo.close()


