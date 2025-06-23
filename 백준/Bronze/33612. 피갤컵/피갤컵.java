import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int startYear = 2024;
        int startMonth = 8;

        int totalMonths = startMonth + 7 * (N - 1);

        int year = startYear + (totalMonths - 1) / 12;
        int month = totalMonths % 12;
        if (month == 0) month = 12;

        System.out.println(year + " " + month);
    }
}
