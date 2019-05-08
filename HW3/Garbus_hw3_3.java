package Garbus_hw3_3;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Garbus_hw3_3 {
    
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
    }
    
    // Reads in a postfix expression and returns the result
    static int CalculatePostfix(String exp)
    {
        for(int i = 0; i < exp.length(); i++)
        {
            char c = exp.charAt(i);
            if(c < '0' || c > '9') // operator
                valStk.push(doOp(c));
            else // digit
              valStk.push(c - '0');
        }
        
        return valStk.pop();
    }
    
    // Perform operation and return result
    static int doOp(char op)
    {
        // Pop variables
        int x = valStk.pop();
        int y = valStk.pop();
        
        // Perform operation
        switch(op)
        {
            case '+':
                return y+x;
            case '-':
                return y-x;
            case '*':
                return y*x;
            case '/':
                return y/x;
            default:
                throw new RuntimeException("Not an arithmetic operation.");
        }
    }
    
    // Establish stacks
    static IntStack valStk = new IntStack();
        
    public static void main(String[] args) {
        // Establish variables
        Scanner in = new Scanner(System.in);
        String expression;
        
        // Ask user for input
        System.out.println("Input an expression in postfix notation (single digits only): ");
        expression = in.nextLine();
        
        // Calculate output
        System.out.println(CalculatePostfix(expression));
    }
}
