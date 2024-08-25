import os

# Get latest Python script from repo.
os.system('git remote add origin https://github.com/4ndyOMG/TrackHackInfra.git')
os.system('git pull origin main')

# Create a file
f = open("demofile1.txt", "a")
f.write("IOCs to follow.")
f.close()

# Push output of script to CURRENT repo branch.
os.system('git remote add origin https://github.com/4ndyOMG/TrackHackInfra-Output.git')
os.system('git add .')
os.system('git commit -m "commit to public repo"')
os.system('git push origin main')


# Notes from google
# change branch and commit only output

#You have to create the branch as usual:
#git checkout -b TheBranchToUse
#Afterwards you need to make it public to others:
#git push -u origin TheBranchToUse

# add new remote repo
#os.system('git remote add origin https://github.com/4ndyOMG/TrackHackInfra-Output.git)'