import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

class SHA1Hashing {

    // Method to calculate the SHA-1 hash of a given text
    public static String calculateSHA1(String text) {
        try {
            // Initialize the SHA-1 MessageDigest
            MessageDigest sha1 = MessageDigest.getInstance("SHA-1");
            
            // Compute the hash of the text
            byte[] hashBytes = sha1.digest(text.getBytes());
            
            // Convert the hash bytes to a hexadecimal string
            StringBuilder sb = new StringBuilder();
            for (byte b : hashBytes) {
                sb.append(String.format("%02x", b));  // Convert each byte to two-digit hex
            }
            
            return sb.toString();
        } catch (NoSuchAlgorithmException e) {
            // Handle the exception if the SHA-1 algorithm is not available
            e.printStackTrace();
            return null;
        }
    }

    // Main method to test the SHA-1 hashing function
    public static void main(String[] args) {
        String text = "hello";  // Sample text to hash
        String sha1Hash = calculateSHA1(text);  // Calculate the SHA-1 hash
        
        // Print the original text and its corresponding SHA-1 hash
        System.out.println("Text: " + text);
        System.out.println("SHA-1 Hash: " + sha1Hash);
    }
}
