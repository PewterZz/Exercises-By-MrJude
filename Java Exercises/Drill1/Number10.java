import java.util.Scanner;
import java.lang.Math;

// all values are double
public class Main{
    public static double mean(double x, double y, double z){
        return (x+y+z)/3;
    }

    public static double variance(double x, double y, double z){
        return ((Math.pow(x - mean(x,y,z),2) + (Math.pow(y - mean(x,y,z),2) + (Math.pow(z - mean(x,y,z),2))))/ 3);
    }

    public static double stddev(double x, double y, double z){
        return Math.sqrt((variance(x, y, z)));
    }
    public static void main(String[] args){
        double answer;
        Scanner input = new Scanner(System.in);
        System.out.printf("What would you like to do? (1. Mean, 2. Variance, 3. Standard Deviation) : ");
        int choice = input.nextInt();
        System.out.printf("Enter the first value : ");
        var x = input.nextDouble();
        System.out.printf("Enter the second value : ");
        var y = input.nextDouble();
        System.out.printf("Enter the third value : ");
        var z = input.nextDouble();
        if(choice == 1){
            answer = mean(x,y,z);
            System.out.println(answer);
        }
        else if(choice == 2){
            answer = variance(x,y,z);
            System.out.println(answer);
        }
        else if(choice == 3){
            answer = stddev(x,y,z);
            System.out.println(answer);
        }

    }
 }
