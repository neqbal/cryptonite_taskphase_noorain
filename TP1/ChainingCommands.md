# Chaining with semi colons

    hacker@chaining~chaining-with-semicolons:~$ /challenge/pwn ; /challenge/college
    Yes! You chained /challenge/pwn and /challenge/college! Here is your flag:
    pwn.college{Ub6Gd37rNQIhOx1rfuRsQM9m9aD.dVTN4QDL5kzM1czW}

***

&nbsp;

# Your first shell script


    hacker@chaining~your-first-shell-script:~$ touch x.sh
    hacker@chaining~your-first-shell-script:~$ vim x.sh
    hacker@chaining~your-first-shell-script:~$ bash x.sh
    Great job, you've written your first shell script! Here is the flag:
    pwn.college{g8G45bPImt9zlhOn_Kog0xgDZ_Y.dFzN4QDL5kzM1czW}
    hacker@chaining~your-first-shell-script:~$ cat x.sh
    /challenge/pwn;
    /challenge/college

`bash x.sh` tells bash to read its commands from the file instead of stdin

***

&nbsp;

# Redirecting script output

    hacker@chaining~redirecting-script-output:~$ bash x.sh | /challenge/solve
    Correct! Here is your flag:
    pwn.college{8HSr4L3SeZGbf6ZgDWgnkaoD9eG.dhTM5QDL5kzM1czW}

Every command's output in `x.sh` is piped to `/challenge/solve` seperately

***

&nbsp;

# Executable shell script

    hacker@chaining~executable-shell-scripts:~$ touch script.sh
    hacker@chaining~executable-shell-scripts:~$ vim script.sh
    hacker@chaining~executable-shell-scripts:~$ chmod 700 script.sh
    hacker@chaining~executable-shell-scripts:~$ ./script.sh
    Congratulations on your shell script execution! Your flag:
    pwn.college{8svIa-9t51aP_1vZPqi7N3iUf_q.dRzNyUDL5kzM1czW}
    hacker@chaining~executable-shell-scripts:~$ 

