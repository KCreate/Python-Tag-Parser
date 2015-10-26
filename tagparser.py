import string
import sys
def parsetag(t, s):
    x = s
    r = []
    while s!="" and s.find(t)!=-1:
        x=s[len(t)+s.find(t):]
        x=x[:x.find(t)]
        if x.isspace()!=1:r.append(x)
        s = s[s.find(t+x+t)+len(t+x+t):] if t in s[len(t+x+t):] else ""
    return r
print(p(sys.argv[1], sys.argv[2]))
