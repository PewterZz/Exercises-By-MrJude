import java.util.Scanner;

public class main2{
    public static void main(String[] args){
        double sum = 0;
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of students: ");
        int numStudents = input.nextInt();
        int[] Scores = new int[numStudents];
        for (int i = 0; i < numStudents; i++){
            System.out.printf("Enter the grade for student %d: ", i+1);
            int number = input.nextInt();
            Scores[i] = number;
        }

        for (int i = 0; i < numStudents; i++){
            sum += Scores[i];
        }

        double average = (sum/numStudents);
        System.out.print("The average is: " + average);
        System.out.println();

        int[] Scores2 = new int[numStudents];
        System.arraycopy(Scores, 0, Scores2, 0 , numStudents);
        for (int i = 0; i+1 < numStudents; i++){
            if(Scores[0] < Scores[i+1]){
                Scores[0] = Scores[i+1];
            }
        }

        for (int i = 0; i+1 < numStudents; i++){
            if(Scores2[0] > Scores2[i+1]){
                Scores2[0] = Scores2[i+1];
            }
        }

        System.out.printf("The minimum is: %d", Scores2[0]);
        System.out.println();
        System.out.printf("The maximum is: %d", Scores[0]);


    }
}
