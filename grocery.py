file=open("food.txt","r")
buffer=file.readlines()
file.close()
total=0
food=[]
price=[]
for line in buffer:
    line=line.strip()
    line=line.split(",")
    food.append(line[0])
    price.append(float(line[1]))
check = False
while check == False:
    print("Welcome to the grocery store")
    print("1. add to cart")
    print("2. remove from cart")
    print("3. checkout")
    option= input("enter your selection: ")
    if option == "1":
        print(food)
        print(price)
        try:
            x=input("which item would you like to purchace: ")
            x=int(x)
            y=input(f"how many of {food[x]} would you like to buy: ")
            y=int(y)
            total=total+y*price[x]
        except Exception as e:
            print(e)
    if option == "2":
        print(food)
        print(price)
        try:
            x=input("which item would you like to remove: ")
            x=int(x)
            y=input(f"how many of {food[x]} would you like to remove: ")
            y=int(y)
            total=total-y*price[x]
           
        except Exception as e:
            print(e)
    if option == "3":
        tax= total*0.06
        cart=total+tax
        print(f"your total is: {cart}")
        check=True