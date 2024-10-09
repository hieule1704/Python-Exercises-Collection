import csv
import random


def create_csv(file_name):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for _ in range(10):
            row = [random.randint(0, 100) for _ in range(10)]
            writer.writerow(row)


def read_csv_and_sum(file_name):
    with open(file_name, mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        line_sums = []
        for row in reader:
            line_sum = sum(int(value) for value in row)
            line_sums.append(line_sum)
        return


def main():
    file_name = 'random_numbers.csv'
    create_csv(file_name)
    sums = read_csv_and_sum(file_name)
    print(sums)


if __name__ == "__main__":
    main()
