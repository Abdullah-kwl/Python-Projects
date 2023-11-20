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


def stop_music():
    mixer.music.stop()



print()
print(current_time)
print("Program is startted !")
print()

if current_time >= "09:00:00" and current_time <= "18:33:00":
    


    while current_time >= "09:00:00" and current_time <= "18:32:00":
        time.sleep(1)    
        time1=datetime.datetime.now()
        current_time=datetime.datetime.strftime(time1,("%H:%M:%S"))
        print(current_time)

        
        # for drinking-water
        if current_time=="10:35:00" or current_time=="11:35:00" or current_time=="12:35:00" or current_time=="18:16:00" or current_time=="18:18:00" or current_time=="18:20:00" or current_time=="18:23:00" :
            
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

    
    print("program is end!")
    print("this program will start from 09:00:00 to 17:00:00 ")
    print("start again at correct time")
    
              
else:
    print()
    print("program is end!")
    print("this program will start from 09:00:00 to 17:00:00 ")
    print("start again at correct time")

    































