import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class FindDuplicates {

    public static List<Integer> findDuplicatesNestedLoops(List<Integer> l) {
        // Make a new list
        List<Integer> duplicates = new ArrayList<Integer>();        

        // Iterate through the given list
        for (int i = 0; i < l.size(); i++) {
            // For each number check the numbers after it for duplicates
            for (int j = i+1; j < l.size(); j++) {
                // Also check that we haven't already added the duplicate to the new list
                if (l.get(i).equals(l.get(j)) && !duplicates.contains(l.get(j))) {
                    // Add them to the new list
                    duplicates.add(l.get(i));
                }
            }
        }
        return duplicates;
    }

    public static void main(String[] args) {
        // some test strings:
        List<Integer> sample1 = new ArrayList<Integer>(Arrays.asList(3, 7, 5, 6, 7, 4, 8, 5, 7, 66));
        List<Integer> sample2 = new ArrayList<Integer>(Arrays.asList(3, 5, 6, 4, 4, 5, 66, 6, 7, 6));
        List<Integer> sample3 = new ArrayList<Integer>(Arrays.asList(3, 0, 5, 1, 0));
        List<Integer> sample4 = new ArrayList<Integer>(Arrays.asList(3));
        System.out.println("Sample 1: " + findDuplicatesNestedLoops(sample1));
        System.out.println("Sample 2: " + findDuplicatesNestedLoops(sample2));
        System.out.println("Sample 3: " + findDuplicatesNestedLoops(sample3));
        System.out.println("Sample 4: " + findDuplicatesNestedLoops(sample4));
    }

}
