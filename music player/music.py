# we will use these different functions

# pygame.mixer.init()
# mixer.music.load("Music name")
# mixer.music.play("-1 to play continusely , how much time you want to play")
# mixer.music.set_volume(0.9)
# pygame.mixer.Sound("file name") to put the sound effect
# mixer.music.pause()
# mixer.music.unpause()


import pygame
from pygame import mixer


pygame.mixer.init()
# mixer.music.set_volume()
mixer.music.load("tune.mp3")
mixer.music.play(-1)
sound_effect=pygame.mixer.Sound("sound.wav")


while True:
    
    print("""
For pause press          : 1
For un-pause press       : 2
For re-play press        : 3
For sound-effect press   : 4
For Quit                 : 5
-----------------------------
 """)
    
    a=int(input("Enter what you want to do = "))

    if a==1:
        mixer.music.pause()
        
    elif a==2:

        mixer.music.unpause()

    elif a==3:
        mixer.music.play(-1)
    
    elif a==4:
        sound_effect.play()

    elif a==5:
        pygame.quit()
        break

input("press enter to exit ! ")
























