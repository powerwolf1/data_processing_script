import csv


def main():
    duplicates = []

    with open("username-or-email.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)
        seen_row = set()

        for row in reader:
            row_tuple = tuple(row)

            if row_tuple in seen_row:
                duplicates.append(row_tuple)
            else:
                seen_row.add(row_tuple)

    print(duplicates)


if __name__ == '__main__':
    main()
