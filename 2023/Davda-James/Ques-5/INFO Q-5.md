* I have used ***PYTHON*** to write this script.
* There are several libraries used in this script so comments are available which will be helping in understand the code.
* I have used google and little gpt for gaining knowledge about requests and smtp server working and libraries use.
* This code checks for deadline only once a day but it can be setup such that it checks at every specific time but to just reduce the number of requests and server load I have set it once.
* In the script we have to provide userid,password for lms account as well as sender's email and receiver's email.
* Using datetime and time module I have checked if time will be less than or equal to 6 hours then it will send remainder otherwise it will went on sleep till the time matches.
