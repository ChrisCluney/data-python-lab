open_file = open('CupcakeInvoices.csv')


# Loop through all the data and print each row.
for row in open_file:
    # print(row)

    # Loop through all the data and print the type of cupcakes purchased.

    # row = row.split(',')
    # for value in row:
    #     if value == row[2]:
    # print(value)

    # Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need
    # to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float.
    # Research how to do this.).
    # for row in open_file:
    #     values = row.split(',')
    #     total = int(values[3]) * float(values[4])
    # print(total)

    # Loop through all the data, and print out the total for all invoices combined.

    total = 0

    # for row in open_file:
    #     values = row.split(',')
    #     total = total + (int(values[3]) * float(values[4]))
    #     print(total)


total_a = 0
total_b = 0
total_c = 0

for row in open_file:
    item = row.rstrip('\n').split(',')
    for value in item:
        if value == 'Chocolate':
            total_a += 1
        elif value == 'Vanilla':
            total_b += 1
        elif value == 'Strawberry':
            total_c += 1

print("Chocolate's:", total_a)
print("Vanilla's:", total_b)
print("Strawberry's:", total_c)

open_file.close()
