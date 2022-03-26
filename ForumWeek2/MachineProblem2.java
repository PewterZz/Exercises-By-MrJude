import java.util.Scanner;

public class PrintArrayInStars{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of items: ");
        int NUM_ITEMS = input.nextInt();
        int[] items = new int[NUM_ITEMS];
        System.out.print("Enter the value of all items (seperated by space): ");
        for(int i = 0; i < NUM_ITEMS; i++){
            items[i] = input.nextInt();
        }

        for (int i = 0; i < NUM_ITEMS; i++){
            System.out.printf("%d: ",i);
            System.out.print("*".repeat(items[i]));
            System.out.printf("(%d)\n", items[i]);
        }

    }
}
