#5
leiviskät=float(input("anna leiviskät:"))
naulat=float(input("anna naulat:"))
luodit=float(input("anna luodit:"))
luoditkg=(0.0133*luodit)
naulatkg=(0.0133*32*naulat)
leiviskätkg=(32*0.0133*20*leiviskät)

print("Massa nykymittojen mukaan kilogrammoina:")
print(luoditkg+naulatkg+leiviskätkg)