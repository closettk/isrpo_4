def area(a, b):
    return a * b

def perimeter(a, b):
    return 2 * (a + b)

def main():
    a = float(input("Введите сторону a: "))
    b = float(input("Введите сторону b: "))
    print("Площадь:", area(a, b))
    print("Периметр:", perimeter(a, b))


if __name__ == "__main__":
    main()