// Definition for a pair
// class Pair {
//     int key;
//     String value;
//
//     Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
public class Solution {
    public List<List<Pair>> insertionSort(List<Pair> pairs) {
        ArrayList<List<Pair>> result = new ArrayList();
        if (pairs.isEmpty()) {
            return new ArrayList();
        }

        result.add(new ArrayList(pairs));
        for (int i = 1; i < pairs.size(); i++) {
            int j = i - 1;
            Pair key = pairs.get(i);
            while (j >= 0 && pairs.get(j).key > key.key) {
                pairs.set(j + 1, pairs.get(j));
                j -= 1;
            }
            pairs.set(j + 1, key);

            result.add(new ArrayList(pairs));
        }

        return result;
    }
}
