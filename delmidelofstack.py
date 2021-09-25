def delete(stack,k):
    if len(stack)==0 or k==0:
        return stack
    #bharosa karo apne function ki hypothesis pe ki ye mereko stack ka middle element delete kr ke sahi salamat stack
    #dega mereko blindly bharosa karo is baat p
    temp=stack[-1]
    stack.pop()
    delete(stack,k-1)
    stack.push(temp)
    return stack
        