def is_prime(number):
    if number>1:
        for i in range(2, number):
            if (number%i) == 0:
                return False
                break
            else:
                return True
    else:
        return False
            
            
if __name__ == "__main__":
    print(is_prime(9))