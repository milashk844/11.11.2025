import redis
import config

redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USERNAME,
    password=config.REDIS_PASSWORD,
)

"""success = r.set('foo111', 'bar')
# True

result = redis_client.get('foo111')
print(result)
# >>> bar"""

#1-4 пункт (str)
redis_client.set('car', 'Tesla model 5')
car = redis_client.get("car")
print(redis_client.get("car"))

redis_client.set("pet",'Laska', ex=7200)
pet = redis_client.get('pet')
print(redis_client.get("pet"))

#redis_client.set('myKeyTTL', 'stored_data', exat=datetime.datetime(year=2026, month=2, day=3, hour=3, minute=2))

#5-7 пункт (list)
redis_client.rpush("shopping_list", "хліб", "мука", "яйця", "молоко")
redis_client.expire('shopping_list', 604800)
print(redis_client.lrange("shopping_list", 0, 2))

# 8-12 пункт
redis_client.hset('cake_receipt', mapping={'flour':250, "milk":500})
redis_client.hset('cake_receipt', mapping={'sugar':300})
redis_client.hset('cake_receipt', mapping={'sugar':500})
ingredients = redis_client.hgetall('cake_receipt')
print(redis_client.hgetall('ingredients'))
redis_client.delete('cake_receipt')

#redis_client.expire('user:1234', 1000)
#data_from_dict = redis_client.hgetall('user:1234')
#print(data_from_dict)

#list
#data_from_list = redis_client.lrange('list-key', 0, -1)
# print(data_from_list)

#Delete
#redis_client.delete('list_key', 'user1234')
