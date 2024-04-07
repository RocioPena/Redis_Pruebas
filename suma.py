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
            <input type="submit" value="Sumar">
            </form>
            </body>
            </html>
        """

    def POST(self):
        # # Obtener los números de la lista "numeros" en Redis
        # numeros = redis_connection.lrange('numeros', 0, 1)
        # numero1 = int(numeros[0])
        # numero2 = int(numeros[1])

        # # Realizar la suma de los números
        # suma = numero1 + numero2

        # # Devolver el resultado de la suma
        # return "La suma de {} y {} es: {}".format(numero1, numero2, suma)

        datos = web.input(numero1=None, numero2=None)
        numero1 = int(datos.numero1)
        numero2 = int(datos.numero2)

        redis_connection.rpush('numeros', numero1, numero2)

        redis_connection.expire('numeros', 20)

        suma = numero1 + numero2

        return "La suma de {} y {} es: {}".format(numero1, numero2, suma)

if __name__ == "__main__":
    app.run()
