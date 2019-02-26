f = open("myout.dat", "rb")

data = f.read()
counts = [0]*256
framelen = 4096
totlen = 1228800
#preframe = [0]*framelen
result = []
ref = 0

idx = 0
for entry in data:
    
    if int(entry) != 255:
        ref = ref + int(entry)
        if len(result) < framelen:
            result.append(ref-255)
            ref = 0
        else:
            res = result[idx-framelen] + (ref-255)
            result.append(res)
            ref = 0
        idx = idx+1
    else:
        ref = int(entry)
cnt = 0
for element in result:
    counts[element] = counts[element] + 1
    cnt = cnt+1



nf = open("finout.dat", "wb")
for entry in result:
    nf.write(bytes([entry]))
nf.close()

print("Decoding Completed")



    
