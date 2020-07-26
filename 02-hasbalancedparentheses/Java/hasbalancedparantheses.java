// # Write the function hasBalancedParentheses, which takes a string and returns True 
// # if that code has balanced parentheses and False otherwise (ignoring all 
// # 	non-parentheses in the string). We say that parentheses are balanced if each 
// # right parenthesis closes (matches) an open (unmatched) left parenthesis, 
// # and no left parentheses are left unclosed (unmatched) at the end of the text. 
// # So, for example, "( ( ( ) ( ) ) ( ) )" is balanced, but "( ) )" is not balanced, and "( ) ) (" 
// # is also not balanced. Hint: keep track of how many right parentheses remain unmatched as 
// # you iterate over the string.

 
class hasbalancedparantheses {
	public boolean fun_hasbalancedparantheses(String s){
		// return false;
		int c1 = 0;
		int c2 = 0;	
		for (char ch: s.toCharArray()) {
			if (ch=='(')
				c1+=1;
			else if (ch==')')
				c2+=1;
		}
		System.out.println(c1+" "+c2);
		if (c1 == c2)
			return true;
		return false;
	}
	public static void main(String[] args) {
		hasbalancedparantheses s = new hasbalancedparantheses();
		boolean x = s.fun_hasbalancedparantheses("( ( ( ( )3))  ");
	}
}
	