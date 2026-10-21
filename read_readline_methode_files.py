#file = open("myfile1.txt", 'r')
#i = 0
#while  True:
   #i = i+1
   #line =file.readline()
   #print(line)
  # if not line:
   # break   
   
   #m1 = line.split(",")[0]
   #m2 = line.split(",")[1]
   #m3 = line.split(",")[2]
   #print(f"marks of math is :{i}")
   #print(f"marks of english is:{i}")
   #print(f"marks of ssl is :{i}")
   #print(line)
file2 = open("myfile2.txt",'w')
lines = ['line1\n', 'line2\n', 'line3\n']
file2.writelines(lines)
file2.close()