from pygame import mixer
import time
import pygame



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

while True:

    music_player1()
    # # a=int(input("Enter number : "))
    # a=input("if you want to stop this notification enter 'end' : ")
    # if a=="end":
    #     stop_music()
    #     break
    print()
    print("****************Stand up and drind some watter******************")
    music_player1()
    cancel=input("If you want to stop this notification please enter 'drank' : ")
    if cancel=="drank":
        stop_music()
        break


