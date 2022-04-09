from random import randint

results = []

while len(results) < 6:
    number = randint(1, 53)
    if number not in results:
        results.append(number)

print(results)