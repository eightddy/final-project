import sys, os
import numpy as np

def asm_misc(asm_code):

    keywords = ['Virtual','Offset','loc','Import','Imports','var','Forwarder','UINT','LONG','BOOL','WORD','BYTES','large','short','dd','db','dw','XREF','ptr','DATA','FUNCTION','extrn','byte','word','dword','char','DWORD','stdcall','arg','locret','asc','align','WinMain','unk','cookie','off','nullsub','DllEntryPoint','System32','dll','CHUNK','BASS','HMENU','DLL','LPWSTR','void','HRESULT','HDC','LRESULT','HANDLE','HWND','LPSTR','int','HLOCAL','FARPROC','ATOM','HMODULE','WPARAM','HGLOBAL','entry','rva','COLLAPSED','config','exe','Software','CurrentVersion','__imp_','INT_PTR','UINT_PTR','---Seperator','PCCTL_CONTEXT','__IMPORT_','INTERNET_STATUS_CALLBACK','.rdata:','.data:','.text:','case','installdir','market','microsoft','policies','proc','scrollwindow','search','trap','visualc','___security_cookie','assume','callvirtualalloc','exportedentry','hardware','hkey_current_user','hkey_local_machine','sp-analysisfailed','unableto']

    keywords_values = [0]*len(keywords)
    for row in asm_code:
        parts = row.replace(',',' ').replace('+',' ').replace('*',' ').replace('[',' ').replace(']',' ') \
                   .replace('-',' ').split()
        for i in range(len(keywords)):
            if keywords[i] in row:
                keywords_values[i] += parts.count(keywords[i])
                # break
    return keywords_values

file_path = "samples/01IsoiSMh5gxyDYTl4CB.asm"
#file_path = "samples/01SuzwMJEIXsK7A8dQbl.asm"
with open(file_path) as f:
    byte_code = f.readlines()

print asm_misc(byte_code)