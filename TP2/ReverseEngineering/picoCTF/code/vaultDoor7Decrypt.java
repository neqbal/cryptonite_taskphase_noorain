package TP2.ReverseEngineering.picoCTF.code;

public class vaultDoor7Decrypt {
    public static void main(String args[]) {
        int x[] = {1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734291511, 960049251, 1681089078};

        char password[] = new char[32];

        for(int i=0; i<8; i++) {
            password[i*4] = (char) ((x[i] >> 24));
            password[i*4 + 1] = (char) ((x[i] >> 16) & 255);
            password[i*4 + 2] = (char) ((x[i] >> 8) & 255);
            password[i*4 + 3] = (char) (x[i] & 255);
        }

        String s = String.valueOf(password);

        System.out.println("picoCTF{" + s + "}");
    }
}
