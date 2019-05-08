package garbus_hw3;
import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class Garbus_HW3 {
    
    static class MinStack
    {
        private List<Integer> data;
        private List<Integer> min;
        
        // Constructor
        public MinStack()
        {
            this.data = new ArrayList<Integer>();
            this.min = new ArrayList<Integer>();
        }
        
        // Push x onto stack
        public void push(int x)
        {
            this.data.add(x);
            if(this.min.size() == 0 || x < this.min.get(this.min.size()-1))
                this.min.add(x);
        }
        
        // Remove and return the element on top of the stack
        public int pop()
        {
            if(this.data.size() == 0)
                throw new java.lang.RuntimeException("Stack is empty");
            if(this.data.get(this.data.size()-1) == this.min.get(this.min.size()-1))
                this.min.remove(this.min.size()-1);
            int i = this.data.get(this.data.size()-1);
            this.data.remove(this.data.size()-1);
            return i;
        }
        
        // Get the top element
        public int top()
        {
            if(this.data.size() == 0)
                throw new java.lang.RuntimeException("Stack is empty");
            return this.data.get(this.data.size()-1);
        }
        
        // Return the minimum element of the stack
        public int getMin()
        {
            if(this.min.size() == 0)
                throw new java.lang.RuntimeException("Stack is empty");
            return this.min.get(this.min.size()-1);
        }
    }
    
    public static void main(String[] args) {
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        System.out.println(minStack.getMin());
        System.out.println(minStack.pop());
        System.out.println(minStack.top());
        System.out.println(minStack.getMin());
    }
    
}
