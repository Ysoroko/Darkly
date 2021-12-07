# Feedback Breach
The breach related to the feedback page



### Explanation:
- On this webpage we can 
- If we inspect the source code, we can see the following code in HTML which represents the process of voting:
    ![image](https://user-images.githubusercontent.com/36443074/145009298-3733b978-5a20-4204-9676-e75b4edf851b.png)
- We can manually modify these values, so that when we vote, instead of adding a note between 1 to 10, we will add our own value
- For example, if I modify the value of the voting option "2" to 999999 and then try to vote "2" for Laurie, instead of adding 2 to the average score, she will get 999999

### How to fix:
- Instead of using manual values twice from 1 to 10, we can use the position / index of the element.
- The user must not be able to modify the values he submits!

