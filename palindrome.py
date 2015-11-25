# Take a positive number and return the number of special steps needed to obtain a palindrome.
# If a number is not a palindrome, then add it to the original and keep doing this until a palindrome is returned.
# Example: 87 + 78 = 165; 165 + 561 = 726; 726 + 627 = 1353; 1353 + 3531 = 4884; total is 4 steps to get palindrome

def palindrome_chain_length(n):
    counter = 0

    # check if palindrome
    while str(n) != str(n)[::-1]:

        # while not palindrome, add 1 to count and create new special n
        n = str(int(n) + int(n[::-1]))
        counter += 1
    return counter
            
