def main():
    """
    Takes some string and returns some answers
    depending on if the input is valid.
    """
    name_list = {"Вячеслав"}
    name = input("Введите имя (регистр не важен): ").lower().capitalize()

    if name in name_list:
        print(f"Привет, {name}")
    else:
        print("Нет такого имени")


if __name__ == "__main__":
    while True:
        main()
