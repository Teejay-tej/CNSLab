#diffiehelman
p=int(input("Enter the prime number:"))
g=int(input("Enter the primitive root value:"))
a=int(input("Enter the private key of Alice:"))
b=int(input("Enter the private key of Bob:"))

x=int(pow(g,a,p))
y=int(pow(g,b,p))
ka=int(pow(y,a,p))
kb=int(pow(x,b,p))

print("the secret key for alice is :",ka)
print("the secret key for Bob is :",kb)