public class Main{
    public static void main(String[] args){
        int x = 10;
        int y = 5;
        int z = x;
        int b = y;
        x = b;
        y = z;
        System.out.printf("X is equals to %d and Y is equals to %d", x,y);
    }
}
