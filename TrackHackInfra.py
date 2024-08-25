import os

f = open("demofile3.txt", "a")
f.write("Now the file has more content!")
f.close()

os.system('git add .')
os.system('git commit -m "commit from within python file using !command"')