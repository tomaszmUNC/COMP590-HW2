import math

f = open("out.dat", "rb")

data = f.read()
counts = [0]*256
framelen = 4096
totlen = 1228800


cnt = 0
for element in data:
    counts[int(element)] = counts[int(element)] + 1

    cnt = cnt+1

idx =0
#print(counts)
for count in counts:
    counts[idx] = (count/cnt)
    idx = idx+1
    

#counts.sort() 
#print(counts)

def entropy(counts):
    entropy = 0
    for count in counts:
        if count > 0:
           entropy = entropy -(count)*math.log(count, 2)
    print("Entropy: " + str(entropy))





idx = 0
cnt = 0
finaldata = []
compdat = [0]*(255+256)
firstframe = [0]*framelen
#print(data[0])
#print(firstframe[0])
for entry in data:
    firstframe.append(int(entry))
data = firstframe

for element in data:
    if idx + framelen < (totlen+framelen):
        
        ref = (int(data[idx+framelen]-int(element)))
        ref = ref+255
        compdat[ref] = compdat[ref] + 1
        finaldata.append(ref)
        cnt = cnt + 1
    idx = idx+1
   

idx = 0   
for element in compdat:
    compdat[idx] = (element/cnt)
    idx = idx+1
    

print("Original Source Model")
entropy(counts)
print(" ")
print("Temporal Coherance Model")
entropy(compdat)




#print(len(finaldata))


nf = open("myout.dat", "wb")
for entry in finaldata:
    if entry > 254:
        
       
        nf.write(bytes([255]))
        nf.write(bytes([entry-255]))
    else:
        nf.write(bytes([entry]))
                     

nf.close()

print(" ")
print("Encoding Completed")
