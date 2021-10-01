import java.util.*;
public class SingleNumber {

	public static int singleNumber(int[] a) {
		ArrayList<Integer> al = new ArrayList<Integer>(); 
		
		for(int i=0; i<a.length; i++) {
			if(al.contains(a[i])) {
				int index = al.indexOf(a[i]);
				al.remove(index);
			}			
			else {
				al.add(a[i]);
			}				
		}
		return al.remove(0);
		
	}
	
	public static void main(String[] args) {
		int[] a = {1};
		System.out.println(singleNumber(a));
	}
}
