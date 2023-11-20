import datetime
from pygame import mixer
import pygame
import time


# in this section i set the time objects
time1=datetime.datetime.now()
current_time=datetime.datetime.strftime(time1,("%H:%M:%S"))


# in this section i wrote the music-player funtions

def music_player1():
    pygame.mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.play(-1)

def music_player2():
    pygame.mixer.init()
    mixer.music.load("eyes.mp3")
    mixer.music.play(-1)

def music_player3():
    pygame.mixer.init()
    mixer.music.load("exercise.mp3")
    mixer.music.play(-1)

def stop_music():
    mixer.music.stop()

print()
print(f"current time is : {current_time}")
print("********** ! Program is startted ! **********")
print()
if current_time >= "09:00:00" and current_time <= "17:00:00":


    while current_time >= "09:00:00" and current_time <= "17:00:00":
        # in while we set some time code
        time.sleep(1)    
        time1=datetime.datetime.now()
        current_time=datetime.datetime.strftime(time1,("%H:%M:%S"))
        print(current_time)



        # for drinking-water after every 30 min to half liier 
        if current_time=="10:25:00" or current_time=="11:25:00" or current_time=="12:25:00" or current_time=="13:25:00" or current_time=="14:25:00" or current_time=="15:25:00" or current_time=="16:25:00":
            print()
            print("**********Stand up and drind some watter**********")
            music_player1()
            cancel=input("If you want to stop this notification please enter 'drank' : ")

            while cancel != "drank":
                cancel=input("If you want to stop this notification please enter 'drank' : ")

            if cancel=="drank":
                with open("log.txt","a") as f:
                    file_time=datetime.datetime.strftime(time1,f"[ %H:%M:%S , %d-%m-%Y ]")
                    f.write(f"{file_time} I drank the watter\n") 

                stop_music()


        # for eye-exercise  after 30 min
        if current_time=="09:30:00" or current_time=="10:00:00" or current_time=="10:30:00" or current_time=="11:00:00" or current_time=="11:30:00" or current_time=="12:00:00" or current_time=="12:30:00" or current_time=="13:00:00" or current_time=="13:30:00" or current_time=="14:00:00" or current_time=="14:30:00" or current_time=="15:00:00" or current_time=="15:30:00" or current_time=="16:00:00" or current_time=="16:30:00" :
            print()
            print("**********Stand up and start eyes exercise**********")
            music_player2()
            cancel=input("If you want to stop this notification please enter 'eydone' : ")

            while cancel != "eydone":
                cancel=input("If you want to stop this notification please enter 'eydone' : ")

            if cancel=="eydone":
                with open("log.txt","a") as f:
                    file_time=datetime.datetime.strftime(time1,f"[ %H:%M:%S , %d-%m-%Y ]")
                    f.write(f"{file_time} I did eye-exercise\n") 

                stop_music()
           

        #for physical-exercise after 45 min

        if  current_time=="09:50:00" or current_time=="10:35:00" or current_time=="11:20:00" or current_time=="12:05:00" or current_time=="12:50:00" or current_time=="13:35:00" or current_time=="14:20:00" or current_time=="15:05:00" or current_time=="16:35:00" or current_time=="16:50:00" :
            print()
            print("**********Stand up and start physical exercise**********")
            music_player3()
            cancel=input("If you want to stop this notification please enter 'exdone' : ")

            while cancel != "exdone":
                cancel=input("If you want to stop this notification please enter 'exdone' : ")

            if cancel=="exdone":
                with open("log.txt","a") as f:
                    file_time=datetime.datetime.strftime(time1,f"[ %H:%M:%S , %d-%m-%Y ]")
                    f.write(f"{file_time} i did physical-exercise\n") 

                stop_music()



    # for bracking inside while loop
    print("********** ! program is end      ! **********")
    print("This program will start from 09:00:00 to 17:00:00 ")
    print("Please start again at correct time")
    

else:
    print()
    print("********** ! program is end      ! **********")
    print("This program will start from 09:00:00 to 17:00:00 ")
    print("Please start again at correct time")

    
input("<====Press enter to exit====>")