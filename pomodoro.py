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
from sys import exit
import pathlib


class Beep(object):
    ''' Simply make a sound beep to alert the user. '''

    def __init__(self, start_time_distance=1, working_interval=0.03):
        self.start_time_distance = start_time_distance
        self.working_interval = working_interval

    def start(self):
        '''The sound from the begining'''
        os.system('play --no-show-progress --null --channels 1 synth 0.08 \
                  sine 7686')
        sleep(self.start_time_distance)
        os.system('play --no-show-progress --null --channels 1 synth 0.08 \
                  sine 7686')
        sleep(self.start_time_distance)
        os.system('play --no-show-progress --null --channels 1 synth 0.08 \
                  sine 7686')
        sleep(self.start_time_distance)

    def double(self):
        ''' The sound beep for unit time consumed '''
        os.system('play --no-show-progress --null --channels 1 synth 0.08 \
                  sine 7686')
        sleep(self.working_interval)
        os.system('play --no-show-progress --null --channels 1 synth 0.08 \
                  sine 7686')

    def long(self):
        ''' The sound beep after the pomodoro session is finished. '''
        os.system('play --no-show-progress --null --channels 1 synth 1 \
                  sine 7686')


def graph(time_spent, starting_time, time_left, concern, finish_time=None):
    ''' Clear the screen and show some stats '''

    subprocess.call("clear")
    print("Pomodoro Session Started for {0} minute(s) at {1} \n"
          .format(time_spent, starting_time))
    print("*" * 50)
    if time_left:
        print("\n\nMinute(s) Left: < {}\n".format(time_left))
        print("Time Spent With: {}\n\n".format(concern))
    else:
        print("Time Spent With: {}\n\n".format(concern))
        print("\nPomodoro Session Completed at: {}\n".format(finish_time))
    print("*" * 50)


def notification(concern, time_spent, starting_time,
                 starting_date, finish_time):
    """ Notification for Ubuntu """

    notify2.init('Pomodoro')
    notice = notify2.Notification("Times's Up For: {}"
                                  .format(concern),
                                  "Minute(s) Spent: {0}\nStarted at: {1} {2}\n"
                                  "Ended at:  {3}".format(time_spent,
                                                          starting_time,
                                                          starting_date,
                                                          finish_time))
    notice.show()


def write_stats(starting_date, starting_time, concern, time_spent, finish_time):
    """ Write some stats on a csv file. """

    path = pathlib.Path('time-management.csv')

    if path.is_file():
        with open('time-management.csv', "a") as f:
            f.write("\n{0}, {1}, {2}, {3}, {4}".format(starting_date,
                                                       starting_time,
                                                       concern,
                                                       time_spent,
                                                       finish_time))
    else:
        with open('time-management.csv', "w") as f:
            f.write("Starting Date, Starting Time, Concern, Time Spent,"
                    " Finish Time")
            f.write("\n")
            f.write("{0}, {1}, {2}, {3}, {4}".format(starting_date,
                                                     starting_time,
                                                     concern,
                                                     time_spent,
                                                     finish_time))


def consume_time(ring=60):
    ''' Manage the time '''

    # Query about the time and how will be spended.
    try:
        time_spent = int(input("\n\n\nMinutes to workout?   "))  # mins
    except Exception as e:
        # Prettify
        print("_" * 50 + "\n")
        print(e)
        print("\nNot a number.Exit !")
        exit()
    time_left = time_spent

    # Prettify
    print("_" * 50)

    concern = input("What are you working?   ")

    # Alert with a beep the user about the tracking time.
    beep = Beep()
    beep.start()

    # Starting time and date
    starting_time = strftime("%H:%M:%S")
    starting_date = strftime("%m-%d-%Y")

    while time_left:
        graph(time_spent, starting_time, time_left, concern)
        sleep(ring)
        if time_left == 1:
            beep.long()
        else:
            beep.double()
        time_left -= 1

    # sleep(3)
    # subprocess.Popen(['spd-say', -p -30',  'Work done ! Your work on {} has \
    #                   finished'.format(concern)])

    finish_time = strftime("%H:%M:%S")

    graph(time_spent, starting_time, time_left, concern, finish_time)
    write_stats(starting_date, starting_time, concern, time_spent, finish_time)
    notification(concern, time_spent, starting_time, starting_date, finish_time)

    # Load the app again, calling recursive function
    consume_time()


if __name__ == "__main__":
    consume_time(3)
