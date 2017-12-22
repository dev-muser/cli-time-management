# Time Management - CLI Pomodoro style

I'm concerned about how i'm spending my time and also i need an assistent to tell me to take a break.

I writed this Time Management Python Application that can track what i'm doing on a specific job, on a specific time unit and also to record my time spent in a simple way.

It's design to work simple, so the app is asking for now just how many minutes would i want to allocate for this job and what i'm working on. Like [pomodoro principles](https://en.wikipedia.org/wiki/Pomodoro_Technique). 

It then start alerting with 3 beeps that is tracking my time. 
For each minute elapsed, the app alerts with a double short beep and show some stats about the begining time, time left and what i'm working on.

When the allocated time is over, the application alert me with a long beep, show some simple stats and also save the stats on a csv file.
