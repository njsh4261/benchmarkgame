import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Vector;
import java.util.Arrays;
import java.util.stream.*;

public final class quicksort {

    private final static void swap(int[] array, int index1, int index2) {
        int temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }

    private final static int partition(int[] array, int begin, int end) {
        int smaller_end = begin-1;
        for(int larger_end = begin; larger_end < end; larger_end++){
            if(array[larger_end] <= array[end]){ // the last one is the pivot
                swap(array, ++smaller_end, larger_end);
            }
        }
        swap(array, ++smaller_end, end);
        return smaller_end;
    }

    public final static void quickSort(int[] array, int begin, int end) {
        if(begin < end){
            int split = partition(array, begin, end);
            quickSort(array, begin, split-1);
            quickSort(array, split+1, end);
        }
    }

    public static void main(String[] args) {
        try {
            BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
            int size = Integer.parseInt(bf.readLine());
            int[] intArray = Arrays.stream(bf.readLine().split(" "))
                .mapToInt(Integer::parseInt).toArray();

            quickSort(intArray, 0, size-1);

        } catch (IOException e) {
            System.out.println("IOException occured");
            System.exit(0);
        }
    }
}