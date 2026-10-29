# 20. Store deposits and withdrawals in a file. Read the file and calculate total deposits, total withdrawals, final balance, and largest transaction.

file = open("transactions.txt","r")
lines = file.readlines()
file.close()

deposits = 0
withdrawals = 0
largest = 0

for line in lines:
    data = line.strip().split(",")

    transaction = data[0]
    amount = float(data[1])

    if transaction == "deposit":
        deposits += amount
    elif transaction == "withdrawal":
        withdrawals += amount

    if amount > largest:
        largest = amount

balance = deposits - withdrawals

print("total deposits =",deposits)
print("total withdrawals =",withdrawals)
print("final balance =",balance)
print("largest transaction =",largest)
