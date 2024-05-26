import time
import random


def generate_numbers():
    while True:
        number = random.randint(1, 100)
        with open('./data/numbers.txt', 'a') as f:
            f.write(f"{number}\n")
        time.sleep(1)


if __name__ == "__main__":
    generate_numbers()
