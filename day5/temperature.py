class Temperature:
    def __init__(self, temp=0):
        self.temp_in_c = temp

    def __str__(self):
        return f"°C {self.temp_in_c:.2f} \t °F {self.to_fahrenheit():.2f}"

    def __add__(self, other):
        return Temperature(self.temp_in_c + other.temp_in_c)

    def __sub__(self, other):
        return Temperature(self.temp_in_c - other.temp_in_c)

    def to_fahrenheit(self):
        # °C × 9/5 + 32
        return self.temp_in_c * 9/5 +32

    def to_celsius(self):
        return self.temp_in_c

def main():
    t1 = Temperature(20)
    t2 = Temperature(30)
    print(t1)
    print(t2)
    t3 = t1 + t2
    print(t3)
    t4 = t1 - t2
    print(t4)

if __name__ == '__main__':
    main()
