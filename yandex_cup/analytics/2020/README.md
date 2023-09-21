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