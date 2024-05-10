import time

def randint(start, end):
    current_millis = int(round(time.time() * 1000))
    pseudo_random_number = (current_millis * 214013 + 2531011) % 2**32
    scaled_number = start + (pseudo_random_number % (end - start + 1))
    return scaled_number

#Для тесту:
# start = 1
# end = 100
# random_number = randint(start, end)
# print(random_number)