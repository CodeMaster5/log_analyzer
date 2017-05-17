#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
import psycopg2

"""This python file analyze news database to answer questions"""

# This is the constant value containing the database name.
DBNAME = 'news'

# This is String array containing the questions.
question_list = ["""Who are the authors in the database?""",

                 """What are names of the articles in the database?""",

                 """Who are the authors of each article?""",

                 """What are the logs dates?""",

                 """How many successful logs per date?""",

                 """How many articles has each author written?""",

                 """What are the log paths that were submitted successfully
                 to the log table? Order by number of successful
                 submissions.""",

                 """Can you connect log path to the right article in the
                 articles table?""",

                 """Can you do the same thing above but with authors
                 included this time?""",

                 """What are the most popular three articles of all time?""",

                 """Who are the most popular article authors of all time?""",
                 "On which days did more than 1% of requests lead to errors?"
                 ]

# This is String array containing the sql commands that answer the questions.
reporting_commands = ["""select name, id from authors""",

                      """select articles.title, articles.author from
                      articles group by articles.title, articles.author
                      order by articles.title""",

                      """select articles.title, authors.name from (articles
                      join authors on articles.author = authors.id) group by
                      articles.title, authors.name order by authors.name""",

                      """select time::date from log group by time::date
                      order by time::date""",

                      """select time::date, count(status) from log where
                      status='200 OK' group by time::date order by
                      time::date""",

                      """select authors.name, count(case when authors.id =
                      articles.author then 1 else 0 end) from authors,
                      articles where authors.id = articles.author group by
                      authors.name order by authors.name""",

                      """select regexp_replace(regexp_replace(
                      log.path, '-', ' ', 'g'), '/article/', '') as logname,
                      count(status) as views from log where log.status =
                      '200 OK' and log.path <> '/' group by logname order
                      by views desc""",

                      """select articles.title, log.path from articles, log
                      where log.status='200 OK' and log.path <> '/' and
                      ((substring(regexp_replace(log.path, '/article/', '')
                      from 0 for position('-' in regexp_replace(log.path,
                      '/article/', ''))) like lower(substring(articles.title
                      from 0 for position(' ' in articles.title)))) or
                      (articles.title like 'There are a lot of bears' and
                      log.path like '/article/so-many-bears')) group by
                      articles.title, log.path order by articles.title""",

                      """select articles.title, authors.name, log.path from
                      articles, authors, log where articles.author =
                      authors.id and log.status='200 OK' and log.path <> '/'
                      and ((substring(regexp_replace(log.path, '/article/',
                      '') from 0 for position('-' in regexp_replace(log.path,
                      '/article/', ''))) like lower(substring(articles.title
                      from 0 for position(' ' in articles.title)))) or
                      (articles.title like 'There are a lot of bears' and
                      log.path like '/article/so-many-bears')) group by
                      articles.title, authors.name, log.path order by
                      articles.title""",

                      """select title, count(*) as views
                      from log join articles on log.path =
                      concat('/article/', articles.slug) group by title
                      order by views desc limit 3""",

                      """select authors.name, count(*) as views from authors,
                       articles, log where authors.id = articles.author and
                       log.path = concat('/article/', articles.slug) group by
                       authors.name order by views desc""",

                      """select to_char(date, 'FMMonth FMDD, YYYY'), err/total
                      as ratio from (select time::date as date, count(*) as
                      total, sum((status != '200 OK')::int)::float as err
                      from log group by date) as errors where
                      err/total > 0.01;"""
                      ]

# conn variable connects to the database.
conn = psycopg2.connect(database=DBNAME)

# cursor variable executes the string sql command.
cursor = conn.cursor()

# Loops through question_list and reporting_commands variables,
# the range starts 9 to only display only the required questions for the lab.
for i in range(9, len(question_list)):
    # Prints the question in the i index of question_list.
    print(question_list[i])
    # Executes the string sql command in the i index of reporting_commands.
    cursor.execute(reporting_commands[i])
    # Loops through the table resulted from the executed command.
    for result in cursor.fetchall():
        # Prints new line and a tab.
        print("\n\t", end="")
        # Loops through the columns in the row of the resulted table.
        for value in result:
            # Converts the value to a string, handles cases when the value is
            # not a string.
            str_value = str(value)
            # Justified the value string.
            print(str_value.ljust(40, ' '), end="")
        # Prints a new line after every row.
        print("\n")
    # Prints a new line.
    print("-" * 70)

# The connection to the database is closed.
conn.close()
