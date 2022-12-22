package blockchain;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Hash {
    public static String calculateHash(String input) throws NoSuchAlgorithmException {
        MessageDigest sha = MessageDigest.getInstance("SHA-256");
        int i = 0;
        byte[] hash = sha.digest(input.getBytes(StandardCharsets.UTF_8));
        StringBuilder hexHash = new StringBuilder();
        while (i < hash.length) {
            String hex = Integer.toHexString(0xff & hash[i]);
            if (hex.length() == 1)
                hexHash.append('0');
            hexHash.append(hex);
            i++;
        }
        return hexHash.toString();
    }
}