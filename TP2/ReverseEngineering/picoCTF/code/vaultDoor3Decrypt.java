package TP2.ReverseEngineering.picoCTF.code;
public class vaultDoor3Decrypt {
    public static void main(String args[]) {
        String s = "jU5t_a_sna_3lpm18gb41_u_4_mfr340";

        char[] res = new char[32];
        int i;
        for(i=0; i<8; i++) {
            res[i] = s.charAt(i);
        }

        for(;i<16; i++) {
            res[i] = s.charAt(23-i);
        }

        for(; i<32; i++) {
            res[i] = s.charAt(46-i);
        }

        for(i=31; i>=17; i -= 2) {
            res[i] = s.charAt(i);
        }

        System.out.println(res);
    }
}
