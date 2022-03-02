import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.printf("Enter the number of seconds: ");
        var sec = input.nextInt();
        int hour = sec / 3600;
        int mins = (sec % 3600) / 60;
        int sec2 = sec % 3600 % 60;
        System.out.printf("%d seconds are %d hour(s) %d minute(s) %d second(s)",sec, hour, mins, sec2);
    }
}
