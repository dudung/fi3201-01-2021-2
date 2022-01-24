import html
char1 = html.unescape('&#x25FB;')
char2 = html.unescape('&#x25FC;')

NIM = '10219098'
for x in NIM:
    n = int(x, 10)
    s = ''
    for i in range(n):
        s += char
        #s += char1
        #s += char2
    print(n, ':', s, sep='')