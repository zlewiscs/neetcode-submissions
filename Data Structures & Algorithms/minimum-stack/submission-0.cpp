class MinStack {
public:
    std::stack<int> stk;
    std::stack<int> min_stack;

    MinStack() {
        
    }
    
    void push(int val) {
        stk.push(val);
        if (min_stack.empty() || val < min_stack.top()) {
            min_stack.push(val);
        } else {
            min_stack.push(min_stack.top());
        }
    }
    
    void pop() {
        stk.pop();
        min_stack.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return min_stack.top();
    }
};
