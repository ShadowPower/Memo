import random

def token_generator(min_length, max_length=None):
    if max_length == None:
        max_length = min_length
    return ''.join(random.sample('qwertyuiopasdfghjklzxcvbnm1234567890',
    random.randrange(min_length, max_length + 1))).replace(" ","")