from pprint import pprint

def get_prime_number(num):
    non_prime_num_flg = None
    for i in range(2, num-1):
        if num % i == 0:
            non_prime_num_flg = True
            break

    if non_prime_num_flg is None:
        return True
    else:
        return False

prime_numbers = []

for i in range(2, 100):
    if get_prime_number(i) == True:
        prime_numbers.append(i)

pprint(prime_numbers)
