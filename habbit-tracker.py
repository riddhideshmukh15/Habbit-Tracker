habits=[]
while True:
    print("\n1. Add habit \n2.view habits  \n3.exit")
    choice=input("Enter choice:")

    if choice=="1":
        name=input("Enter habit:")
        habits.append({"name":name,"done":False})
        print("Habit added!")
    elif choice=="2":
        for i,h in enumerate(habits,1):
            print(i,h["name"],"-","Done" if h["done"] else "pending")
            if not habits:
                print("No habits found!")
                
    elif choice=="3":
        print("Thank you for using!")
        break
else:
    print("Invalid choice!")
    

