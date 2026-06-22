// Definition for a pair.
// class Pair {
//     public int key;
//     public String value;
//
//     public Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    public List<Pair> mergeSort(List<Pair> pairs) {
        if (pairs.isEmpty()) {
            return pairs;
        }

        if (pairs.size() == 1) {
            return pairs;
        }
        List<Pair> subPair1 = mergeSort(new ArrayList(pairs.subList(0, pairs.size() / 2)));
        List<Pair> subPair2 = mergeSort(new ArrayList(pairs.subList(pairs.size() / 2, pairs.size())));
        return merge(subPair1, subPair2);
    }

    private List<Pair> merge(List<Pair> subPair1, List<Pair> subPair2) {
        List<Pair> result = new ArrayList();

        int head1 = 0;
        int head2 = 0;

        while (head1 < subPair1.size() && head2 < subPair2.size()) {
            if (subPair1.get(head1).key <= subPair2.get(head2).key) {
                result.add(subPair1.get(head1));
                head1 += 1;
            } else {
                result.add(subPair2.get(head2));
                head2 += 1;
            }
        }

        if (!(head1 == subPair1.size())) {
            for (int i = head1; i < subPair1.size(); i ++) {
                result.add(subPair1.get(i));
            }

            return result;
        }

        if (!(head2 == subPair2.size())) {
            for (int i = head2; i < subPair2.size(); i ++) {
                result.add(subPair2.get(i));
            }

            return result;
        }

        return result;
    }
}
