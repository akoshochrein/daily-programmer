
def get_closest_divisible(number):
    closest_low, closest_high = number - 1, number + 1
    if not number % 3:
        return number, 0
    return (closest_high, 1) if not closest_high % 3 else (closest_low, -1)


def main():
    divisor = 3
    number = int(raw_input('What\'s your number? '))
    while number > 1:
        closest_divisible, direction = get_closest_divisible(number)
        number = number // divisor if not number % divisor else closest_divisible
        print number, direction


if __name__ == '__main__':
    main()
