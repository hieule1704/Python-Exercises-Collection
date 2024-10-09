import csv

def main():
    with open("D:\Python\Chuong7\datacsv.csv", newline='') as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in reader:
            print(row[0]," \t| ",row[1])

if __name__ == "__main__":
    main()