import java.util.Scanner;

public class Main {
    static Bank BCA = new Bank("BCA");
    static Scanner input = new Scanner(System.in);

    public static void ClearConsole(){
        System.out.print("\nPress y to continue...");
        String yes = input.next();
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

    public static boolean passwordprotect(int i){
        System.out.printf("Enter the password of %s %s: ", BCA.getCustomerInteger(i).getFirstName(), BCA.getCustomerInteger(i).getLastName());
        int password = input.nextInt();
        return password == BCA.getCustomerInteger(i).getPassword();
    }

    public static void main(String[] args) {
        while (true) {
            System.out.println("Bank Central Asia");
            System.out.printf("Current no. of accounts: (%d) \n", BCA.getNumOfCustomers());
            System.out.println("What would you like to do: ");
            System.out.println("1. Create new account");
            System.out.println("2. Search for account");
            System.out.println("3. Display all accounts");
            System.out.println("4. Deposit to account");
            System.out.println("5. Withdraw from account");
            System.out.println("6. Exit");
            System.out.print("Please enter your desired choice: ");

            int choice = input.nextInt();
            if(choice == 1){
                Account acc = new Account(0);
                System.out.print("Enter first name: ");
                String first = input.next();
                System.out.print("Enter last name: ");
                String last = input.next();
                System.out.println("Enter the secure password (Numeric): ");
                int password = input.nextInt();
                BCA.addCustomer(first, last, password);
                BCA.getCustomerName(last).setAccount(acc);
                ClearConsole();

            }
            else if(choice == 2){
                System.out.println("How ?");
                System.out.println("1. Through index");
                System.out.println("2. Through name");
                choice = input.nextInt();
                if(choice == 1){
                    System.out.print("Index: ");
                    int index = input.nextInt();
                    if(0 < index && index <= BCA.getNumOfCustomers()){
                    System.out.printf("\nFirst Name: %s \n" ,BCA.getCustomerInteger(index-1).getFirstName());
                    System.out.printf("Last Name: %s \n" ,BCA.getCustomerInteger(index-1).getLastName());
                    System.out.printf("Balance in account: %f \n\n" ,BCA.getCustomerInteger(index-1).getAccount().getBalance());
                    ClearConsole();
                    }
                    else{
                        System.out.println("\nInvalid Range");
                    }
                }
                else if(choice == 2){
                    System.out.print("Person's Last name: ");
                    String name = input.next();
                    BCA.getCustomerName(name);
                    System.out.printf("\nFirst Name: %s \n" ,BCA.getCustomerName(name).getFirstName());
                    System.out.printf("Last Name: %s \n" ,BCA.getCustomerName(name).getLastName());
                    System.out.printf("Balance in account: %f \n\n" ,BCA.getCustomerName(name).getAccount().getBalance());
                    ClearConsole();
                }
            }
            else if(choice == 3){
                System.out.println();
                for(int i = 0; i < BCA.getNumOfCustomers(); i++){
                    System.out.printf("Account no.%d \n", i+1);
                    System.out.printf("First name: %s \n", BCA.getCustomerInteger(i).getFirstName());
                    System.out.printf("Last name: %s \n", BCA.getCustomerInteger(i).getLastName());
                    System.out.printf("Balance: %f \n", BCA.getCustomerInteger(i).getAccount().getBalance());
                    System.out.println();
                }
                ClearConsole();
            }
            else if(choice == 4){
                System.out.println("Which account to deposit to ?");
                for(int i = 0; i < BCA.getNumOfCustomers(); i++){
                    System.out.printf("%d. %s %s \n", i+1, BCA.getCustomerInteger(i).getFirstName(), BCA.getCustomerInteger(i).getLastName());
                }
                System.out.println("Please enter the index of your account: ");
                choice = input.nextInt();
                if (passwordprotect(choice-1)) {
                    System.out.println("How much to deposit ?: ");
                    int amount = input.nextInt();
                    BCA.getCustomerInteger(choice - 1).getAccount().deposit(amount);
                    System.out.printf("Amount in account now: %f", BCA.getCustomerInteger(choice - 1).getAccount().getBalance());
                    ClearConsole();
                }
                else{
                    System.out.println("Unrecognized password. Access denied \n");
                }
            }
            else if(choice == 5) {
                System.out.println("Which account to withdraw from ?");
                for (int i = 0; i < BCA.getNumOfCustomers(); i++) {
                    System.out.printf("%d. %s %s \n", i + 1, BCA.getCustomerInteger(i).getFirstName(), BCA.getCustomerInteger(i).getLastName());
                }
                System.out.println("Please enter the index of your account: ");
                choice = input.nextInt();
                if (passwordprotect(choice-1)) {
                    while(true) {
                        System.out.print("How much to withdraw ?: ");
                        int amount = input.nextInt();
                        if(amount <= BCA.getCustomerInteger(choice-1).getAccount().getBalance()) {
                            BCA.getCustomerInteger(choice - 1).getAccount().withdraw(amount);
                            System.out.printf("Amount in account now: %f \n", BCA.getCustomerInteger(choice - 1).getAccount().getBalance());
                            break;
                        }
                        else{
                            System.out.println("Withdraw amount is too much. Nothing was drawn");
                            ClearConsole();
                        }
                    }
                }
            }
            else{
                ClearConsole();
                break;
            }
        }
    }
}
