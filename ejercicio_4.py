# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda
if str(texto_1)> str(texto_2):
    print('el texto', texto_1, 'es mayor que', texto_2)
else:
    print('el texto', texto_2, 'es mayor que', texto_1)

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda
texto_11 = int(texto_1)
texto_22 = int(texto_2)
if texto_11 > texto_22:
    print('la variable', texto_11, 'es mayor que', texto_22)
else:
    print('la variable', texto_22, 'es mayor que', texto_11)

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1? 
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así? Porque a las letras se les asiga el mismo orden
# de acuerdo a la escala numérica que ya usamos. Lo que está a la izquierda será menor a lo 
# que está ala derecha.
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
