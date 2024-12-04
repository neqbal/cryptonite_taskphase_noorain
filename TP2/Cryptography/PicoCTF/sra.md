### Problem 

We have to figure out N.

From the code provided we know the value of e \
Upon connecting to remote server we get the encrypted text and private key d \
From the code it is clear that we need to decrypt the cypher text and send it in order to get the flag.

The problem is that we only know d and e so we cannot directly compute N

e.d = 1 mod(phi)

Where phi = (p-1)(k-1)

e.d - 1 = k(p-1)(q-1)

So we need to find the factors of e.d - 1 

e = 65537 

d = 47521591079241458199990201253488756338892559598687029840178394880552522007233

e.d - 1 = 1845238994787093868829071101511950464175922457296917469750101517162126249781286720

(https://www.alpertron.com.ar/ECM.HTM)
factors = 2^6 × 3^2 × 5 × 587 × 24329 × 129631 × 407807 × 80787 180953 × 1241 605438 156271 × 84761 673627 946307 × 99817 949863 851199 
