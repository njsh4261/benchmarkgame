import java.util.Scanner;

public final class fibonacci {
    public final static int fib(int num) {
        if(num == 0){
            return 0;
        }
        else if(num == 1) {
            return 1;
        }
        else {
            return fib(num-1) + fib(num-2);
        }
    }

    public final static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        // int num = Integer.parseInt(args[0]);

        int result = fib(num);
        long endTime = System.currentTimeMillis();

        System.out.println(num + "th fibonacci number: " + result);
        System.out.println("running time: " + (endTime - startTime) + " ms");
    }
}
