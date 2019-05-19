import os, sys
command = 'objdump -M intel -d ' + sys.argv[1] + ' > ' + sys.argv[1] + '.asm'
print command
os.system(command)

command = 'hexdump -C ' + sys.argv[1] + ' > ' + sys.argv[1] + '.bytes'
print command
os.system(command)