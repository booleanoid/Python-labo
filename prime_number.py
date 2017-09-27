
def is_prime_number(num):
    flg_non_prime_num = False
    for i in range(2, num-1):
        if num % i == 0:
            flg_non_prime_num = True
            break

    return not(flg_non_prime_num)

def get_prime_numbers(num):
    prime_numbers = []

    for i in range(2, num):
        if is_prime_number(i) == True:
            prime_numbers.append(i)

    return prime_numbers

prime_numbers = get_prime_numbers(200)
print(prime_numbers)
