class IntegerToRoman:
    _val_to_roman = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    def __init__(self, number):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer.")
        if number < 1 or number > 3999:
            raise ValueError("Number must be between 1 and 3999.")
        self.number = number

    def convert(self):
        num = self.number
        roman_numeral = ""
        for value, symbol in self._val_to_roman:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral


if __name__ == "__main__":
    try:
        num = int(input("Enter an integer (1-3999): "))
        converter = IntegerToRoman(num)
        print(f"Roman numeral: {converter.convert()}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
