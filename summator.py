import time


def sum_numbers():
    while True:
        try:
            with open('./data/numbers.txt', 'r') as f:
                numbers = f.readlines()
            numbers = [int(num.strip()) for num in numbers]
            total_sum = sum(numbers)
            print(f"Sum of numbers: {total_sum}")
        except FileNotFoundError:
            print("No numbers to sum yet.")
        time.sleep(5)


if __name__ == "__main__":
    sum_numbers()
