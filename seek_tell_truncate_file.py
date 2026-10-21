#with open("main.txt", 'r') as f:
# print(type(f))
# move to the 10 byte in the file
# f.seek(10)

 #read the next 5 byte
# print(f.tell())
# data = f.read(5)
# print(data)

 #truncate methode
with open("main1.txt",'w') as f1:
 f1.write("hello Arjun")
 f1.truncate(3) # only 3 characters are print in the output like hel

with open("main1.txt", 'r') as f1:
  print(f1.read()) 
