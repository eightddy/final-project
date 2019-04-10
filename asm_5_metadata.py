import sys, os

def asm_meta_data(file_path, asm_code):

    #filesize
    meta_data = []
    statinfo = os.stat(file_path)
    fileSize = statinfo.st_size
    meta_data.append(fileSize)

    #StartAddress
    loc = 0
    for row in asm_code:
        loc += 1
    meta_data.append(loc)

    return meta_data

file_path = "samples/01IsoiSMh5gxyDYTl4CB.asm"
#file_path = "samples/01SuzwMJEIXsK7A8dQbl.asm"
with open(file_path) as f:
    byte_code = f.readlines()

print asm_meta_data(file_path, byte_code)