import random

salary = int(input('Enter your salary: '))
bonus = random.choice([False, True])

salary_with_bonus = salary + random.randint(1, salary) if bonus else salary

print(f"{salary}, {bonus} - '{salary_with_bonus}'")
