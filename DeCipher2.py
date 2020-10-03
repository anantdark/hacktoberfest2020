# codechef problem code = DC10005

def keys(key):
    table1 = {'A':'CGA', 'B':'CCA', 'C':'GTT', 'D':'TTG'
    , 'E':'GGC', 'F':'GGT', 'G':'TTT', 'H':'CGC'
    , 'I':'ATG', 'J':'AGT', 'K':'AAG', 'L':'GCT'
    , 'M':'TCC', 'N':'TCT', 'O':'GGA', 'P':'GTG'
    , 'Q':'AAC', 'R':'TCA', 'S':'ACG', 'T':'TTC'
    , 'U':'CTG', 'V':'CCT', 'W':'CCG', 'X':'CTA'
    , 'Y':'AAA', 'Z':'CTT', '0':'ACT', '1':'ACC'
    , '2':'TAG', '3':'GCA', '4':'GAG', '5':'AGA'
    , '6':'TTA', '7':'ACA', '8':'AGG', '9':'GCG'}    
    temp = []
    for i in key:
        temp.append(table1[i])
    temp = ''.join(_ for _ in temp)
    return temp

def dnas(binstr):
    i = 0
    temp = []
    while i< len(binstr):
        temp.append(binstr[i]+binstr[i+1])
        i+=2
    sub = {"00" : "A", "01" : "C", "10" : "G", "11" : "T"}
    for i in range(len(temp)):
        temp[i] = sub[temp[i]]
    dna = ''.join(i for i in temp)
    return(dna)

def encrypt(dna, keycode):
    table2 = {'AA':'C', 'GA':'T', 'CA':'G', 'TA':'A'
    , 'AG':'A', 'GG':'G', 'CG':'T', 'TG':'C'
    , 'AC':'T', 'GC':'A', 'CC':'G', 'TC':'C'
    , 'AT':'G', 'GT':'C', 'CT':'A', 'TT':'T'}
    final = []
    multiplier = (int(len(dna)/len(keycode))+1)
    keycode = keycode*multiplier
    for i in range(len(dna)):
        temp = str(dna[i]+keycode[i])
        final.append(table2[temp])
    final = ''.join(_ for _ in final)
    return(final)
    
if __name__ == "__main__":
    plain = input()
    key = input()
    string = '0'+'0'.join(format(ord(x), 'b') for x in plain)
    dna = dnas(string)
    keycode = keys(key)
    print(encrypt(dna, keycode))
