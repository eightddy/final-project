import feature_extraction as fe
import sys
from numba.decorators import autojit
import numpy as np
import os, gzip
import hickle


file_path = "samples/01IsoiSMh5gxyDYTl4CB.asm"
#file_path = "samples/0QIZ6hemJLErWdFlGnCc.bytes"
#file_path = "samples/test/ITSUPtCmh7WdJcsYDwQ5.asm"
# doc tung dong cua file .bytes	
with open(file_path) as f:
    byte_code = f.readlines()
#file  = open(file_path, "r")


# print fe.byte_1gram(byte_code)
# print fe.byte_make_image(byte_code)
# print fe.byte_image1(byte_code)
# print fe.byte_image2(byte_code)



#print fe.asm_data_define(byte_code)


#print fe.asm_meta_data(file_path, byte_code)
#print fe.asm_symbols(byte_code)
#print fe.asm_opcodes(byte_code)
#print fe.asm_registers(byte_code)

#path = DATASET_PATH
#os.chdir(path)
#defined_apis = io.read_all_lines(APIS_PATH)
#with open('APIs.txt') as f:
#    defined_apis = f.readlines()
#defined_apis = defined_apis[0].split(',')
#print fe.asm_APIs(byte_code, defined_apis)
print fe.asm_sections(byte_code)
#print fe.asm_data_define(byte_code)

sys.exit()












