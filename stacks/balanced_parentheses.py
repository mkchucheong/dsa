def balance_checker(s):
    par_stack = []

    closing = {}
    closing[")"] = "("
    closing["}"] = "{"
    closing["]"] = "["

    openers = set(["(", "{", "["])

    for c in s:
        if c in openers:
            par_stack.append(c)
        
        elif c in closing:
            if par_stack[-1] == closing[c]:
                par_stack.pop()
            else:
                return False
    
    return True

if __name__ == "__main__":
    s1 = "(hi)th[[e]]re m[a(t)t]"
    s2 = "([hi(the[re]))] m[a(t)t]"
    s3 = ""

    print(balance_checker(s1))
    print(balance_checker(s2))
    print(balance_checker(s3))
