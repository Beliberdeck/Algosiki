class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def empty(self):
        return not self.data


def is_balanced(s):
    match = {')': '(', ']': '[', '}': '{'}
    st = Stack()

    for ch in s:
        if ch in match.values():
            st.push(ch)
        elif ch in match:
            if st.empty() or st.top() != match[ch]:
                return False
            st.pop()

    return st.empty()


print('yes' if is_balanced(input().strip()) else 'no')