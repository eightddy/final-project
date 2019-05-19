
import os, gzip, re, sys

# byte_1gram: doc file tung byte mot
# params: tung dong cua file
# returns: mang tuan suat xuat hien cua 1 bytes trong file
def byte_1gram(byte_code):
    # khai bao 1 mang gom 16^2 phan tu de luu so lan xuat hien cua 0x00->0xFF
    # khoi tao gia tri bang 0
    OneByte = [0]*16**2 

    for row in byte_code:
        codes = row.split()[1:]
        # doc tung byte cua moi dong
        OneByteCode = []
        for i in codes:
            if i != '??':
                # chuyen hex -> decimal
                OneByteCode += [int(i,16)]

        #print(OneByteCode)
        # Tinh toan tan suat cua tung byte
        for i in OneByteCode:
            OneByte[i] += 1
        #print (OneByte)
    return OneByte
# --------------------------------------------------------------------------------------------


# doc kich thuoc file va dia chi bat dau tren bo nho
# params:
# returns: mang chua thong tin meta
def byte_meta_data(file_path, file):
    #kich thuoc file
    meta_data = []
    statinfo = os.stat(file_path)
    fileSize = statinfo.st_size
    #print(fileSize)
    meta_data.append(fileSize)

    #dia chi bat dau
    firstLine = file.readline().split()
    offset = firstLine[0]
    #print(offset)
    dec = int(offset, 16)
    meta_data.append(dec)

    return meta_data

# --------------------------------------------------------------------------------------------


from math import log
import numpy as np
from PIL import Image

def byte_make_image(byte_code):
    img_array=[]
    for row in byte_code:
        xx=row.split()
        if len(xx)!=17:
            continue
	# doi ve decimal
        img_array.append([int(i,16) if i!='??' else 0 for i in xx[1:] ])
    img_array = np.array(img_array)
    #print img_array
    if img_array.shape[1]!=16:
        assert(False)
    b=int((img_array.shape[0]*16)**(0.5))    
    b=2**(int(log(b)/log(2))+1)
    #print img_array.shape[0]*16
    a=int(img_array.shape[0]*16/b)
    print a, b
    print img_array.shape, img_array
    img_array=img_array[:a*b/16,:]
    print "x:",img_array[:a*b/16,:].shape, img_array[:a*b/16,:]
    img_array=np.reshape(img_array,(a,b))
    print img_array.shape, img_array
    img_array = np.uint8(img_array)
    im = Image.fromarray(img_array)
    im.show()
    # sys.exit()
    return img_array
# --------------------------------------------------------------------------------------------

# doc img tu mahotas
# params: mang cua dong byte code
# returns: 
# refers: https://mahotas.readthedocs.io/en/latest/api.html
import mahotas
import mahotas.features

def byte_image1(byte_code):
    img_feat = []
    img = byte_make_image(byte_code)
    #img = mahotas.imread(img.im)
    features = mahotas.features.haralick(img)
    #print features
    for i in range(len(features)):
        for j in range(len(features[0])):
            img_feat.append(features[i][j])
    return img_feat
# --------------------------------------------------------------------------------------------

from mahotas.features.lbp import lbp

def byte_image2(byte_code):
    img = byte_make_image(byte_code)
    #spoints = lbp(img,10,10,ignore_zeros=False)
    spoints = mahotas.features.lbp(img,10,10,ignore_zeros=False)
    #print spoints
    return spoints.tolist()
# --------------------------------------------------------------------------------------------

import strings

def byte_string_lengths(file_name):
    strs_len = strings.extract_length([strings.get_strings(file_name)])
    #print strs_len
    return strs_len[0].tolist()
    #pass
# --------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------
# |			ASM - FEATURES							      |
# --------------------------------------------------------------------------------------------

# 
# params: file_path, asm_code
# returns: kich thuoc file, so dong
def asm_meta_data(file_path, asm_code):

    #kich thuoc
    meta_data = []
    statinfo = os.stat(file_path)
    fileSize = statinfo.st_size
    meta_data.append(fileSize)

    #so dong
    loc = 0
    for row in asm_code:
        loc += 1
    meta_data.append(loc)

    return meta_data

#
# params: asm_code
# returns: dem so lan xuat hien cua symbol
def asm_symbols(asm_code):
    symbols = [0]*7
    for row in asm_code:
        if '*' in row:
            symbols[0] += 1
        if '-' in row:
            symbols[1] += 1
        if '+' in row:
            symbols[2] += 1
        if '[' in row:
            symbols[3] += 1
        if ']' in row:
            symbols[4] += 1
        if '@' in row:
            symbols[5] += 1
        if '?' in row:
            symbols[6] += 1

    return symbols

#
# params: asm_code
# returns: so lan xua hien cua thanh ghi
def asm_registers(asm_code):
    registers = ['edx','esi','es','fs','ds','ss','gs','cs','ah','al',
                 'ax','bh','bl','bx','ch','cl','cx','dh','dl','dx',
                 'eax','ebp','ebx','ecx','edi','esp']
    # khoi tao mang voi gia tri 0
    registers_values = [0]*len(registers)
    for row in asm_code:
	# loai bo cac ki tu phu
        parts = row.replace(',',' ').replace('+',' ').replace('*',' ').replace('[',' ').replace(']',' ') \
                    .replace('-',' ').split()
        for register in registers:
            registers_values[registers.index(register)] += parts.count(register)
    return registers_values

