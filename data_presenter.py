open_file = open("CupcakeInvoices.csv")

for row in open_file:
    print(row)

for row in open_file:
    row = row.rstrip("\n").split(",")
    print(row[2])


for row in open_file:
    row = row.rstrip("\n").split(",")
    quantity = float(row[3])
    price = float(row[4])
    row_total = quantity*price
    print(row_total)

total = 0

for row in open_file:
    row = row.rstrip("\n").split(",")
    total += (int(row[3])*float(row[4]))

print(total)

open_file.close()