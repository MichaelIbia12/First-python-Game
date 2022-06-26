fc = 0 
 
f = [3,6]
c = f[1]

t = 0    

while t < 5:
 fc += 1
 t += 1
 if fc > c: 
   fc = 0   
 if f[0] < f[1]:
    print("FrameDrop")
    c = f[1] - f[0]
    
 else:
    print("Increased Frame")
 print(str(fc) + " fc")
 print(c)