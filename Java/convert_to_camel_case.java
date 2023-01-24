class Solution{
  static String toCamelCase(String s){
    /*
    https://www.codewars.com/kata/517abf86da9663f1d2000003/java
    
    given string s, convert dash and underscored delimited words into camel case
    */
    String rtnstring = "";
    for (int i = 0; i < s.length(); i++){
        if (!Character.isAlphabetic(s.charAt(i))){
            rtnstring += (Character.toUpperCase(s.charAt(i+1)));
            i++;
        }else{
            rtnstring += s.charAt(i);
        }
    }
    return rtnstring;
  }
}