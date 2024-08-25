import os

# Get latest Python script from repo.
os.system('git pull origin main')

# Create a file
f = open("demofile6.txt", "a")
f.write("Now the file has more content!")
f.close()

# Push output of script to repo. 
os.system('git add .')
os.system('git commit -m "commit from within python file using !command"')
os.system('git push origin main')