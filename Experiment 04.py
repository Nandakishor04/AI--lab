import itertools

def solve():
    letters = 'SENDMORY'
    digits = '0123456789'

    # All possible permutations of digits assigned to letters
    for perm in itertools.permutations(digits, len(letters)):
        assign = dict(zip(letters, perm))
        
        # Leading letters can't be zero
        if assign['S'] == '0' or assign['M'] == '0':
            continue

        # Convert words to numbers
        send = int(assign['S'] + assign['E'] + assign['N'] + assign['D'])
        more = int(assign['M'] + assign['O'] + assign['R'] + assign['E'])
        money = int(assign['M'] + assign['O'] + assign['N'] + assign['E'] + assign['Y'])

        if send + more == money:
            print("Solution found!")
            print(f"SEND = {send}")
            print(f"MORE = {more}")
            print(f"MONEY = {money}")
            return

    print("No solution found.")

solve()
