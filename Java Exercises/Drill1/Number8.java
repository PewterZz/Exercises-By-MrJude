public class Main {
    static String block = "*";
    static String space = " ";

    static void createbox(int height, int length){
        for(int i = 0; i < length ; i++){
            System.out.printf(block);
        }

        System.out.printf("\n");

        for(int i = 0; i < (height - 2); i++){
            System.out.printf(block);
            System.out.printf(space.repeat(length - 2));
            System.out.println(block);
        }

        for(int i = 0; i < length ; i++){
            System.out.printf(block);
        }
        System.out.println(" ");

    }

    static void createoval(int height, int length){
        System.out.printf(space.repeat(2));
        for(int i = 0; i < (length-4) ; i++){
            System.out.printf(block);
        }
        System.out.printf("\n");
        System.out.printf(space);
        System.out.printf(block);
        System.out.printf(space.repeat(length - 4));
        System.out.println(block);

        for(int i = 0; i < (height - 4); i++){
            System.out.printf(block);
            System.out.printf(space.repeat(length - 2));
            System.out.println(block);
        }
        System.out.printf(space);
        System.out.printf(block);
        System.out.printf(space.repeat(length - 4));
        System.out.println(block);
        System.out.printf(space.repeat(2));
        for(int i = 0; i < (length-4) ; i++){
            System.out.printf(block);
        }
        System.out.println(" ");
    }
    static void createarrow(int height, int length){
         for(int i = 0; i < 5; i++){
             System.out.printf(space.repeat(length/2 - i));
             System.out.println(block.repeat(i+1) + block.repeat(i));
         }
        for(int i = 0; i < (height - 5); i++){
            System.out.println(space.repeat(length/2) + block);
        }
        System.out.println(" ");

    }
    static void creatediamond(int height, int length){
        for(int i = 0; i < 5; i++){
            System.out.printf(space.repeat(length/2 - i));
            System.out.println(block.repeat(i+1) + block.repeat(i));
        }
        for(int i = 4; i > -1; i--){
            System.out.printf(space.repeat(length/2 - i));
            System.out.println(block.repeat(i+1) + block.repeat(i));
        }
        }

    public static void main(String[] args) {
        createbox(9,9);
        createoval(9,9);
        createarrow(9,9);
        creatediamond(9,9);
    }
}
