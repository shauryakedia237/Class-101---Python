import time
timer_length = int(input("please enter the time in seconds:"))

def countdown_timer(seconds):
   while seconds:
        min=int(seconds/60)
        seconds = int(seconds%60)
        timer=f"{min}:{seconds}"
        
        print (timer,end="\r")
        time.sleep(1)

        seconds-=1
   print("time's up")


countdown_timer(timer_length)