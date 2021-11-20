import redis
from random import randint
from django.conf import settings


redis = redis.Redis(settings.REDIS_HOST,
                    settings.REDIS_PORT,
                    settings.REDIS_DB)


def add_user_to_redis(user, mode):
    EX_TIME = 300
    key = f'{user.username}_{mode.lower()}'
    token = randint(1000, 9999)
    redis.set(key, token, EX_TIME)
    return token


def get_user_from_redis(user, mode):
    key = f'{user.username}_{mode.lower()}'
    return redis.get(key)


def delete_user_from_redis(user, mode):
    key = f'{user.username}_{mode.lower()}'
    redis.delete(key)
    return True
