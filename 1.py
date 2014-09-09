import string

def translate(encrypt):
    plain = ''
    for ch in encrypt:
        if ch >= 'a' and ch <= 'z':
            ch = chr(ord(ch) + 2)
            if ch > 'z':
                ch = chr(ord(ch) - ord('z') - 1 + ord('a'))
    
        plain += ch

    return plain

intab = ''
outtab = ''
for i in range(26):
    ch =  chr(ord('a') + i)
    intab += ch
    ch = chr(ord(ch) + 2)
    if ch > 'z':
        ch = chr(ord(ch) - ord('z') - 1 + ord('a'))
    outtab += ch

print intab, outtab
transtab = string.maketrans(intab, outtab)

encrypt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print translate(encrypt)
print encrypt.translate(transtab)

encrypt = 'map'
print translate(encrypt)
print encrypt.translate(transtab)
