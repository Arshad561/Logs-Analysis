#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

# query 1: What are the most popular three articles of all time?
popular_articles = """select articles.title, count(*) as count
            from articles, log
            where log.status='200 OK'
            and articles.slug = substr(log.path, 10)
            group by articles.title
            order by count desc
            limit 3;"""

# query 2: Who are the most popular article authors of all time?
popular_authors = """select authors.name, count(*) as count
            from articles, authors, log
            where log.status='200 OK'
            and authors.id = articles.author
            and articles.slug = substr(log.path, 10)
            group by authors.name
            order by count desc;"""

# query 3: On which day did more than 1% of requests lead to errors?
error_days = """select TO_CHAR(date,'fmMonth dd, yyyy'), errorpercentage
        from errorcount
        where errorpercentage > 1;"""


# query connection, execution and closig the connection
def query_execution(query):
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# Print the top three articles of all time
def top_three_articles():
    top_three_articles = query_execution(popular_articles)
    print("\n\t\tTop 3 articles of all time\n")

    for title, count in top_three_articles:
        print(" \"{}\" -- {} views".format(title, count))


# Print the top authors of all time
def top_three_authors():
    top_three_authors = query_execution(popular_authors)
    print("\n\t\tTop authors of all time\n")

    for name, count in top_three_authors:
        print(" {} -- {} views".format(name, count))


# Print the days which has more than 1% of requests lead to errors
def error_dates():
    error_dates = query_execution(error_days)
    print("\n\t\tDays with more than one percentage of error requests\n")

    for date, errorpercentage in error_dates:
        print(" {} -- {:.1f}% errors".format(date, errorpercentage))


if __name__ == '__main__':
    top_three_articles()
    top_three_authors()
    error_dates()
