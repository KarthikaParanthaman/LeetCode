import java.util.HashMap;

public class majorityElement {
	public static int findMajorityElement(int[] a) {
		// hashmap to store occurence
		HashMap<Integer,Integer> m = new HashMap<Integer, Integer>();
		
		// create hashmap with num-> no of occurence
		int count=1;
		for(int i = 0; i < a.length; i++) {
			if(m.containsKey(a[i])) {
				count = m.get(a[i]);
				m.put(a[i], count+1);
			} else {
				m.put(a[i], 1);
			}			
		}
		
		// get max occurence number
		int max = 0;
		int maxnum = 0;
		for(int i : m.keySet()) {
			if(m.get(i) > max) {
				maxnum = i;
				max = m.get(i);
			}				
		}
		
		
		return maxnum;
	}
	
	public static void main(String[] args) {
		int[] a = {1, 2, 3, 1, 1, 2, 1, 2};
		System.out.println(findMajorityElement(a));
	}
}
