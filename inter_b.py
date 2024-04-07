import web
import redis

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())

# Configurar la conexión a Redis
redis_host = 'localhost'
redis_port = 6379
redis_db = 1
redis_connection = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

class Index:
    def GET(self):
        # Renderizar el formulario HTML
        return """
            <html>
            <head>
            <title>Insertar números en Redis</title>
            </head>
            <body>
            <h2>Insertar números en la lista de Redis</h2>
            <form action="/" method="post">
            Número 1: <input type="text" name="numero1"><br>
            Número 2: <input type="text" name="numero2"><br>
            <input type="submit" value="Insertar">
            </form>
            </body>
            </html>
        """

    def POST(self):
        # Obtener los datos del formulario
        datos = web.input(numero1=None, numero2=None)
        numero1 = datos.numero1
        numero2 = datos.numero2

        # Insertar los números en la lista "numeros" de Redis
        redis_connection.rpush('numeros', numero1, numero2)

        # Establecer el tiempo de vida de la lista en 20 segundos
        redis_connection.expire('numeros', 20)

        # Obtener todos los números de la lista
        numeros = redis_connection.lrange('numeros', 0, -1)

        # Mostrar los números insertados
        return "Números insertados: {}".format(numeros)

if __name__ == "__main__":

    app.run()
