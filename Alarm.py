import time
from pygame import mixer

def sound():
    mixer.init()
    mixer.music.load("C:\python\Python37\Alarm-Ring-Tone.mp3")

def userinput():

    print("current time is: ",time.strftime("%H:%M:%S"))
    h=(input("Enter  hour: "))
    m=(input("Enter  minutes: "))
    s=(input("Enter  seconds: "))
    alarm(h,m,s)


def alarm(h,m,s):
    n=2

    while True:
        if time.strftime("%H") == h and time.strftime("%M") == m and time.strftime("%S") == s:

            print("hoo hoo!!!! \n")
            break

    sound()
    while n>0:
        mixer.music.play()
        time.sleep(5)
        mixer.music.stop()
        n-=1


    snooze_in = input("Do you want to snooze? press y or n. ")

    if snooze_in == 'y':
        print("The alarm will start in 2 seconds")
        time.sleep(2)
        h=time.strftime("%H")
        m=time.strftime("%M")
        s=time.strftime("%S")

        return alarm(h,m,s)

    else:
        print("have a nice day")
        exit()



if __name__=="__main__":
    userinput()

