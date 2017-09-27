
def is_prime_number(num):
    flg_non_prime_num = False
    for i in range(2, num-1):
        if num % i == 0:
            flg_non_prime_num = True
            break

    return not(flg_non_prime_num)

prime_numbers = []

for i in range(2, 200):
    if is_prime_number(i) == True:
        prime_numbers.append(i)

print(prime_numbers)
