
def is_odd(number: int) -> bool:
    if number%2 == 0:
        return True
    else:
        return False

def collatz(number: int) -> list:
    numbers: list = []
    while number != 1:
        numbers.append(int(number))  
        if is_odd(number):
            number /= 2
        else:
            number = 3*number+1
    return numbers

def main() -> None:
    print(collatz(2024))
        


if __name__ == "__main__":
    main()