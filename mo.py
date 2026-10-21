import os
if ( os.path.exists("data")):
   os.mkdir("data")


for i in range(1,21):
   os.mkdir(f"data/Day{i}")