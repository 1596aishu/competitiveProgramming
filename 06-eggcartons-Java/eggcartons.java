// # Write the function eggCartons(eggs) that takes 
// # a non-negative integer number of eggs, and returns 
// # the smallest integer number of cartons required to hold 
// # that many eggs, where a carton may hold up to 12 eggs

class eggcartons {
	public int fun_eggcartons(int eggs){
		int n;
		while(eggs>0){
			if(eggs<12) return 1;
			n = 1 + eggs/12;
		}
		return n;
	}
}