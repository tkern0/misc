# Turns 'num' into base 'b'
def base_n(num,b,chars="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and chars[0]) or (base_n(num // b, b, chars).lstrip(chars[0]) + chars[num % b])
# Adds numbers to letters
def add_letters(stri, amount = 1):
    b26 = ""
    # Converts each character to base 10 from base 36, subtracts 10 and converts into base 26
    for i in list(stri.lower()): b26 += base_n(int(i, 36) - 10, 26)
    alph = ""
    # Converts base 26 number to base 10, adds 'amount', converts to base 26, adds 10 to each character and converts each character to base 36
    for i in list(base_n(int(b26, 26) + amount, 26)): alph += base_n(int(i, 26) + 10, 36)
    return alph[-len(stri):]
# Returns 'True' if the password follows rules
def good_pwd(stri):
    row = True
    pairs = 0
    for i in range(len(stri)):
        if stri[i] in "iol": return False
        if i > 0:
            if stri[i] == stri[i - 1]: pairs += 1
        if i > 2:
            if stri[i - 3:i] in "abcdefghijklmnopqrstuvwxyz": row = False
            if stri[i - 2] == stri[i - 1] == stri[i]: return False
    if row: return False
    if pairs > 1: return True
# Tests known passwords to see if they have the expected outcome
def test_cases(file):
    tfile = open(file, "r")
    failures = []
    for case in tfile:
        results = case.split()
        if results[1].lower() == "false" and good_pwd(results[0]): failures.append(case.strip())
        if results[1].lower() == "true" and not good_pwd(results[0]): failures.append(case.strip())
    if failures: print("Faliures:", failures)
    else: print("No Failures")

current_pwd = "hepxcrrq"
while not good_pwd(current_pwd): current_pwd = add_letters(current_pwd)
print("First Password:", current_pwd)
current_pwd = add_letters(current_pwd)
while not good_pwd(current_pwd): current_pwd = add_letters(current_pwd)
print("Second Password", current_pwd)
