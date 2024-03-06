import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <=min <=max <= 1000) or quantity < 0:
        return[]
    if quantity >= max - min + 1:
        return list(range(min,max +1))
    else:
        unique_numbers = set()
        while len(unique_numbers) < quantity:
            unique_numbers.add(random.randint(min,max))
        return sorted(list(unique_numbers))
    
lottery_numbers = get_numbers_ticket(1, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers)