def int_to_roman(n):
    numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    romans = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    i =12
    roman_numeral = ''
    while n != 0:
        if numbers[i] <= n:
            roman_numeral += romans[i]
            n -= numbers[i]
        else:
            i -= 1
    return roman_numeral


if __name__ == "__main__":
    print(int_to_roman(2023))