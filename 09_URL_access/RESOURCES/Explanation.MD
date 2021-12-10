“dot-dot-slash”

Right now, let's try corrupt files on the server side from an URL.

On a sign-in page, I see <</?page=smth>> that means we can see other files on the server.

Let's move to the root little by little <<?page=../../>>

It popups "Wrong", but I guess it is the right way!

So we will reach the <<etc/passwd>> like true hackers!

>http://{IP}/?page=../../../../../../../etc/passwd

<img width="1300" alt="Screen Shot 2021-12-10 at 2 07 10 PM" src="https://user-images.githubusercontent.com/64800542/145578794-db4ac96b-ad4f-4594-9641-510c137e70dc.png">

Here we are!




<img width="1297" alt="Screen Shot 2021-12-10 at 2 09 37 PM" src="https://user-images.githubusercontent.com/64800542/145579010-0892b1cc-6ae9-463a-beb2-220509eb097f.png">

