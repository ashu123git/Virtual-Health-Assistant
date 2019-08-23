# # # Here 1 glass of water weigh 110 mL.
import pygame
import time
print("\t\t\t\t\t\t\t\t\t\t\t\t\tHELLO, I AM YOUR VIRTUAL ASSISTANT AND I WILL HELP YOU TO BE HEALTHY.")

def music_loop(file,stop):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)
    while True:
        a = input()
        if a == stop:
            pygame.mixer.music.stop()
            break
def Drink_water(msg):
            b = time.asctime(time.localtime(time.time()))
            with open("drank_water.txt","a") as f:
                f.write(f" {msg} on {b} \n")
                print("Get ready for next exercise")
def Eyes_exer(msgg):
               d=time.asctime(time.localtime(time.time()))
               with open("Eyes_Exercise.txt","a") as f:
                          f.write(f"{msgg} on {d} \n")
                          print("Get ready for next exercise")
def Phy_exer(msd):
               e=time.asctime(time.localtime(time.time()))
               with open("physical_ex.txt","a") as f:
                    f.write(f"{msd} on {e} \n")
                    print("Get ready for next exercise")
if __name__ == '__main__':
    do_wat = time.time()
    do_eye = time.time()
    do_phy = time.time()

    water = 5
    eyes = 10
    exercise = 15
    while True:
          if time.time() - do_wat > water:
              print("Drink water : ")
              print("Write Drank if you did your task : ")
              music_loop("water.wav","drank")
              do_wat = time.time()
              Drink_water("Drank water ")
          if time.time() - do_eye > eyes:
              print("Rotate your eyes : ")
              print("Write eydone if you did your task : ")
              music_loop("eyes.wav","eydone")
              do_eye = time.time()
              Eyes_exer("Eye exercise done " )
          if time.time() - do_phy > exercise:
              print("Go and do some exercise")
              print("Write exdone if you did your task : ")
              music_loop("physical.wav","exdone")
              do_phy = time.time()
              Phy_exer("Exercise done  ")