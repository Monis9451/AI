#Practice 1
num1 = 5
num2 = 10
sum = num1 + num2
print("Number = " + str(num1))
print("Number = " + str(num2))
print("Sum = " + str(sum))

#Practice 2
num1=5
num2=10
sum=num1+num2
print("Number="+str(num1))
print("Number="+str(num2))
print("Sum="+str(sum))

#Practice 3
initialVelocity=float(input("Enter the initial velocity: "))
acceleration=float(input("Enter the acceleration: "))
time=float(input("Enter the time: "))
finalVelocity=initialVelocity+acceleration*time
print("Final velocity is: ",finalVelocity)

#Practice 4
Day=str(input("Enter the day: "))
if Day=="Monday" or Day=="monday":
    print("Chicken Karahi")
elif Day=="Tuesday" or Day=="tuesday":
    print("Biryani")
elif Day=="Wednesday" or Day=="wednesday":
    print("Daal chawal/roti")
elif Day=="Thursday" or Day=="thursday":
    print("Aloo ke parathee")
elif Day=="Friday" or Day=="friday":
    print("Nihari")
elif Day=="Saturday" or Day=="saturday":
    print("Aloo mattar keema")
elif Day=="Sunday" or Day=="sunday":
    print("Chicken Manchoorian")
else :
    print("Invalid day")

#Practice 5
num=int(input("Enter the number: "))
if(num>0):
    print("Number is positive")
elif(num<0):
    print("Number is negative")
else:
    print("Number is zero")

#Practice 6
start=int(input("Enter the start of range: "))
stop=int(input("Enter the end of range: "))
steps=int(input("Enter the steps: "))
for i in range(start,stop,steps):
    print(i)

#Practice 7
Number=int(input("Enter the number: "))
for i in range(11):
    print(Number,"x",i,"=",Number*i)

#Task 1
Radius = float(input("Enter the radius of the cylinder: "))
Height = float(input("Enter the height of the cylinder: "))
Volume = 3.14 * Radius**2 * Height
print(f"The volume of the cylinder is: {Volume}")

#Task 2
Range = int(input("Enter the range: "))
Even = []
Odd = []
for i in range(1, Range+1):
    if i % 2 == 0:
        Even.append(i)
    else:
        Odd.append(i)
print(f"The even numbers are: {Even}")
print(f"The odd numbers are: {Odd}")

#Task 3

Jellies = 10
Juice = 50
Chips = 40
IceCream = 60
Chocolate = 35
SalesTax = 0.05
print("Items:")
print("1. Jellies - 10 rs")
print("2. Juice - 50 rs")
print("3. Chips - 40 rs")
print("4. Ice-Cream - 60 rs")
print("5. Chocolate - 35 rs")

itemNumber = int(input("Enter the item number you want to buy: "))
quantity = int(input("Enter the quantity: "))

if itemNumber == 1:
    price = Jellies
elif itemNumber == 2:
    price = Juice
elif itemNumber == 3:
    price = Chips
elif itemNumber == 4:
    price = IceCream
elif itemNumber == 5:
    price = Chocolate
else:
    print("Invalid item number")
    price = 0
    quantity = 0

totalPrice = price * quantity
tax = totalPrice * SalesTax
totalPriceWithTax = totalPrice + tax

print(f"Total price without tax: {totalPrice} rs")
print(f"Sales tax: {tax} rs")
print(f"Total price with tax: {totalPriceWithTax} rs")

#Task 4

percentage = float(input("Enter the marks: "))
if percentage > 100 or percentage < 0:
    print("Invalid marks")
elif percentage >= 95:
    grade = "A+"
elif percentage >= 85:
    grade = "A"
elif percentage >= 80:
    grade = "B+"
elif percentage >= 75:
    grade = "B"
elif percentage >= 70:
    grade = "C+"
elif percentage >= 65:
    grade = "C"
elif percentage >= 60:
    grade = "D+"
elif percentage >= 55:
    grade = "D"
elif percentage >= 50:
    grade = "E+"
elif percentage >= 45:
    grade = "E"
else:
    grade = "F"

print(f"Grade: {grade}")

#Task 5

books = int(input("Enter the number of books purchased this month: "))
if books == 0:
    points = 0
elif books == 1:
    points = 5
elif books == 2:
    points = 15
elif books == 3:
    points = 30
else:
    points = 60

print(f"Points awarded: {points}")

#Task 6

print("Shapes:")
print("1. Rectangle")
print("2. Circle")
print("3. Cylinder")
shape = int(input("Enter the shape number: "))
if shape == 1:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
elif shape == 2:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius**2
    circumference = 2 * 3.14 * radius
    print(f"Area: {area}")
    print(f"Circumference: {circumference}")
elif shape == 3:
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    volume = 3.14 * radius**2 * height
    surfaceArea = 2 * 3.14 * radius * (radius + height)
    print(f"Volume: {volume}")
    print(f"Surface Area: {surfaceArea}")
else:
    print("Invalid shape number")

#Task 7
sum = 0
print("Enter numbers to add (enter 0 to stop):")
while True:
    number = float(input("Enter a number to add (enter 0 to stop): "))
    if number == 0:
        break
    sum += number

print(f"Sum: {sum}")

#Task 8
print("Number\tSquare")
for i in range(1, 11):
    print(f"{i}\t{i**2}")
    
#Task 9
alphabet = input("Enter an alphabet: ")
if alphabet in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")

#Task 10
start = int(input("Enter a number for start point: "))
stop = int(input("Enter a number for stop point: "))
step = int(input("Enter a number as a step in counting: "))
for i in range(start, stop, step):
    for j in range(0, i):
        print("* ", end="")
    print("\n")

