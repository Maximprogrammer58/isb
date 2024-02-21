import java.util.Random;

public class RandomGeneratorJava {
    public static void main(String[] args) {
        final int NUMBER_BITS = 128;
        Random random = new Random();
        for (int i = 0; i < NUMBER_BITS; i++) {
            System.out.print(random.nextInt(2));
        }
        System.out.println();
    }
}