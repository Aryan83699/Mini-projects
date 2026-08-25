CREATE DATABASE campusx;

USE campusx;

SELECT * FROM smartphones;

# SOLVING SORTING QUESTIONS 

# findings top 5 samsung phones with biggest scr size
SELECT * FROM smartphones 
WHERE brand_name='samsung'
ORDER BY screen_size DESC LIMIT 5;

# sort all the phones in descending order of number of total cameras 
SELECT * FROM smartphones 
ORDER BY (primary_camera_rear+primary_camera_front) DESC;

# sort data on the basis of ppi in decreasing order 
SELECT brand_name,model, ROUND(SQRT((POWER(resolution_width,2)+POWER(resolution_height,2))/screen_size),2) as ppi  FROM smartphones 
ORDER BY ppi DESC;

# find the phone with 2nd largest battery
SELECT brand_name,model,battery_capacity
FROM smartphones
ORDER BY battery_capacity DESC LIMIT 1,1;

# find the name and rating of the worst rated apple phone 
SELECT model,rating 
FROM smartphones 
WHERE brand_name='Apple'
ORDER BY rating ASC LIMIT 1;

# sort phones alphabetically and then on the basis on ratings in desc order 
SELECT * FROM smartphones 
ORDER BY brand_name ASC , rating DESC;

# sort phones alphabetically and then on the basis of price in asc order
SELECT * FROM smartphones 
ORDER BY brand_name ASC , price ASC;



# SOLVING GROUP BY QUESTIONS


# grouping smartphones by brand_name then find the following aggregate values i.e total count , average price , max rating , average scr_size , average battery capacity 
SELECT brand_name, COUNT(model) AS total_count , AVG(price) AS average_price , MAX(rating) AS max_rating , AVG(screen_size) AS avg_scr_size , AVG(battery_capacity) 
FROM smartphones 
GROUP BY brand_name;

# group smartphones by whether they have an NFC and get the avg price and rating 
SELECT has_nfc ,AVG(price), AVG(rating)
FROM smartphones 
GROUP BY has_nfc;

#group smartphones by the extended memory available and get the average price 
SELECT extended_memory_available , AVG(price) FROM smartphones 
GROUP BY extended_memory_available;

#group smartphones by the brand and processor brand and get the count of models and avg primary camera resolution of rear 
SELECT brand_name,processor_brand,COUNT(model),TRUNCATE(AVG(primary_camera_rear),2) AS avg_resolution
FROM smartphones
GROUP BY brand_name,processor_brand;

# find the top 5 most costly phones brands
SELECT brand_name,AVG(price) AS avg_price
FROM smartphones 
GROUP BY brand_name
ORDER BY avg_price DESC LIMIT 5;

# which brand makes the smallest screen smartphones
SELECT brand_name,AVG(screen_size)
FROM smartphones 
GROUP BY brand_name 
ORDER BY AVG(screen_size) LIMIT 1;

# avg price of 5g phones vs avg price of non 5g phones 
SELECT has_5g , AVG(price) 
FROM smartphones
GROUP BY has_5g;

# group smartphones  by the brand and find the brand with the highest number of models that have both NFC and IR blaster 
SELECT brand_name , COUNT(model)
FROM smartphones
WHERE  has_ir_blaster='True' AND has_nfc='True'
GROUP BY brand_name
ORDER BY COUNT(model) DESC;


# find all samsung 5g enabled phones and find out the avg price for NFC and Non-NFC phones
SELECT has_nfc , AVG(price) 
FROM smartphones 
WHERE has_5g='True' AND brand_name='samsung'
GROUP BY has_nfc;

# find the phone name , price of the costliest phone 
SELECT brand_name,model,price FROM smartphones 
ORDER BY price DESC LIMIT 1;



-- DEALING WITH HAVING CLAUSE 

# find the avg rating of smartphones brands which have more than 20 phones 
SELECT brand_name,ROUND(AVG(rating),2)
FROM smartphones 
GROUP BY brand_name
HAVING COUNT(model)>20;

# find the top3 brands with the highest avg ram that have a refresh rate of at least 90Hz and fast charging available and dont consider brands which have less than 10 phones 
SELECT brand_name , AVG(ram_capacity) as avg_ram
FROM smartphones 
WHERE refresh_rate>90 AND fast_charging_available=1
GROUP BY brand_name
HAVING COUNT(*)>10
ORDER BY avg_ram DESC LIMIT 3;


# find the avg price of all the phones brands with avg rating > 70 and num_phones more than 10 among all 5g enables phones
SELECT  brand_name , AVG(price) as avg_price 
FROM smartphones
WHERE has_5g='True'
GROUP BY brand_name
HAVING avg_price > 70 AND COUNT(*) > 10;


-- SOLVING PRACTICE QUESTIONS 
SELECT * FROM ipl;

# find the top 5 batsman in IPL 
SELECT batter , SUM(batsman_run) FROM ipl 
GROUP BY batter
ORDER BY SUM(batsman_run) DESC;

# find the 2nd highest 6 hitters 
SELECT batter,COUNT(*)
FROM ipl 
WHERE batsman_run=6
GROUP BY batter
ORDER BY COUNT(*) DESC LIMIT 1,1;

#find batsman with highest number of centuries 
SELECT batter,id , COUNT(*)
FROM ipl
GROUP BY batter,id
HAVING SUM(batsman_run)>100;

#find the top 5 batsman with highest strike rate who have played a min of 1000 balls
SELECT 
    batter,
    SUM(batsman_run) AS total_runs,
    COUNT(batsman_run) AS balls,
    ROUND((SUM(batsman_run) / COUNT(batsman_run)) * 100, 2) AS sr
FROM ipl
GROUP BY batter
HAVING COUNT(batsman_run) > 1000
ORDER BY sr DESC
LIMIT 5;
