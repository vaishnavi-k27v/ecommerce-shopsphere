import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

def add_to_cart(user_id, product_id):
    r.hset(f"cart:{user_id}", product_id, 1)