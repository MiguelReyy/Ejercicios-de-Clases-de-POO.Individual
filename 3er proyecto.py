class ClaseA:
    def obtener_instancia(self):
        """
        Método de la clase ClaseA que simplemente devuelve la instancia actual.

        Returns:
            self: La instancia actual.
        """
        return self

    def obtener_longitud(self, iterable):
        """
        Método de la clase ClaseA que devuelve la longitud del iterable dado.

        Args:
            iterable (iterable): El iterable del que se desea conocer la longitud.

        Returns:
            int: La longitud del iterable dado.
        """
        return len(iterable)

# Crear una instancia de la clase ClaseA
instancia_a = ClaseA()

# Llamar al método obtener_instancia de la clase ClaseA y asignarlo a la variable obtener_instancia
obtener_instancia = instancia_a.obtener_instancia

# Imprimir el resultado de llamar al método obtener_instancia sobre la instancia_a
print("Resultado de llamar al método obtener_instancia sobre la instancia_a:", type(obtener_instancia()))

# Crear dos instancias diferentes de la clase ClaseA y verificar si son la misma instancia
otra_instancia_a = ClaseA()
print("¿Las instancias otra_instancia_a y instancia_a son la misma instancia?", otra_instancia_a is ClaseA())

# Asignar el método obtener_longitud de la instancia_a a la variable obtener_longitud
obtener_longitud = instancia_a.obtener_longitud

# Imprimir la longitud de una tupla vacía llamando al método obtener_longitud de la instancia_a
print("Longitud de una tupla vacía:", obtener_longitud(()))

# Imprimir la longitud de una tupla que contiene la clase ClaseA como elemento
print("Longitud de una tupla que contiene la clase ClaseA como elemento:", ClaseA().obtener_longitud((ClaseA,)))

# Imprimir la longitud de una tupla que contiene la instancia otra_instancia_a y el método obtener_longitud
print("Longitud de una tupla que contiene la instancia otra_instancia_a y el método obtener_longitud:",
      ClaseA.obtener_longitud(otra_instancia_a, (otra_instancia_a, obtener_longitud)))

# Imprimir la longitud de una tupla que contiene el método obtener_longitud, un entero y una cadena
print("Longitud de una tupla que contiene el método obtener_longitud, un entero y una cadena:",
      otra_instancia_a.obtener_longitud((obtener_longitud, 1, 'cadena')))
