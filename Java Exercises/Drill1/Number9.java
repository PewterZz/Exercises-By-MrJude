import java.util.Scanner;

public class Main{

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.printf("Enter the temperature in Celcius(C): ");
        int temp = input.nextInt();
        double fah = temp * 1.8 + 32;
        System.out.printf("%d Celsius degree are %f Fahrenheit degrees", temp, fah);


    }
}
