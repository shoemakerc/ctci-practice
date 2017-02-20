/*
URLify.java
*/

class URLify {
	public static String URLify(String input, int len) {
		char[] inputArray = input.toCharArray();

		for (int i = 0; i < len; i++) {
			if (inputArray[i] == ' ') {
				for (int j = i + 1; j < input.length() - 2; j++) {
					curr = 
					inputArray[j + 2] = inputArray[j];
				}
				inputArray[i] = '%';
				inputArray[i+1] = '2';
				inputArray[i+2] = '0';
			}
		}
		String result = new String(inputArray);
		return result;
	}

	public static void main(String[] args) {
		String in = "Hello World  ";
		int trueLen = 11;
		System.out.println(URLify(in, trueLen));
	}
}