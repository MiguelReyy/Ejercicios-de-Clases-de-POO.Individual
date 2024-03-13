class Palindromo:
    @staticmethod
    def esPalindromo(cadena):
        # Convertir la cadena a minúsculas y eliminar los caracteres no alfanuméricos
        cadena_limpia = ''
        for caracter in cadena:
            if caracter.isalnum():
                cadena_limpia += caracter.lower()
        
        # Comparar la cadena original con su reverso
        for i in range(len(cadena_limpia) // 2):
            if cadena_limpia[i] != cadena_limpia[len(cadena_limpia) - 1 - i]:
                return False
        return True

# Ejemplos de uso
print(Palindromo.esPalindromo('radar')) 
print(Palindromo.esPalindromo('sonar')) 
print(Palindromo.esPalindromo('Arde ya la yedra')) 
print(Palindromo.esPalindromo('Ardeyalayedra')) 
print(Palindromo.esPalindromo('!@#$% %$#@!')) 
print(Palindromo.esPalindromo('L O L'))
