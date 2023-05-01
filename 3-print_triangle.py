def print_right_triangle(height):
    for i in range(0, height):
        for j in range(i+1):
            print("* ", end="")
        print()
    return print_right_triangle
        

if __name__ == "__main__":
    print(print_right_triangle(5))