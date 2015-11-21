import string

def rot13(message):
    alpha = string.ascii_lowercase
    beta = string.ascii_uppercase
    a = alpha[:len(alpha)/2] + beta[:len(beta)/2]
    b = alpha[(len(alpha)+1)/2:] + beta[(len(beta)+1)/2:]
    aStr = ''
    for char in message:
        if char in a:
            aStr += b[a.index(char)]
        elif char in b:
            aStr += a[b.index(char)]
        else:
            aStr += char
    return aStr

# clever solution...
def rot13_clever(message):
    return message.encode('rot13')
