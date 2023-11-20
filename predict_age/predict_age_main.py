a=int(input("Enter your age or year in which you born : "))
y=0
ag=0

while a<1:
    print("Please enter the positive number grater then '0' ")
    print("please now enter correctaly !")
    print()
    a=int(input("Enter your age or year in which you born : "))


while a>130 and a<=1895 :
        print("you are entring the wrong value")
        print("If you are humen then this will not be your age or year in which you born")
        print("please now enter correctaly !")
        print()
        a=int(input("Enter your age or year in which you born : "))

while  a>=2021 :
    print("you not yet born")
    print("please now enter correctaly !")
    print()
    a=int(input("Enter your age or year in which you born : "))



if a>1895:
    y=a    
else:
    ag=a


year=y
age=ag



if year>1895:
    print()
    print("You entered yor 'year' in which you born")
    print("your age is : ",(2021-year))
else:
    print()
    print("you entered your 'age' and your's year of birth is : ",(2021-age))



# =======================================================================
# here is part 2---------------------------------------------------------
# =======================================================================



if year>0:
    real_age=2021-year
else:
    real_age=age

# These are the variables of 2nd part  

value=True
x=""



while value:
    print()
    print(""" we can also pridict your age to up-coming next years
              if you want to continus press 'c'
              if you want to quit  press 'q'
              """)
    while x!='c' and x!= 'q':
        x=input("please enter 'c' or 'q' : ")

    if x=='q':
        value=False
        break
    else:

        if year>0:
            print()
            pr=int(input("please enter any century grater then 2021 (e.g 2025) :  "))
            while pr <=2021:
                print("please enter century more than 2021")
                pr=int(input("please enter any century grater then 2021 (e.g 2025) :  "))
            
            pr_age= real_age+(pr-2021)
            if pr_age > 130:
                print("it seems to be imposible")
                print(f"In {pr} your age will be {pr_age}")

                value=False
            else:
                print(f"In {pr} your age will be {pr_age}")
                value=False


        if age>0:

            print()
            pr=int(input("please enter your pridiction how many years you will be live more (e.g 50) : "))
            while pr<1:
                print("please enter positive numbr grater then 0 ")
                pr=int(input("please enter your pridiction how many years you will be live more (e.g 50) : "))

            print(f"your will be living in {2021+pr}")
            print(f"your age will be  {age+pr}")
            value=False


    
    
    value=False



print("*********** Thanks for using our program ***********")
input("<================Press enter to exit=============>")
