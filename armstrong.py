num=int(input("Enter a number: "))

Sum=0

temp = num

while temp>0:
    digit=temp%10
    Sum+=digit**3
    temp//=10
if num == Sum:
    print(num," is an armstrong number")
else:
    print(num," is not an armstrong number")
