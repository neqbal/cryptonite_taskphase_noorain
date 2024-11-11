### Problem

Read the source code and figure out the flag

```java
String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
```

```java
public boolean checkPassword(String password) {
    return password.equals("w4rm1ng_Up_w1tH_jAv4_be8d9806f18");
}
```

From the above code it is clear that the flag is `picoCTF{w4rm1ng_Up_w1tH_jAv4_be8d9806f18}`
