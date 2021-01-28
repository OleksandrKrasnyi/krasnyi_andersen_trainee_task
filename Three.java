public class Three {

	public static void main(String[] args) {
		
		int[] numArray = {3, 9, 10, 42, 55, 66, 77, 99, 122};
		
		for (int i = 0; i < numArray.length; i++) {
			if (numArray[i] % 3 == 0) {
				System.out.println(numArray[i]);
			}
		}
	}
}
