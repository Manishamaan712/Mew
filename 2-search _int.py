def find_first_occurence(my_list, num):
    for index, item in enumerate(my_list):
        if num == item:
            return index
        
        
if __name__ == "__main__":
    list_numbers = [0, 25, 35, 40, 50, 60, 70, 80, 100]
    print(find_first_occurence(list_numbers, 60))