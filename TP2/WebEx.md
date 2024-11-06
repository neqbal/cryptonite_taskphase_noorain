# Inspect Element

We can use inspect element to view the HTML of the page 

![](./sc/sc1.png)

As we can see the flag is written as a comment in the page

&nbsp;

***

# Intro to Burp 

Burpsuite is a tool which we can use to intercept connection between server and client. It sits between the user's browser and the webserver and allow users to intercept, inspect, modify traffic

To start the challenge we have to starts an instance which gives a URL
The url opens up a registration page on which we can fill any random values and register which returns another page that asks for OTP
Since we dont have any OTP we need to trick server into thinking it never needed an OTP to begin with and since it is requiered to fill the OTP text field we cannot do it simply from the webpage

Now we use burpsuite to intercept data that is sent to the server

![](./sc/sc2.png)

As we can see burpsuite first stops whatever data is to be sent to the server to allow us to modify it

Now we can just remove the OTP field from here

![](./sc/sc3.png)

and forward the modified data which gives us the flag

![](./sc/sc4.png)


&nbsp;

***

# Dont-use-client-side

In this challenge the client side is not trusted which means it needs to verify first. 
We can look at the debugger and then index.js which contains a nested if else statement that verifies whatever is entered

![](./sc/sc5.png)

As we can see this nested if else statements verifies only of a specific string is entered and that specific string is the flag 
So based on the above checks the password should be `picoCTF{no_clients_plz_b706c5}`

We can also use burpsuite to intercept the javascript

![](./sc/sc6.png)

For this we have to modify the proxy settings to allow detection of javascript

![](./sc/sc7.png)


&nbsp;

***

# Where are the robots

Robots in the context of websites is `/robots.txt` \
It is a set of instructions for bots or more specifically good bots like webcrawlers(a bot that systematically browses the internet and collects information). \
It basically tells the webcrawler which parts of the site it is allowed to visit. \
It is used as a prevention measure to stop overloading. 

`robots.txt` is a normal text file that is hosted on a server. It doesnt enforce any rule so bad bots simply ignore them but webcrawlers first vists this url when it first visits a websote.

![](./sc/sc8.png)

as we can see `/477ce.html` is a page that cannot be visited by webcrawlers but we can

![](./sc/sc9.png)

&nbsp;

***

# SQL direct

![](./sc/sc10.png)

`\dt` command displays all the table in the database

`SELECT * FROM flags` displays all the columns and rows in the `flags` table

&nbsp;

***

# Power Cookies

![](./sc/sc11.png)

In this challenge we just had to change the `isAdmin` value from 0 to 1 in our cookies which will basically tell the server that we are an admin.

&nbsp;

***

# Who are you

### Message headers
They are a key value pairs included in the header section of a message being sent over a network protocol like HTTP or email (SMTP) etc.\
It carries the meta data about the message which provides information about the message.

There are several types of message headers such as General headers(Applies to both request and response), request headers(provides information about client's request), response headers(provides information about server's response), entity headers(contains information about the content of the message).

For this challlenge we will look into Request headers

### Request headers

![](./sc/sc13.png)

Headers can be viewed under the network tab of developer tools or we can use bursuite to view it.

&nbsp;

![](./sc/sc12.png)

Under the headers section above there is a request headers section and under that there is a key value pair that states the browser and operating system. 

So we just have to change the value to `PicoBrowser`

![](./sc/sc14.png)

&nbsp;

![](./sc/sc15.png)

To spoof the server into thinking we were directed to this site from the correct url we can use the `Referer` header under request headers

![](./sc/sc16.png)

&nbsp;

![](./sc/sc17.png)

To provide the server with the Date and time at which the message was generated we can use `Date` header.

![](./sc/sc18.png)

&nbsp;

![](./sc/sc19.png)

`DNT` can be used to signal that we dont want to be tracked by websites and third parties.

![](./sc/sc20.png)

&nbsp;

![](./sc/sc21.png)

To specify the IP address we can use `X-Forwaded-For`. 
This header is a custom header i.e it is not included in the IETF RFC standard.
It was introduced by various proxy vendors to realy client's original IP address. 
Since this is an unofficial header, hence it has X at the begining

![](./sc/sc22.png)

&nbsp;

![](./sc/sc23.png)

To specify the language we can use the `Accept-Language` header

![](./sc/sc25.png)

&nbsp;

![](./sc/sc24.png)

&nbsp;

***

# Some Assembly Required



