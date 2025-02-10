import re
 
def solve(q):
    try:
        n = next(i for i in q if i.isalpha())  # Check if q has alphabetic characters
    except StopIteration:
        # Use eval to evaluate the parsed string
        # Use sub to replace strings with regular expressions
        # In the regular expression, ab+ will match 'a' followed by any non-zero number of 'b's
        # [abv] is a set of characters, which will match 'a', 'b', or 'v'
        # ^[0-9] means "any digit, at the start of the string"; [^0-9] means "anything except a digit"
        return q if eval(re.sub(r'(^|[^0-9])0+([1-9]+)', r'\1\2', q)) else False
    else:
        for i in (str(i) for i in range(10) if str(i) not in q):
            r = solve(q.replace(n, str(i)))  # Replace character with number
            if r:
                return r
        return False
 
# Driver code
if __name__ == "__main__":
    query = "TO + GO == OUT"
    r = solve(query)
    print(r) if r else print("No solution found.")
