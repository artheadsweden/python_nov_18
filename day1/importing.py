import math
from math import sqrt
from math import sqrt as squareroot
import math as mathematics
from math import pi, pow
# from math import * Don't use this


def main():
    print(math.sqrt(9))         # Uses import math
    print(sqrt(9))              # Uses from math import sqrt
    print(squareroot(9))        # Uses from math import sqrt as squareroot
    print(mathematics.sqrt(9))  # Uses import math as mathematics
    print(pi, pow(10, 2))       # Uses from math import pi, pow


if __name__ == '__main__':
    main()
