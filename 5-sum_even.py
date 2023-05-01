def sum_even_numbers(my_list):
    sum = 0
    for number in my_list:
        if number%2 == 0:
            sum += number
    return sum


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 17, 20]
    print (sum_even_numbers(my_list))