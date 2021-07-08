strVal="fuck"
charArr= ["!","@","#","$","%","^","&","*","(",")"]
numArr= [1,2,3,4,5,6,7,8,9,0]
swearArr= ["fuck","shit","poes","tranny","chink","dyke","faggot","nigg","kike","kaffer","cunt","tief","moffie","whore","hoer","etter","fok","hotnot","naai"]
charCount=0
numCount=0
swearCount=0
upperCount=0
swear=""
for i in range(len(strVal)):
    for n in range(len(charArr)):
        if strVal[i]==charArr[n]:
                 charCount+=1
        for x in range(len(numArr)):
             if strVal[i]==numArr[n]:
                 numCount+=1
                 for y in range(len(numArr)):
                    swearLen = int(len(swearArr[y]))
                    if strVal[i:swearLen]==swearArr[y]:
                        swaer=swearArr[y]
                        swearCount+=1
                    if strVal[i].isupper():
                        upperCount+=1
                    
print(swear)
 
if charCount > 0:
    if numCount > 0:
        if upperCount > 0:
            if swearCount==0:
                 print("password eligible")
