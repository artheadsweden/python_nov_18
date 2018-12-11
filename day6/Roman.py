class RomanNumber:
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]

    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    def __init__(self, number):
        if isinstance(number, int):
            self._roman_number = self.int_to_roman(number)
        elif isinstance(number, str):
            self._roman_number = number.upper()
        else:
            raise TypeError("Number must be either int or string")

    def __str__(self):
        return f'RomanNumber("{self._roman_number}")'

    def int_to_roman(self, num):
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // self.val[i]):
                roman_num += self.syb[i]
                num -= self.val[i]
            i += 1
        return roman_num


    def __int__(self):
        # rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rom_val = {r: n for r, n in zip(self.syb, self.val)}
        int_val = 0
        rn = self._roman_number
        for i in range(len(self._roman_number)):
            if i > 0 and rom_val[rn[i]] > rom_val[rn[i - 1]]:
                int_val += rom_val[rn[i]] - 2 * rom_val[rn[i - 1]]
            else:
                int_val += rom_val[rn[i]]
        return int_val


def main():
    number = RomanNumber("xii")
    print(number)
    print(int(number))
    number = RomanNumber(958)
    print(number)
    print(int(number))


if __name__ == '__main__':
    main()
