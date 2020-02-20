import os
cmd = 'ls'
os.system(cmd)

cmd2 = 'git status'
os.system(cmd2)
cmd3 = 'git add .'
os.system(cmd3)
cmd4 = 'git commit -m "First commit"'
os.system(cmd4)
cmd5 = 'git status'
os.system(cmd5)
cmd6 = 'git remote add origin https://github.com/AakashMaheedar/Test'
os.system(cmd6)
cmd6 = 'git push -u origin master'
os.system(cmd6)
cmd6 = 'git status'
os.system(cmd6)