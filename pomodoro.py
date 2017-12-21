#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""

A simple time management utility that make a sound on every minute and announce
the end of period. It also should track the time by adding the consumed time
to a data base and the make some inference.

"""


from time import sleep
import notify2
import subprocess
from time import strftime
import os

# Starting time and date
starting_time = strftime("%H:%M:%S")
starting_date = strftime("%m-%d-%Y")




class Beep(object):
    ''' Simply make a sound beep to alert the user. '''

    def __init__(self, start_time_distance=1, working_interval=0.03):
        self.start_time_distance = start_time_distance
        self.working_interval = working_interval

    def start(self):
        '''The sound from the begining'''
        os.system('play --no-show-progress --null --channels 1 synth 0.08 sine 7686')
        sleep(self.start_time_distance)
        os.system('play --no-show-progress --null --channels 1 synth 0.08 sine 7686')
        sleep(self.start_time_distance)
        os.system('play --no-show-progress --null --channels 1 synth 0.08 sine 7686')
        sleep(self.start_time_distance)

    def double(self):
        ''' The sound beep for unit time consumed '''
        os.system('play --no-show-progress --null --channels 1 synth 0.08 sine 7686')
        sleep(self.working_interval)
        os.system('play --no-show-progress --null --channels 1 synth 0.08 sine 7686')

    def long(self):
        ''' The sound beep after the pomodoro session is finished. '''
        os.system('play --no-show-progress --null --channels 1 synth 1 sine 7686')

def consume_time():
    def graph():
        ''' Clear the screen and show some stats '''
        subprocess.call("clear")
        print("Pomodoro Session Started for {0} minute(s) at {1} \n"\
              .format(time_to_work, starting_time))
        print("*" * 50)
        print("\n\nMinute(s) Left:  {}\n".format(time_left))
        print("Time Spent With: {}\n\n".format(time_spent_for_domain))
        print("*" * 50)


    def notification(time_spent_for_domain, time_to_work, starting_time, \
                     starting_date, finished_time):
        notify2.init('Pomodoro')
        notice = notify2.Notification("Times's Up For: {}".format(time_spent_for_domain), \
                             "Minute(s) Spent: {0}\nStarted at:  \
                             {1} {2}\nEnded at:  {3}".format(time_to_work, \
                                                         starting_time, \
                                                         starting_date, \
                                                         finished_time) )
        notice.show()


    def write_stats(time_left):
        # with open("/tmp/pomodoro_time", "w") as f:
        with open("pomodoro_time", "w") as f:
            f.write("Minute(s) Left:  {}".format(time_left))


    # Query about the time and how will be spended the time.
    time_to_work = int(input("\n\n\nMinutes to workout?   ")) #mins
    time_left = time_to_work

    #Prettify
    print("_" * 50)

    time_spent_for_domain = input("What are you working?   ")

    beep = Beep()
    beep.start()

    # Write some stats
    write_stats(time_left)

    while time_left:
        graph()
        sleep(60)
        if time_left == 1:
            beep.long()
        else:
            beep.double()
        time_left -= 1

        # Write some stats
        write_stats(time_left)
        # with open("/tmp/pomodoro_time", "w") as f:
        #     f.write("Minute(s) Left:  {}".format(time_left))

    graph()
    #sleep(3)
    #subprocess.Popen(['spd-say', '-p -30',  'Work done ! Now it\'s {}'.format(h)])
    finished_time = strftime("%H:%M:%S")
    print("\nPomodoro Session Completed at: {}\n".format(finished_time))
    print("#" * 50)

    notification(time_spent_for_domain, time_to_work, starting_time, \
                 starting_date, finished_time)


    consume_time()   # Infinite loop, unlesss CTRL+C




if __name__ == "__main__":
    consume_time()
