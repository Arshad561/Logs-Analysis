## Logs Analysis Project
    This is an informative tool from logs by sql database queries. 
    It Interacts with a live db from both command line and the python code.
    
### Technologies used
    PostgreSQL
    inux-based virtual machine (VM) Vagrant
    
### Project Requirements
    Reporting tool should answer the following questions:
        What are the most popular three articles of all time?
        Who are the most popular article authors of all time?
        On which days did more than 1% of requests lead to errors?
        
### System setup and how to view this project
This project makes use of Udacity's Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.

#### Step 1 (Download VirtualBox and install)<br>
VirtualBox is the software that actually runs the virtual machine.<br>
You can download it from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)   

#### Step 2 (Download Vagrant and install)<br>
Vagrant is the software that configures the VM and lets you share files between host and the VM's filesystem.<br>
You can downlaod it from [here](https://www.vagrantup.com/downloads.html)

#### Step 3 (Download the VM configuration)<br>
you can use Github to fork and clone [this](https://github.com/udacity/fullstack-nanodegree-vm) repository.<br>
Change your directory to this repository and do ***cd vagrant***<br>

#### Step 4 (Start the virtual machine)<br>
From your terminal, inside the vagrant subdirectory, run the command ***vagrant up***<br>
This will cause Vagrant to download the Linux operating system and install it.<br>
When vagrant up is finished running, you will get your shell prompt back.<br>
At this point, you can run vagrant ssh to log in to your newly installed Linux VM!

#### Step 5 (Downloading Prerequisite data)<br>
Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)<br>
Unzip this file after downloading it.<br>
The file inside is called **newsdata.sql**<br>
Put this file into the vagrant directory, which is shared with your virtual machine.

#### Step 6 (Loading the data)<br>
To load the data, cd into the vagrant directory and use the command ***psql -d news -f newsdata.sql***<br>

##### Here's what this command does:<br>
**psql**   — the PostgreSQL command line program<br>
**-d news** — connect to the database named news which has been set up for you<br>
**-f newsdata.sql** — run the SQL statements in the file newsdata.sql<br>

#### Step 7 (Creating the views)<br>
The required views are mentioned in **create_views.sql**<br>
You need to just run this command ***psql -d news -f create_views.sql*** to create the views in database.<br>

###### Once you have done all these steps, run this command ***python news.py*** to start the reporting tool. You will see the output in commandline

### Summary:<br>
    vagrant up ---> to start up the VM.
    vagrant ssh ---> to log into the VM.
    cd /vagrant ---> to change to your vagrant directory.
    psql -d news -f newsdata.sql ---> to load the data and create the tables.
    psql -d news -f create_views.sql ---> to create the views which can be reusable.
    python news.py ---> to run the reporting tool.
    pycodestyle news.py ---> to check for code standards and warnings
    
    The code is error free and conforms to the PEP8 style recommendations.<br>
    The code presents its output in clearly formatted plain text.
