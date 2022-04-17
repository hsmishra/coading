class CheckParen:
    def if_balenece(self, sequence: str):
        stack = []
        opening_br = set('([{')
        closing_br = set(')]}')
        pair = {')': '(', ']': '[', '}': '{'}
        for i in sequence:
            if i in opening_br:
                stack.append(i)
            if i in closing_br:
                if not stack:
                    return "Balance"
                elif stack.pop() != pair[i]:
                    return "Unbalance"
                else:
                    continue
        if not stack:
            return "Balance"
        else:
            return "Unbalance"


sequence = '{{[({})]}}'

paren = CheckParen()
result = paren.if_balenece(sequence)
print(result)