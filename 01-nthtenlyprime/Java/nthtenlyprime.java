
class nthtenlyprime {
	public boolean isprime(int n){
		for(int i=2;i<n;i++){
			if (n%i == 0){
				return false;
			}
		}
		return true;
	}
	public int fun_nthtenlyprime(int n){
		int count = -1; 
  
		for (int curr = 10;; curr++) { 
			if (isprime(curr) == true){
				// Find sum of digits in current no. 
				int sum = 0; 
				for (int x = curr; x > 0; x = x / 10) 
					sum = sum + x % 10; 
		
				// If sum is 10, we increment count 
				if (sum == 10) 
					count++; 
		
				// If count becomes n, we return current 
				// number. 
				if (count == n) {
					// System.out.println(curr);
					return curr; }
			}			
		} 
		// return -1; 

	}

	// public static void main(String[] args) {
	// 	nthtenlyprime s = new nthtenlyprime();
	// 	int x = s.fun_nthtenlyprime(1);
		
	// }
}
