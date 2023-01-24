class XO {
  
    public static boolean getXO (String str) {
        /*
        https://www.codewars.com/kata/55908aad6620c066bc00002a/java

        given string str, check if same number of X and O
        */
        int X_count = 0;
        int O_count = 0;
        str = str.toUpperCase();
        for (int i = 0; i < str.length(); i ++){
            if (Character.compare(str.charAt(i), 'X') == 0){
                X_count += 1;
                System.out.print(X_count);
            } else if (Character.compare(str.charAt(i), 'O') == 0){            {
                O_count += 1; }
                System.out.print(O_count);
            }
        }
        return X_count == O_count;
    }
}