print("!!! Welcome to Din's PyCal !!!")
print("You can do below operations through my Application")

print("Addition ---> +")
print("Subtraction ---> -")
print("Multiplication ---> *")
print("IntegerDivison ---> //") #result in integer value
print("DecimalDivision ---> /") #result in float value
print("Reminder ---> %")
print("Power ---> **")

print("Select one option to do the task--->")   

# operators= ['+','-','*','//','/','%','**']
option= int(input("Select an Option: "))
if(option>=1 and option<=7):
    
    input1 = int(input("Enter one numeric input: "))
    input2 = int(input("Enter another numeric input: "))
    
    if(option == 1):
       print("Result for your operation : ", input1+input2)
    elif(option == 2):
       print("Result for your operation : ", input1-input2)
    elif(option == 3):
       print("Result for your operation : ", input1*input2)
    elif(option == 4):
       print("Result for your operation : ", input1//input2)
    elif(option == 5):
       print("Result for your operation : ", input1/input2)
    elif(option == 6):
        print("Result for your operation : ", input1%input2)
    else:
        print("Result for your operation : ", input1**input2)
    
else:
    print("Please select only given option")
    

print("Thanks for using\nHope Application is useful")




