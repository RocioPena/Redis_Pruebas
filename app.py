# REGRESA SOLO UN DIJITO, OSEA GET
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
    def GET(self):
        # Ejemplo: obtener un valor de Redis
        valor = redis_connection.get('num')
        return "El valor de la clave es: {}".format(valor)

if __name__ == "__main__":
    app.run()
