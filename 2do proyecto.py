class Palindromo:
    def __init__(self, cadena):
        self.cadena = cadena

    @staticmethod
    def esPalindromo(cadena):
        cadena_limpia = ''.join(caracter for caracter in cadena if caracter.isalnum()).lower()
        return cadena_limpia == cadena_limpia[::-1]

    def test(self):
        return self.esPalindromo(self.cadena)

    def __del__(self):
        print(self.cadena.upper())

# Ejemplos de uso
p = Palindromo("radar")
print(p.test())  # Salida: True
p = Palindromo("sonar")
print(p.test())  # Salida: False
