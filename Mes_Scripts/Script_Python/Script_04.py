str1="Salut tout le monde"
print(str1[3])
print(str1[0])
print(str1[-1])
print(str1[-2])
print(len(str1))
print(str1[len(str1)-1])
#Decoupage de chaine de caractere
print(str1[0:4])
print(str1[6:10])
print(str1[0:])
str2="sabacada"
print(str2[1::2])
print(str1[1::3])
print(str1[:7])
print(str1[-4:])
print(str1[::-1])
str3="boudjadi"
str4="abdelsalem"
str5=str3+" "+str4
print(str5)
str2=str2+str2
print(str2)
for i in str2:
    print(i)
    for i in enumerate(str2):
        print(i)