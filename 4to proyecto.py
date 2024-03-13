class Logger:
    def __init__(self, file_path="log.txt"):
        """
        Inicializa el Logger.

        Args:
            file_path (str): La ruta del archivo de registro. Por defecto, es 'log.txt' en el directorio actual.
        """
        self.log_file = open(f".\ejercicios.poo\log.txt", "w")  # Abre el archivo en modo escritura
        self.log_count = 0  # Inicializa el contador de registros
        self.log_file.write("--Start log--\n")  # Escribe un mensaje de inicio en el archivo de registro

    def log(self, message):
        """
        Registra un mensaje en el archivo de registro.

        Args:
            message (str): El mensaje que se va a registrar.
        """
        self.log_count += 1  # Incrementa el contador de registros
        self.log_file.write(message + "\n")  # Escribe el mensaje en el archivo de registro

    def __del__(self):
        """
        Método especial llamado cuando el objeto Logger se destruye.
        Cierra el archivo de registro y escribe un mensaje de fin con el recuento total de registros.
        """
        self.log_file.write("--End log: {} log(s)--\n".format(self.log_count))  # Escribe un mensaje de fin con el recuento total de registros
        self.log_file.close()  # Cierra el archivo de registro


class Test:
    def __init__(self):
        """
        Inicializa la prueba creando un Logger.
        """
        self.logger = Logger()  # Crea una instancia de Logger para registrar eventos

    def llamada(self, message):
        """
        Realiza una llamada de prueba y registra un mensaje con el Logger.

        Args:
            message (str): El mensaje de la llamada.
        """
        self.logger.log(message)  # Registra el mensaje utilizando el Logger


test = Test()  # Crea una instancia de la prueba
for i in range(1, 6):
    if i == 1:
        test.llamada("Primera llamada")
    else:
        test.llamada("{}ª llamada".format(i))
