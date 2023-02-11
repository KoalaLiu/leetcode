# 栈的使用
class Solution:
    def isValid(self, s: str) -> bool:
        symbol_map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = []

        for ch in s:
            if ch in symbol_map:    # 右括号
                mch = symbol_map[ch]
                if len(stack) <= 0:
                    return False

                top = stack.pop()
                if top != mch:
                    return False
            else:    # 左括号
                stack.append(ch)

        if len(stack) != 0:
            return False
        else:
            return True