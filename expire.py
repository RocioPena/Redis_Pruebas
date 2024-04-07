# ESTE MISMO INSERTA LOS NUMEROS Y PONE UN TIEMPO LIMITADO PARA QUE DE BORREN
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
        # Ejemplo: obtener una lista de valores de Redis
        valores = redis_connection.lrange('numeros', 0, -1)
        return "Los valores de la lista son: {}".format(valores)

if __name__ == "__main__":
    # Agregar números a la lista "numeros"
    redis_connection.rpush('numeros', 2, 9)
    # Establecer el tiempo de vida de la lista en 20 segundos
    redis_connection.expire('numeros', 20)

    # Ejecutar la aplicación web
    app.run()
