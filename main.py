from rectangle import Rectangle
from circle import Circle
from square import Square
import emoji


def main():
    r = Rectangle("синего", 3, 3)
    c = Circle("зеленого", 3)
    s = Square("красного", 3)
    print(r)
    print(c)
    print(s)
    print()
    result = emoji.emojize(':red_circle::red_circle::red_circle::red_circle::red_circle:')
    print(result)

if __name__ == "__main__":
    main()