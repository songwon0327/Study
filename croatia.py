inputStr = input()
croatia = ["c=", "c-", "dz=","d-","lj","nj","s=","z="]

for i in range(len(croatia)):
   inputStr = inputStr.replace(croatia[i],"#")

print(len(inputStr))    
    