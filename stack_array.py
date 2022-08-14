#return a list of all the operations needed to build target
def stack_array(target, n):
    stack = []
    for i in range(1, n + 1):
            stack.append('Push')
            if i not in target:
                stack.append('Pop')
            if i == target[-1]:
                break
    return stack
