def main():
    """
    Takes some array as input and
    returns a list which consists of elements which can be integer divided by 3.
    """
    number_array = (input("Введите последовательность чисел через запятую "
                          "(пробелы и/или скобки не имею значения): \n")
                    .replace('(', '').replace(')', '')
                    .replace('[', '').replace(']', '')
                    .replace('{', '').replace('}', '')
                    .replace(' ', '').split(','))

    def element_checker(number_array):
        """
        Takes sequence of elements and if their type corresponds to numeric
        puts them into a new list.
        """
        number_array_only_numbers = []

        for element in number_array:
            if element != "":
                try:
                    if float(element):
                        number_array_only_numbers.append(float(element))

                except ValueError:
                    print(f"{element} не является представителем числового типа.")
            else:
                pass

        return number_array_only_numbers

    def divide_by_3_selector(number_array):
        """
        Takes preprocessed list of only numeric elements and
        filters it by (element % 3 == 0) requirement.
        Returns new filtered list.
        """
        elements_divided_by_3 = []

        for element in number_array:
            if element % 3 == 0:
                elements_divided_by_3.append(int(element))

        return elements_divided_by_3

    number_array_clean = element_checker(number_array)
    divided_by_3_result = divide_by_3_selector(number_array_clean)

    print(f"\nСписок элементов, нацело делящихся на 3:\n{divided_by_3_result}\n")


if __name__ == "__main__":
    while True:
        main()
