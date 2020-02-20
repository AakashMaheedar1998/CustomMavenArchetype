import os



cmd1 = 'git init'
os.system(cmd1)
cmd2_2 ='git status'
os.system(cmd2_2)
cmd2 = 'git add .'
os.system(cmd2)

cmd3 = 'git commit -m "My first File"'
os.system(cmd3)
cmd4 = 'git remote add origin https://github.com/AakashMaheedar/Test'
os.system(cmd4)
os.system(cmd2_2)

cmd6 = 'git push -u origin master'
os.system(cmd6)
