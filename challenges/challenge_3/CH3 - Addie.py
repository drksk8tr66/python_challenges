intab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
outtab = "YPLTAVKREZGMSHUBXNCDIJFQOWypltavkrezgmshubxncdijfqow"
trantab = str.maketrans(intab, outtab)

with open('Secret Message_encrypted.txt', 'r') as f2:
    s = f2.read()

print(s.translate({ord(x): y for (x, y) in zip(outtab, intab)}))
# print(s.translate({ord(x): y for (x, y) in zip(intab, outtab)}))
