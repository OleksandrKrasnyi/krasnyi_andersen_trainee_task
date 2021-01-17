def main():
    """
    Takes some numeric and returns some string or None depending on input.
    """
    try:
        number = float(input("Введите число: "))

        if number > 7:
            print("Привет")
        else:
            pass

    except ValueError:
        print("Неверный тип вводных данных, должно быть число "
              "(целое или десятичная дробь).")


if __name__ == "__main__":
    while True:
        main()
