#Logs Analysis Project

    Building an informative tool from logs by sql database queries. Interacting with a live database both from the command line and from the python code. This project is a part of the Udacity's Full Stack Web Developer Nanodegree.

#Technologies used

    PostgreSQL
    inux-based virtual machine (VM) Vagrant

#Project Requirements

    Reporting tool should answer the following questions:
        What are the most popular three articles of all time?
        Who are the most popular article authors of all time?
        On which days did more than 1% of requests lead to errors?

The code is error free and conforms to the PEP8 style recommendations.
The code presents its output in clearly formatted plain text.

#System setup and how to view this project

This project makes use of Udacity's Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.

Download Vagrant and install.
Download Virtual Box and install.
Clone this repository to a directory of your choice.
Download the newsdata.sql (not provided here) which contains the "news" database commands and newsdata.py files from the respository and move them to your vagrant directory within your VM.
Run these commands from the terminal in the folder where your vagrant is installed in:

    vagrant up ---> to start up the VM.
    vagrant ssh ---> to log into the VM.
    cd /vagrant ---> to change to your vagrant directory.
    psql -d news -f newsdata.sql ---> to load the data and create the tables.
    python3 newsdata.py ---> to run the reporting tool.

#Views used

1.errors

    create view errors as 
    select time::date as date,count(time::date) as count 
    from log 
    where status='404 NOT FOUND' 
    group by date;

2.totalrequests

    create view totalrequests as 
    select time::date as date,count(*) as count 
    from log 
    group by date;

3.errorcount

    create view errorcount as  
    select errors.date, errors.count::double precision/totalrequests.count::double precision * 100 as errorpercentage 
    from errors,totalrequests 
    where errors.date=totalrequests.date;