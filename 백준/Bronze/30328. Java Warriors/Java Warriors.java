import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        
        int totalFee = n * 4000;
        
        System.out.println(totalFee);
    }
}
