-- SELECT first_name, last_name FROM users WHERE id = 1;

-- SELECT *  FROM twitter users;

-- SELECT first_name, last_name FROM users WHERE handle = "alleniverson";

-- SELECT first_name, last_name FROM users 
-- ORDER BY first_name ASC;

-- SELECT first_name, last_name FROM users 
-- ORDER BY first_name DESC;

-- SELECT MONTHNAME(birthday) AS birth_month FROM users; 

SELECT COUNT(tweet) AS total_tweets, user_id from tweets
GROUP BY user_id;