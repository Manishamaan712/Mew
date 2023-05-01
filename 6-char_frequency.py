def character_frequency(string):
    dict_1 = dict()
    for i in string:
        if i in dict_1:
            dict_1[i] = dict_1[i] + 1
        else:
            dict_1[i] = 1
    return dict_1


if __name__ == "__main__":
    string = "khatib licky"
    print(character_frequency(string))