pt=input("Enter the plaintext:")
key=input("Enter the key:")
pt.lower()
key.lower()

pt=[ord(a)-97 for a in pt]
key=[ord(a)-97 for a in key]
i=0

while (len(key)!=len(pt)):
    key.append(key[i])
    i+=1
    if i==len(key):
        i=0

enc=[]
print("The encrypted text is:")
for i,j in zip(pt,key):
    res=(i+j)%26
    enc.append(res)
    print(chr(res+97),end=" ")
print()
print("The decrypted text is:")
for i,j in zip(enc,key):
    res=(i-j)%26
    if res<0:
        res+=26
    print(chr(res+97),end=" ")
print()