# coding: utf-8
from time import sleep
import notify2
import subprocess
from time import strftime
import os


### Initiate 
#notify2.init('Pomodoro')
#n = notify2.Notification('Pomodoro Tehnique', "Time's Up !")
h = strftime("%H:%M:%S")



def double_beep():
    os.system('play --no-show-progress --null --channels 1 synth 0.08 sine 7686')
    sleep(0.05)
    os.system('play --no-show-progress --null --channels 1 synth 0.08 sine 7686')

def consume_time():
    def graph():
        subprocess.call("clear")
        print("Pomodoro Session Started for {0} minute(s) at {1} \n".format(init_time_study, h))
        print("*" * 50)
        print("\n\nMinute(s) Left:  {}\n".format(time_to_study))
        print("Time Spent With: {}\n\n".format(study_tag))
        print("*" * 50)
    
    #print("*" * 50)
    time_to_study = int(input("\n\n\nMinutes to workout?   ")) #mins
    init_time_study = time_to_study
    print("_" * 50)
    study_tag = input("What are you working?   ") 
    #print("_" * 50)
    #print("Pomodoro Session Started for {} minutes \n".format(time_to_study))
    double_beep()
    with open("/tmp/pomodoro_time", "w") as f:
        f.write("Minute(s) Left:  {}".format(time_to_study))
    while time_to_study:
        graph()
        sleep(60)
        if time_to_study == 1:
            os.system('play --no-show-progress --null --channels 1 synth 1 sine 7686')
        else:
            double_beep()
        time_to_study -= 1
        with open("/tmp/pomodoro_time", "w") as f:
            f.write("Minute(s) Left:  {}".format(time_to_study))
        #print('{} minute(s) remaining.'.format(time_to_study))
        
    
    #if time_to_study == 0:
    
    graph()
    #sleep(3)
    #subprocess.Popen(['spd-say', '-p -30',  'Work done ! Now it\'s {}'.format(h)])
    e = strftime("%H:%M:%S")
    print("\nPomodoro Session Completed at: {}\n".format(e))
    print("#" * 50)
    
    #Notification
    notify2.init('Pomodoro')
    n = notify2.Notification("Times's Up For: {}".format(study_tag), "Minute(s) Spent: {0}\nStarted at:  {1}\nEnded at:  {2}".format(init_time_study, h, e) )
    n.show()
    
    
    #print("\n{0} minutes\n{1}\n\n\n".format(init_time_study, study_tag))
    consume_time()   # Infinite loop, unlesss CTRL+C 

    

    
consume_time()
