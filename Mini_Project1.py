name = str(input("Enter Product Name:"))
price = float(input("Enter Product Price:"))
quantity = int(input("Enter Quantity:"))
member = int(input("Are you a member? (for yes: 1 , for no: 0): "))

print("------SHOPPING BILL------")
print("Product Name:", name)
print("Price:", price)
print("Quantity:", quantity)
total = quantity * price
print("Total Cost:", total)
if member <= 0:
    print("Member: False")
    print("Final Amount:", total)
elif member >= 1:
    print("Member: True")
    final = total * 90/100
    print("Final Amount:", final)
print("------DATA TYPE------")
print("Type of product:",(type(name)))
print("Type of price:",(type(price)))
print("Type of quantity:",(type(quantity)))
print("Type of member:",(type(member)))
print("Type of final amount:",(type(final)))