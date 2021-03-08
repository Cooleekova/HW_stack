from collections import deque


class Stack(deque):

    def is_empty(self):
        if len(self) > 0:
            return False
        else:
            return True

    def push(self, x):
        return self.appendleft(x)

    def _pop(self):
        return self.popleft()

    def peek(self):
        return self[0]

    def size(self):
        return len(self)

    def par_check(self, x):
        count = 0
        balanced = True
        while count < len(x):
            if x[count] == '(' or x[count] == '[' or x[count] == '{':
                self.push(x[count])
            else:
                if self.is_empty():
                    balanced = False
                else:
                    if x[count] == ')' and self.peek() == '(':
                        self._pop()
                    elif x[count] == ']' and self.peek() == '[':
                        self._pop()
                    elif x[count] == '}' and self.peek() == '{':
                        self._pop()
            count += 1
        if self.is_empty() and balanced:
            return 'Сбалансированно'
        else:
            return 'Не сбалансированно'


stack = Stack()