#
# params: asm_code
# returns: so lan xua hien cua 93 opcodes
def asm_opcodes(asm_code):
    opcodes = ['add','al','bt','call','cdq','cld','cli','cmc','cmp','const','cwd','daa','db'
                ,'dd','dec','dw','endp','ends','faddp','fchs','fdiv','fdivp','fdivr','fild'
                ,'fistp','fld','fstcw','fstcwimul','fstp','fword','fxch','imul','in','inc'
                ,'ins','int','jb','je','jg','jge','jl','jmp','jnb','jno','jnz','jo','jz'
                ,'lea','loope','mov','movzx','mul','near','neg','not','or','out','outs'
                ,'pop','popf','proc','push','pushf','rcl','rcr','rdtsc','rep','ret','retn'
                ,'rol','ror','sal','sar','sbb','scas','setb','setle','setnle','setnz'
                ,'setz','shl','shld','shr','sidt','stc','std','sti','stos','sub','test'
                ,'wait','xchg','xor']
    #print len(opcodes)
    opcodes_values = [0]*len(opcodes)
    for row in asm_code:
        parts = row.split()
        for opcode in opcodes:
            if opcode in parts:
                opcodes_values[opcodes.index(opcode)] += 1
                break
    return opcodes_values

#
# params: asm_code, apis
# returns: dem so lan xuat hien cua cac api
def asm_APIs(asm_code, apis):
    apis_values = [0]*len(apis)
    for row in asm_code:
        for i in range(len(apis)):
            if apis[i] in row:
                apis_values[i] += 1
                break
    return apis_values

#
# params: asm_code
# returns: xem chi tiet trong bao cao
def asm_sections(asm_code):
    section_names = []
    # dem tat ca section co trong file asm
    for row in asm_code:
        section_name = [row[0:np.core.defchararray.index(row, ':')]]
	#print section_name, np.core.defchararray.index(row, ':')
	#sys.exit()
        if section_name != 'HEADER':
            section_names += section_name
    #print section_names

    known_sections = ['.text', '.data', '.bss', '.rdata', '.edata', '.idata', '.rsrc', '.tls', '.reloc']
    sections_values = [0]*24 #24 features se return. Xem chi tiet trong bao
    unknown_sections = []
    unknown_lines = 0
    number_of_sections = len(section_names)

    # dem so lan xuat hien cua knowm_sections
    # them moi vao unknown_sections neu ko co trong known_section
    for section in section_names:
        if section in known_sections:
            section_index = known_sections.index(section)
            sections_values[section_index] += 1
        else:
            unknown_sections.append(section)
            unknown_lines += 1

    # dem so section doc duoc tu file
    uni_section_names_len = len(np.unique(section_names))
    uni_unknown_section_names_len = len(np.unique(unknown_sections))
    uni_known_section_names_len = 0
    # chi tiet 24 features xem trong bao cao
    for i in range(0,8):
        if sections_values[i] != 0:
            uni_known_section_names_len += 1

    sections_values[9] = uni_section_names_len
    sections_values[10] = uni_unknown_section_names_len
    sections_values[11] = unknown_lines

    for i in range(0,8):
        sections_values[i + 12] = float(sections_values[i])/ number_of_sections

    sections_values[21] = float(uni_known_section_names_len) / uni_section_names_len
    sections_values[22] = float(uni_unknown_section_names_len) / uni_section_names_len
    sections_values[23] = float(unknown_lines) / number_of_sections

    return sections_values#, section_names



def asm_misc(asm_code):

    keywords = ['Virtual','Offset','loc','Import','Imports','var','Forwarder','UINT','LONG','BOOL','WORD','BYTES','large','short','dd','db','dw','XREF','ptr','DATA','FUNCTION','extrn',
'byte','word','dword','char','DWORD','stdcall','arg','locret','asc','align','WinMain','unk','cookie','off','nullsub','DllEntryPoint','System32','dll','CHUNK','BASS','HMENU','DLL',
'LPWSTR','void','HRESULT','HDC','LRESULT','HANDLE','HWND','LPSTR','int','HLOCAL','FARPROC','ATOM','HMODULE','WPARAM','HGLOBAL','entry','rva','COLLAPSED','config','exe','Software',
'CurrentVersion','__imp_','INT_PTR','UINT_PTR','---Seperator',
'PCCTL_CONTEXT','__IMPORT_','INTERNET_STATUS_CALLBACK','.rdata:','.data:','.text:','case','installdir','market','microsoft','policies','proc','scrollwindow','search','trap',
'visualc','___security_cookie','assume','callvirtualalloc','exportedentry','hardware','hkey_current_user','hkey_local_machine','sp-analysisfailed','unableto']

    keywords_values = [0]*len(keywords)
    for row in asm_code:
        for i in range(len(keywords)):
            if keywords[i] in row:
                keywords_values[i] += 1 #parts.count(opcode)
                break
    return keywords_values




