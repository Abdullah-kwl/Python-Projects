value=True


year=2000
age=21
real_age=age


while value:
    print(""" we can also pridict your age to up-coming next years
              if you want to continus press 'c'
              if you want to quit  press 'q'
              """)
    print()

    x=input("please enter 'c' or 'q' : ")
    # while x!="c" or x!= "q":
    #     x=input("please entr 'c' or 'q' : ")

    
    while x!="c" and x!= "q":
        x=input("please entr 'c' or 'q' : ")


    if x=='q':
        value=False
        break
    else:

        if year>0:

            pr=int(input("please enter any century grater then 2021 (e.g 2025) :  "))
            while pr <=2021:
                print("please enter century more than 2021")
                pr=int(input("please enter any century grater then 2021 (e.g 2025) :  "))
            
            pr_age= real_age+(pr-2021)
            if pr_age > 130:
                print("it seems to be imposible")
                print(f"your age will be {pr_age}")
                value=False
            else:
                print(f"your age will be {pr_age}")
                value=False


        if age>0:
            pr=int(input("please enter your pridiction how many years you will be live more (e.g 50)"))
            while pr<1:
                print("please enter positive numbr grater then 0 ")
                pr=int(input("please enter your pridiction how many years you will be live more (e.g 50)"))

            print(f"your will be living in {2021+pr}")
            value=False


    
    
    value=False
