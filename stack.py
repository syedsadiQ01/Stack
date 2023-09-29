class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} into stack")

    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop()
            print(f"Popped {popped_item} from the stack")
            return popped_item
        else:
            print("Stack is empty, can't pop ")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty.")
    def size(self):
        return len(self.items)
    def display(self):
        if not self.is_empty():
            print("Elements present in the satck:")
            for item in reversed(self.items):
                print(item)
        else:
            print("Stack is empty. Nothing to display.")



if __name__ == "__main__":
    stack = Stack()
    print("Return true if stack is empty else return false :-",stack.is_empty())
    stack.pop()
    stack.push(3)
    stack.push(1)
    stack.push(5)
    stack.push(9)
    stack.push(11)
    print("")
    stack.display()
    print("Return true if stack is empty else return false :-",stack.is_empty())
    print("size of the stack:", stack.size())
    top_element = stack.peek()
    print(f"Top of the stack: {top_element}")

    popped_item = stack.pop()
    print(f"Popped item: {popped_item}")
    popped_item = stack.pop()
    print(f"Popped item: {popped_item}")

    stack.display()
    top_element = stack.peek()
    print(f"Top of the stack: {top_element}")
    print("size of the stack:", stack.size())