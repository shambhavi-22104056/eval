def func(s):
    swapped=""
    for char in s:
        if char==',':
            swapped+='.'
        elif char=='.':
            swapped+=','
        else:
            swapped+=char
    return swapped

def transform(s,n):
    transformed = ""
    for i in range(len(s)):
        if i < n :
            transformed+=s[i].lower()
        else:
            transformed+=s[i].upper()
    return transformed   
input="Yes, Real time monitoring, Immediate alerts."
n=6
swapped_str=func(input)
output=transform(swapped_str,n)
print(output)
