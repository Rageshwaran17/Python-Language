# Area Of Triangle

while True:
    try:
        Base = int(input("Base : "))
        Height = int(input("Height : "))
        break
    except:
        print("Invalid Number")

print("Area Of Triangle :",(0.5*Base*Height))
