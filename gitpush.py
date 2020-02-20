import os
cmd0 ='cd /Users/aaakasha/Workstore/Feb/sampleApp'
os.system(cmd0)
cmd01 ='pwd'
os.system(cmd01)
cmd = 'ls'
os.system(cmd)
os.system(cmd01)
cmd1 = 'git init'
os.system(cmd1)

cmd2 = 'git status'
os.system(cmd2)
cmd3 = 'git add .'
os.system(cmd3)
cmd4 = 'git commit -m "First commit" '

os.system(cmd4)
cmd5 = 'git status'
os.system(cmd5)
cmd6 = 'git remote add origin https://github.com/AakashMaheedar/Test.git'
os.system(cmd6)
cmd6 = 'git push -u origin master'
os.system(cmd6)
cmd7 = 'git status'
os.system(cmd7)
