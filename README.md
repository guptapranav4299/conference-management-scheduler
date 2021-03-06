# Conference-Management-Scheduler 

##Note - This task is for Aisle backend developer hiring role

## Problem Statement-
You are planning a big programming conference and have received many proposals
which have passed the initial screen process but you're having trouble fitting them
into the time constraints of the day -- there are so many possibilities! So you write
a program to do it for you.

- The conference has multiple tracks each of which has a morning and afternoon
session.
- Each session contains multiple talks.
- Morning sessions begin at 9am and must finish by 12 noon, for lunch.
- Afternoon sessions begin at 1pm and must finish in time for the networking
event.
- The networking event can start no earlier than 4:00 and no later than 5:00.
- No talk title has numbers in it.
- All talk lengths are either in minutes (not hours) or lightning (5 minutes).
- Presenters will be very punctual; there needs to be no gap between sessions.
Note that depending on how you choose to complete this problem, your solution
may give a different ordering or combination of talks into tracks. This is acceptable;
you don’t need to exactly duplicate the sample output given here.


Test input: <br>
Writing Fast Tests Against Enterprise Rails 60min <br>
Overdoing it in Python 45min <br>
Lua for the Masses 30min <br>
Ruby Errors from Mismatched Gem Versions 45min <br>
Common Ruby Errors 45min <br>
Rails for Python Developers lightning Communicating Over Distance 60min <br>
Accounting-Driven Development 45min <br>
Woah 30min <br>
Sit Down and Write 30min <br>
Pair Programming vs Noise 45min <br>
Rails Magic 60min <br>
Ruby on Rails: Why We Should Move On 60min <br>
Clojure Ate Scala (on my project) 45min <br>
Programming in the Boondocks of Seattle 30min <br>
Ruby vs. Clojure for Back-End Development 30min <br>
Ruby on Rails Legacy App Maintenance 60min <br>
A World Without HackerNews 30min <br>
User Interface CSS in Rails Apps 30min <br>


## To run the program
`python3 main.py`

## To run the tests
`python3 -m unittest tests.py `