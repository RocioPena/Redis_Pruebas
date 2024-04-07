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
    app.run()
