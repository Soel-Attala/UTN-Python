# Ejercicio 9: mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese una frase, se le devolver� la misma frase pero sin espacios
# en blanco, y un contador de cu�ntos caracteres tiene la frase
# Ejemplo:     frase = vivir por siempre en paz
#              frase final = vivirporsiempreenpaz
#              N� de caracteres = 20
frase1 = input('Digite una frase: ')
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f'\nFrase final: {frase1}')
print(f'N� de caracteres: {len(frase1)}')

