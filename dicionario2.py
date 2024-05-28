pais = {'Nome': 'alagoas', 'Capital': 'Maceio'}
print(pais)
print(pais['Capital'])
#pais.clear()

#metodo get()
print(pais.get("Nome", "Não existe"))
print(pais.get("Qualquer", "Não existe"))