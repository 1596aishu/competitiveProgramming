// # largestNumber: Write the function largestNumber(text) that takes a string of text and 
// # returns the largest int value that occurs within that text, or 0 if no such value occurs. 
// # You may assume that the only numbers in the text are non-negative integers and 
// # that numbers are always composed of consecutive digits (without commas, for example). For example:
// #     	largestNumber("I saw 3 dogs, 17 cats, and 14 cows!")
// # returns 17 (the int value 17, not the string "17"). And
// #     	largestNumber("One person ate two hot dogs!")
// # returns None (the value None, not the string "None").


class largestnumber {
	public int fun_largestnumber(String s){
		// return 0;
		int high = 0;
		// Array lst = new Array[10];
		String numbers = "";		
		for(String w:s.split(" ")){
			String n = ".*[0-9].*";
			if (w.matches(n)){
				numbers=w.replaceAll("[^0-9]", " ");
				if(high < Integer.parseInt(numbers))
					high = 	Integer.parseInt(numbers);		
			}
			// if (numbers != "" || numbers != null){
			// 	high = Integer.parseInt(numbers);
			// 	System.out.println(high);
			// }
		}
		System.out.println(high);
		return 0;
	}
	public static void main(String[] args) {
		largestnumber s = new largestnumber();
		s.fun_largestnumber("we have 32 dogs 3 cats");
	}
	
}
	