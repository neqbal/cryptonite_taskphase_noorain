package TP2.ReverseEngineering.picoCTF.code;

public class vaultDoor6 {
    public static void main(String args[]) { 
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x6c, 0x61, 0x6d, 0x37, 0x6d, 0x6d, 0x6d,
        };

        char password[] = new char[32];

        for(int i=0; i<32; i++) {
            password[i] = (char) (myBytes[i] ^ 0x55);
        }

        String s = String.valueOf(password);

        System.out.println("picoCTF{" + s + "}");
    }
}