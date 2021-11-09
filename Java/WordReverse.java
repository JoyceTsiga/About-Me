import java.util.Scanner;

public class TsigaWordReverse{
    public static void main(String[] args){
        reverseWord("word");   
        reverseWord("uhh");   
        reverseWord("cat");   
        reverseWord("dog");
        reverseWord("regret");      
    }

    private static void reverseWord(String s){
        //print out w, o, r,d 
        //String word = ui.nextLine();
        //for(int i = 0; i<s.length(); i++){ 
            //System.out.println(s.substring(i)); 
        //}
        String output="";
        for(int i = (s.length()-1); i>=0; i--){ 
            output+=s.substring(i,i+1); 

        }
        System.out.println(output);
    }
}
