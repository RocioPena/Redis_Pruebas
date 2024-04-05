import web
import redis

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())

# Configurar la conexión a Redis
redis_host = 'localhost'
redis_port = 6379
redis_db = 0
redis_connection = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

class Index:
    # def GET(self):
    #     return """
    #     <form action="" method="POST">
    #         Primer número: <input type="text" name="num1"><br>
    #         Segundo número: <input type="text" name="num2"><br>
    #         <input type="submit" value="Enviar">
    #     </form>
    #     """

    def POST(self):
        form = web.input(num1=3, num2=5)
        num1 = form.num1
        num2 = form.num2

        # Ejemplo: Guardar los números en Redis
        redis_connection.set('num1', num1)
        redis_connection.set('num2', num2)

        return "Números guardados en Redis: {} y {}".format(num1, num2)

if __name__ == "__main__":
    app.run()
