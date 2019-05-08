package garbus_hw3_2;
import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class garbus_hw3_2 {
    public static class IntStack
    {
        private List<Integer> data;
        
        // Constructor
        public IntStack()
        {
            this.data = new ArrayList<Integer>();
        }
        // Push x onto stack
        public void push(int x)
        {
            this.data.add(x);
        }
        
        // Remove and return the element on top of the stack
        public int pop()
        {
            if(data.size() == 0)
                throw new java.lang.RuntimeException("Stack is empty");
            int i = data.get(data.size()-1);
            data.remove(data.size()-1);
            return i;
        }
        
        // Get the top element
        public int top()
        {
            if(this.data.size() == 0)
                throw new java.lang.RuntimeException("Stack is empty");
            return this.data.get(this.data.size()-1);
        }
        
        // Return the current size of the stack
        public int size()
        {
            return this.data.size();
        }
    }
    
    public static class StringStack
    {
        private List<String> data;
        
        // Constructor
        public StringStack()
        {
            this.data = new ArrayList<String>();
        }
        // Push x onto stack
        public void push(String x)
        {
            this.data.add(x);
        }
        
        // Remove and return the element on top of the stack
        public String pop()
        {
            if(data.size() == 0)
                throw new java.lang.RuntimeException("Stack is empty");
            String s = data.get(data.size()-1);
            data.remove(data.size()-1);
            return s;
        }
        
        // Get the top element
        public String top()
        {
            if(this.data.size() == 0)
                throw new java.lang.RuntimeException("Stack is empty");
            return this.data.get(this.data.size()-1);
        }
        
        // Return the current size of the stack
        public int size()
        {
            return this.data.size();
        }
    }
    
    // Evaluate the input expression and return the solution
    static boolean evalExp(String exp)
    {
        String str = "";
        
        // Iterate through string and values
        for(int i = 0; i < exp.length(); i++)
        {
            char c = exp.charAt(i);
            
            // Construct string
            if(c != ' ')
                str += c;
            
            // Complete string if a space or end of loop is reached
            if(c == ' ' || i == exp.length()-1)
            {
                if(isNumber(str)) // Integer
                {
                    valStk.push(Integer.parseInt(str));
                    str = "";
                }
                else // Operator
                {
                    repeatOps(str);
                    opStk.push(str);
                    str = "";
                }
            }
        }
        repeatOps("$");
        return result;
    }
    
    // Check if input string is a number
    static boolean isNumber(String s)
    {
        for(int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);
            if(c < '0' || c > '9')
                return false;
        }
        return true;
    }
    
    // Returns the precidence order of the reference operator
    static int prec(String refOp)
    {
        switch(refOp)
        {
            case "$":
                return -1;
            case "<=":
            case ">=":
            case "<":
            case ">":
            case "=":
                return 0;
            case "+":
            case "-":
                return 1;
            case "*":
            case "/":
                return 2;
        }
        throw new RuntimeException("Invalid input");
    }
    
    // Perform operations by precedence
    static void repeatOps(String refOp)
    {
        while(valStk.size() > 1 && prec(refOp) <= prec(opStk.top()))
            doOp();
    }
    
    // Perform an arithmetic operation
    static void doOp()
    {
        int x = valStk.pop();
        int y = valStk.pop();
        String op = opStk.pop();
        switch(op)
        {
            case "+":
                valStk.push(y+x);
                break;
            case "-":
                valStk.push(y-x);
                break;
            case "*":
                valStk.push(y*x);
                break;
            case "/":
                valStk.push(y/x);
                break;
            case ">":
                if(y>x)
                    result = true;
                break;
            case "<":
                if(y<x)
                    result = true;
                break;
            case ">=":
                if(y>=x)
                    result = true;
                break;
            case "<=":
                if(y<=x)
                    result = true;
                break;
            case "=":
                if(y==x)
                    result = true;
                break;
        }
    }
    
    // Static variables
    static StringStack opStk = new StringStack();
    static IntStack valStk = new IntStack();
    static boolean result = false;
    
    public static void main(String[] args) {
        // Establish variables
        Scanner in = new Scanner(System.in);
        String expression;
        
        // Ask user for input
        System.out.println("Input an expression (put spaces between integers and operators): ");
        expression = in.nextLine();
        
        // Print output
        System.out.println(evalExp(expression));
    }
}