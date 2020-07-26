
class nthtenlyprime {
	public int fun_nthtenlyprime(int n){
		// return 1;
		int i = 0;
		int j = 2;
		int sum = 0;
		while(i<n){
			while(i!=0) {
				sum += i%10;
				i = n/10;
			}
			if (sum == 10){
				i+=1;
			}
			j+=1;
		}
		
		return j-1;
	}

	// public static void main(String[] args) {
	// 	nthtenlyprime s = new nthtenlyprime();
	// 	int x = s.fun_nthtenlyprime(2);
	// 	System.out.println(x);
		
	// }
}
