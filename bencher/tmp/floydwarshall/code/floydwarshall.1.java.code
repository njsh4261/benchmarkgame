import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Vector;
import java.util.Arrays;

public final class floydwarshall {
    private static int vertexNum;
    private static int[][] graph;

    // private static Vector<HashMap<Integer, Integer>> graph;

    private final static void readInput() {
        try {
            BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
            vertexNum = Integer.parseInt(bf.readLine());
            graph = new int[vertexNum][vertexNum];
            for(int i=0; i<vertexNum; i++){
                int[] intArray = Arrays.stream(bf.readLine().split(" "))
                    .mapToInt(Integer::parseInt).toArray();
                for(int j=0; j<intArray.length; j++){
                    graph[i][j] = intArray[j];
                }
            }
        } catch (IOException e) {
            System.out.println("IOException occured");
            System.exit(0);
        }
    }

    private final static void fw() {        
	    for(int k=0; k<vertexNum; k++) {
	        for(int i=0; i<vertexNum; i++) {
	            for(int j=0; j<vertexNum; j++) {
	                if(graph[i][j] > graph[i][k] + graph[k][j])
                        graph[i][j] = graph[i][k] + graph[k][j];
	            }
	        }
	    }
    }

    public final static void main(String[] args) {
        readInput();
        fw();
    }
}