# Python Database Analyzer 
This is Python project that analyzes the news database in newsdata.sql to answer questions regarding the log table.

# Usage
##### To run the code, please make sure you have Python version 3 and the newsdata.sql file.
The command to run the Python file: `python3 program_log.py`

# Python Code Example Output
###### Who are the authors in the database?
('Ursula La Multa', 1)
('Rudolf von Treppenwitz', 2)
('Anonymous Contributor', 3)
('Markoff Chaney', 4)


###### What are names of the articles in the database?
('Bad things gone, say good people', 3)
('Balloon goons doomed', 4)
('Bears love berries, alleges bear', 1)
('Candidate is jerk, alleges rival', 2)
("Goats eat Google's lawn", 1)
('Media obsessed with bears', 1)
('There are a lot of bears', 1)
('Trouble for troubled troublemakers', 2)


###### Who are the authors of each article?
('Bad things gone, say good people', 'Anonymous Contributor')
('Balloon goons doomed', 'Markoff Chaney')
('Candidate is jerk, alleges rival', 'Rudolf von Treppenwitz')
('Trouble for troubled troublemakers', 'Rudolf von Treppenwitz')
('Bears love berries, alleges bear', 'Ursula La Multa')
("Goats eat Google's lawn", 'Ursula La Multa')
('Media obsessed with bears', 'Ursula La Multa')
('There are a lot of bears', 'Ursula La Multa')


###### What are the logs dates?
(datetime.date(2016, 7, 1),)
(datetime.date(2016, 7, 2),)
(datetime.date(2016, 7, 3),)
(datetime.date(2016, 7, 4),)
(datetime.date(2016, 7, 5),)
(datetime.date(2016, 7, 6),)
(datetime.date(2016, 7, 7),)
(datetime.date(2016, 7, 8),)
(datetime.date(2016, 7, 9),)
(datetime.date(2016, 7, 10),)
(datetime.date(2016, 7, 11),)
(datetime.date(2016, 7, 12),)
(datetime.date(2016, 7, 13),)
(datetime.date(2016, 7, 14),)
(datetime.date(2016, 7, 15),)
(datetime.date(2016, 7, 16),)
(datetime.date(2016, 7, 17),)
(datetime.date(2016, 7, 18),)
(datetime.date(2016, 7, 19),)
(datetime.date(2016, 7, 20),)
(datetime.date(2016, 7, 21),)
(datetime.date(2016, 7, 22),)
(datetime.date(2016, 7, 23),)
(datetime.date(2016, 7, 24),)
(datetime.date(2016, 7, 25),)
(datetime.date(2016, 7, 26),)
(datetime.date(2016, 7, 27),)
(datetime.date(2016, 7, 28),)
(datetime.date(2016, 7, 29),)
(datetime.date(2016, 7, 30),)
(datetime.date(2016, 7, 31),)


###### How many successful logs per date?
(datetime.date(2016, 7, 1), 38431)
(datetime.date(2016, 7, 2), 54811)
(datetime.date(2016, 7, 3), 54465)
(datetime.date(2016, 7, 4), 54523)
(datetime.date(2016, 7, 5), 54162)
(datetime.date(2016, 7, 6), 54354)
(datetime.date(2016, 7, 7), 54380)
(datetime.date(2016, 7, 8), 54666)
(datetime.date(2016, 7, 9), 54826)
(datetime.date(2016, 7, 10), 54118)
(datetime.date(2016, 7, 11), 54094)
(datetime.date(2016, 7, 12), 54466)
(datetime.date(2016, 7, 13), 54797)
(datetime.date(2016, 7, 14), 54813)
(datetime.date(2016, 7, 15), 54554)
(datetime.date(2016, 7, 16), 54124)
(datetime.date(2016, 7, 17), 54642)
(datetime.date(2016, 7, 18), 55215)
(datetime.date(2016, 7, 19), 54908)
(datetime.date(2016, 7, 20), 54174)
(datetime.date(2016, 7, 21), 54823)
(datetime.date(2016, 7, 22), 54800)
(datetime.date(2016, 7, 23), 54521)
(datetime.date(2016, 7, 24), 54669)
(datetime.date(2016, 7, 25), 54222)
(datetime.date(2016, 7, 26), 53982)
(datetime.date(2016, 7, 27), 54122)
(datetime.date(2016, 7, 28), 54404)
(datetime.date(2016, 7, 29), 54569)
(datetime.date(2016, 7, 30), 54676)
(datetime.date(2016, 7, 31), 45516)


###### How many articles has each author written?
('Anonymous Contributor', 1)
('Markoff Chaney', 1)
('Rudolf von Treppenwitz', 2)
('Ursula La Multa', 4)


###### What are the log paths that were submitted successfully to the log table? Order by number of successful submissions.
('candidate is jerk', 338647)
('bears love berries', 253801)
('bad things gone', 170098)
('goats eat googles', 84906)
('trouble for troubled', 84810)
('balloon goons doomed', 84557)
('so many bears', 84504)
('media obsessed with bears', 84383)


###### Can you connect log path to the right article in the articles table?
('Bad things gone, say good people', '/article/bad-things-gone')
('Balloon goons doomed', '/article/balloon-goons-doomed')
('Bears love berries, alleges bear', '/article/bears-love-berries')
('Candidate is jerk, alleges rival', '/article/candidate-is-jerk')
("Goats eat Google's lawn", '/article/goats-eat-googles')
('Media obsessed with bears', '/article/media-obsessed-with-bears')
('There are a lot of bears', '/article/so-many-bears')
('Trouble for troubled troublemakers', '/article/trouble-for-troubled')


###### Can you do the same thing above but with authors included this time?
('Bad things gone, say good people', 'Anonymous Contributor', '/article/bad-things-gone')
('Balloon goons doomed', 'Markoff Chaney', '/article/balloon-goons-doomed')
('Bears love berries, alleges bear', 'Ursula La Multa', '/article/bears-love-berries')
('Candidate is jerk, alleges rival', 'Rudolf von Treppenwitz', '/article/candidate-is-jerk')
("Goats eat Google's lawn", 'Ursula La Multa', '/article/goats-eat-googles')
('Media obsessed with bears', 'Ursula La Multa', '/article/media-obsessed-with-bears')
('There are a lot of bears', 'Ursula La Multa', '/article/so-many-bears')
('Trouble for troubled troublemakers', 'Rudolf von Treppenwitz', '/article/trouble-for-troubled')


###### What are the most popular three articles of all time?
('Candidate is jerk, alleges rival', 338647)
('Bears love berries, alleges bear', 253801)
('Bad things gone, say good people', 170098)


###### Who are the most popular article authors of all time?
('Ursula La Multa', 507594)
('Rudolf von Treppenwitz', 423457)
('Anonymous Contributor', 170098)
('Markoff Chaney', 84557)


###### On which days did more than 1% of requests lead to errors?
(datetime.date(2016, 7, 17), 2.31506898999214)


