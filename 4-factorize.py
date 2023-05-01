def factorize(number):
    prime_factorials = []
    divisor = 2
    while divisor <= number:
        if number%divisor == 0:
            prime_factorials.append(divisor)
            number = number/divisor
        else:
            divisor = divisor + 1
    return prime_factorials


if __name__ == "__main__":
    print(factorize(255))