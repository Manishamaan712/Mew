def get_smallest_integer(my_list):
    smallest_integer = my_list[0]
    for integer in my_list:
        if integer < smallest_integer:
            smallest_integer = integer
    return smallest_integer


if __name__ == "__main__":
    my_list = [12, 98, 29, 95, 11, 22, 18, 10]
    print(get_smallest_integer(my_list))