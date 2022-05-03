import pandas as pd

mot = {'L':1, 'A':2, 'ST':3}
pot = {'START':1, 'END':2, 'USING':3} #Assembly Directives
dl = {'DC':1, 'DS':2}

print(f'\nmot: {mot}\npot: {pot}\ndl: {dl}')

st = {}
lt = {}
intm = []

tokens = dict()
with open('exp3.asm', 'r') as f:
    for i,line in enumerate(f.readlines(),1):
        temp = line.strip('\n').split('\t')
        if temp[-1] == '**': continue
        for t in temp:
            if t != '': break
        else: continue
        if len(temp) < 3:
            for _ in range(3-len(temp)): temp.append('')
        tokens[i] = temp
# for i,token in tokens.items(): print(f"{i:{2}}: {token}")

lc = 0
line1 = list(tokens.values())[0]
lc_idx = line1.index('START')+1
if line1[lc_idx].isdigit(): lc = int(line1[lc_idx])
#print(lc)

st_c = 1
lt_c = 1
for i,t in tokens.items():
    if t[1] == 'END':
        #assign addresses to literals
        pass
    if t[0] != '': st[st_c] = [t[0].rstrip(':')]; st_c+=1
    if t[1] == 'START' and t[0].endswith(':'): st[st_c-1].append(lc)
    if t[1] in mot.keys(): lc+=1
    if t[1] == 'DC':
        st[st_c] = st.get(st_c-1).append(lc)
        lt[lt_c] = [int(t[2][2:len(t[2])-1]), lc]; lt_c+=1
        # lt[lt_c] = [t[2], lc]; lt_c+=1
        if t[2].isdigit(): lc+=1
        elif t[2][0] == 'F': lc+=4
        elif t[2][0] == 'H': lc+=2
        else: raise Exception(f"Invalid Number @line {i}")
    if t[1] == 'DS':
        st[st_c-1].append(lc)
        if t[2].isdigit(): lc+=int(t[2])
        elif t[2][t[2].index("'")+1] == 'F': lc+=4
        elif t[2][t[2].index("'")+1] == 'H': lc+=2
    #print(lc)
    temp = list(st.keys())
# for i in temp:
#     if len(st[i]) <2: del st[i]

print('\nPass1 Output:')
print(f"Symbol Table: {st}")
print(f"Literal Table: {lt}")

pass2_op = []
for i,l in tokens.items():
    temp = []
    if l[1] in mot.keys():
        temp.append(mot[l[1]])
        done = {0:False, 1:False}
        f = 0
        for sl in st.values():
            for c,op in enumerate(l[2].split(',')):
                if op == sl[0]: temp.append(sl[1]); done[c]=True; f=1; break
        for k in done.keys():
            if k != True: temp.append(int(l[2].split(',')[k]))
        #
        temp[1], temp[2] == temp[2], temp[1]
        #
        pass2_op.append(temp)
    elif l[1] == 'DC':
        s = l[2][2:len(l[2])-1]
        for c,_ in lt.values():
            l = ['-']*3
            if int(s) == c:
                l[1] = bin(c)[2:]
                pass2_op.append(l)
print('\n', 'Pass2 Output:', '\n', pd.DataFrame(pass2_op, columns=['opcode', 'op1', 'op2']).to_string(index=False))