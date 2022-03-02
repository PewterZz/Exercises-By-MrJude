import java.util.Scanner;
import java.lang.Math;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.printf("Enter the coefficient of X^2: ");
        var a = input.nextDouble();
        System.out.printf("Enter the coefficient of X: ");
        var b = input.nextDouble();
        System.out.printf("Enter the constant number: ");
        var c = input.nextDouble();
        if(a == 0){
            System.out.println("Invalid");
        }
        else{
            double answerPos = ((-b) + Math.sqrt(Math.pow(b,2)-(4*a*c)))/(2*(a));
            double answerNeg = ((-b) - Math.sqrt(Math.pow(b,2)-(4*a*c)))/(2*(a));
            System.out.println(answerNeg);
            System.out.println(answerPos);
        }


    }
}
