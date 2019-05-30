create view errors as 
    select time::date as date,count(time::date) as count 
    from log 
    where status!='200 OK' 
    group by date;

create view totalrequests as 
    select time::date as date,count(*) as count 
    from log 
    group by date;

create view errorcount as  
    select errors.date, errors.count::double precision/totalrequests.count::double precision * 100 as errorpercentage 
    from errors,totalrequests 
    where errors.date=totalrequests.date;