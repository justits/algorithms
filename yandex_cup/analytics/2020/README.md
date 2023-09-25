## user logs

Logs of user activity are stored in the log.csv file.
Each line in the file is one event, which is described in the format:
- date: time of log
- user: user id
- event_type: type of event
- parameter: parameter of event


Based on the log.csv file, perform the following tasks:
1. Let's call a session a sequential set of events of one user.
The session ends if the user has not performed any actions for 30 minutes or more.
   - Combine events into sessions.
   - Find the number of sessions that started on 2020-04-11.


2. The user uploaded an image to the site if he had an event with type **3** and the **picture** parameter.
   - Find the day when the number of unique users who uploaded the image was the maximum.


3. Find the ten-minute interval _[time; time + 10 minutes)_ during which the most events occurred.
If there are several such intervals, specify the beginning of the latest interval.


## deck of cards

From a deck of cards (32 cards) you are given 6 cards in a row. 
With what probability do the cards issued in total give 50 points?

Consider that:
- the jack is 11 points 
- the queen is 12 points
- the king is 13 points
- the ace is 14 points
- The number of points for the remaining cards is the same as their face value.

Round the answer to the sixth digit after the dot.


## movie tickets

When a users buy a ticket, they can specify their email or phone number, or email and phone number at once.
Write an algorithm that, based on a list of such transactions, finds the user who bought the most tickets.
Find the number of lines in the source file that relate to this user.

**Example of linking users by logs:**<br>
user_1@contest.yandex.ru, 880111111111 <br>
user_1@contest.yandex.ru, 880222222222 <br>
user_2@contest.yandex.ru, 880222222222 <br>
user_3@contest.yandex.ru, 880333333333

**first user:**  <br>
user_1@contest.yandex.ru, 880111111111 <br>
user_1@contest.yandex.ru, 880222222222 <br>
user_2@contest.yandex.ru, 880222222222 <br>

**second user:**  <br>
user_3@contest.yandex.ru, 880333333333


## the epidemic on the "Tortuga"
The bosun of the ship "Tortuga" contracted an unknown virus on the last day on land before a long voyage.
The symptoms of the virus carrier appear on the 14th day after the day of infection. 
On the ship "Tortuga", a patient with symptoms immediately goes to self-isolation in the hold and
loses the opportunity to infect others (on the day of symptoms, the patient does not infect anyone).
The number of people infected by one virus carrier per day with an unlimited number of victims
has a binomial distribution with parameters n=10 and p=0.08, and does not depend on the number of other carriers.
There are 124 people on the ship.

On what day of the voyage is it most likely that it will be found that all the people on the ship have been in the hold?


## saw

An array of integers $a_{0}, a_{1}, a_{2}, ..., a_{n-1}$ is called a saw if for any pair $a_{i}, a_{i+1}$ is true::
- $a_{i} ≤ a_{i+1}$ - если i чётно
- $a_{i} ≥ a_{i+1}$ - если i нечётно

Given an array of integers in which k numbers are skipped (in their place are "-") 
and a set of k integers that need to be inserted into the place of the gaps so that the resulting array becomes a "saw".

If there are several solutions, output any one. 
If you cannot create "saw", output 'NO SOLUTION'.