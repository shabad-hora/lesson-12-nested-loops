

num = int(input("Enter number: "))
binary = ""
x = num

while x > 0:              
    r = x % 2             

    for i in range(1):   
        binary = str(r) + binary

    x = x // 2           

print("Binary of", num, "is", binary)



