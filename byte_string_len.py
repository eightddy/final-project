from handle_io import io

def asm_APIs(asm_code, apis):
    apis_values = [0]*len(apis)
    for row in asm_code:
        for i in range(len(apis)):
            if apis[i] in row:
                apis_values[i] += 1
                break
    return apis_values

file_path = "samples/01IsoiSMh5gxyDYTl4CB.asm"
# file_path = "samples/01SuzwMJEIXsK7A8dQbl.asm"
with open(file_path) as f:
    byte_code = f.readlines()

defined_apis = io.read_all_lines('APIs.txt')
defined_apis = defined_apis[0].split(',')

print asm_APIs(byte_code, defined_apis)