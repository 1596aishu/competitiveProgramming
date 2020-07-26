// # Write the function longestSubpalindrome(s), that takes a string s and returns 
// the longest palindrome that occurs as consecutive characters (not just letters, but 
// 	any characters) in s. So:
// #    	longestSubpalindrome("ab-4-be!!!") 
// # returns "b-4-b". If there is a tie, return the lexicographically larger value -- 
// in java, a string s1 is lexicographically greater than a string s2 if (s1 > s2). So:
// #    	longestSubpalindrome("abcbce") 
// # returns "cbc", since ("cbc" > "bcb"). Note that unlike the previous functions, 
// this function is case-sensitive (so "A" is not treated the same as "a" here). Also, 
// from the explanation above, we see that longestSubpalindrome("aba") is "aba", 
// and longestSubpalindrome("a") is "a".

class longestsubpalindromes {
	public String fun_longestsubpalindromes(String s){
		if(s==null || s.length() < 2) 
			return s;
        int l = 0;
        int h = 0;
        int max = 1;
        int len = s.length();
        boolean[][] dp = new boolean[len][len];
        for(int i=0; i<len; i++){
            dp[i][i] = true;
            for(int j=i-1; j>=0; j--){
                if(s.charAt(i) == s.charAt(j) && (dp[j+1][i-1] || j+1>i-1)){
                    dp[j][i] = true;
                    if(i-j+1 > max){
						l = j;
						h = i;
						max = i-j+1;
                    }
                }
            }
        }
		// System.out.println(l);
		// System.out.println(s.substring(h+1));

        return s.substring(l, h+1);
	}

	// public static void main(String[] args) {
	// 	longestsubpalindromes s = new longestsubpalindromes();
	// 	s.fun_longestsubpalindromes("abcbce");
	// }
}
