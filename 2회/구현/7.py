s = input()

length = len(s)
if sum(list(map(int, s[:length//2]))) == sum(list(map(int, s[length//2:]))):
    print('LUCKY')
else:
    print('READY')
