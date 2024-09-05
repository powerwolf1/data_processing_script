import csv


def main():
    duplicates = []

    # Remove duplicates
    with open("username-or-email.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = tuple(next(reader))
        next(reader, None)
        seen_row = set()

        for row in reader:
            row_tuple = tuple(row)

            if row_tuple in seen_row:
                duplicates.append(row_tuple)
            else:
                seen_row.add(row_tuple)

    # Create new cleared document without duplicates
    data = list(seen_row)
    data.insert(0, header)
    writer = csv.writer(open("username-or-email-cleared.csv", "w", newline=''))
    writer.writerows(data)


if __name__ == '__main__':
    main()
