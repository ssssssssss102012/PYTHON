Diccionario_de_palabras = {
    "TRYHARD": "ES cuando una persona es muy bueno es muy bueno en algun juego",
    "PAPEADO": "Es cuando alguen humilla a otra persona",
    "ROTO": "Cuando algo en un juego esta demasiado bueno",
    "NOS ESTAN BAILANDO": "Es cuando el otro equipo nos esta ganando por mucha diferencia",
    "CHIRIPUDO": "ES cuando una persona le pasa algu bueno por suerte"
}
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in Diccionario_de_palabras.keys():
    print(Diccionario_de_palabras[word])
else:
    print("No se encontro la palabra")
