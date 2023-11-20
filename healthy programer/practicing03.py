# in this we will reviw the file i/o
import datetime
import time


# from datetime import datetime

time1=datetime.datetime.now()
file_time=datetime.datetime.strftime(time1,f"[ %H:%M:%S , %d-%m-%Y ]")

# with open("log.txt","a") as f:
#     f.write(f"{file_time} i did this work\n") 

current_time=datetime.datetime.strftime(time1,("%H:%M:%S"))
print(current_time)




# if current_time > "14:44:10":
#     print("time up")


# print("asd")
# time.sleep(3)
# print("asd")

# print("-------------------------------------------------------")

# a=0
# while a<1000:
    
#     # time.sleep(1)
#     time1=datetime.datetime.now()
#     current_time=datetime.datetime.strftime(time1,("%H:%M:%S"))
#     print(current_time)
#     a+=1
            