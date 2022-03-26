import java.util.Scanner;

public class PrintArray{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of items: ");
        int NUM_ITEMS = input.nextInt();
        int[] items = new int[NUM_ITEMS];
        System.out.print("Enter the value of all items (seperated by space): ");
        for(int i = 0; i < NUM_ITEMS; i++){
            items[i] = input.nextInt();
        }

        System.out.print("The values are: [");
        for(int i = 0; i < NUM_ITEMS; i++){
            System.out.print(items[i]);
            if(NUM_ITEMS > i+1) {
                System.out.print(",");
            }
        }
        System.out.print("]");


    }
}
