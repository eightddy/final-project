import sys, os
import numpy as np
from numba.decorators import jit, autojit
import hickle
import os, gzip

def binary_search(a, x):
    lo = 0
    hi = a.shape[0]
    while lo < hi:
        mid = (lo + hi) // 2
        midval = a[mid]
        if midval < x:
            lo = mid + 1
        elif midval > x:
            hi = mid
        else:
            return mid
    return -1

#binary_search_numba = autojit(binary_search, nopython=True)


def extract(all_elems_codes, out, askii_list):

    MAX_STR = out.shape[0]

    cur_num_str = 0

    i = all_elems_codes.shape[0] - 1
    state = 0

    cur_end = -1
    min_length = 4
    count_one = 0
    count_two = 0
    count_three = 0

    while i >= 1:
    
        if all_elems_codes[i] == 0:
            # print all_elems_codes[i:i+10]
            # sys.exit()
            if (state == 1):
                if (cur_end - i - 1 >= min_length):
                    out[cur_num_str, 0] = i + 1
                    out[cur_num_str, 1] = cur_end
                    cur_num_str += 1
                elif (cur_end - i - 1 == 1):
                    count_one += 1
                elif (cur_end - i - 1 == 2):
                    count_two += 1
                elif (cur_end - i - 1 == 3):
                    count_three += 1
                    
            state = 1
            cur_end = i
        else:
            if binary_search(askii_list, all_elems_codes[i]) == -1:
                if (state == 1):
                    state = 0

                    if (cur_end - i - 1 >= min_length):
                        out[cur_num_str, 0] = i + 1
                        out[cur_num_str, 1] = cur_end
                        cur_num_str += 1
                    elif (cur_end - i - 1 == 1):
                        count_one += 1
                    elif (cur_end - i - 1 == 2):
                        count_two += 1
                    elif (cur_end - i - 1 == 3):
                        count_three += 1
        i -= 1
        if cur_num_str == MAX_STR:
            break
    return cur_num_str, count_one, count_two, count_three


#ex_numba = autojit(extract, nopython=True)


def get_dict():
    d = {format(key, '02X'): key for key in range(256)}
    d['??'] = 256
    return d

def get_strings(byte_data):
    text = byte_data
    name = ''
    # loai bo cac ki tu thua
    lines = ''.join(text).split('\r\n')
    
    
    all_elems_codes = []
    convert_dict = get_dict()
    # ASCII printable characters : 32 - 127; 13\r ; 10\n
    askii_list = np.array(range(32, 127) + [13, 10])
    askii_list.sort()

    for l in lines:
        elems = l.split(' ')
        all_elems_codes.extend([convert_dict[x] for x in elems[1:]])
    # Mot dong 00401000 C7 01 24 04 5C 00 E9 D6 4A 00 00 CC CC CC CC CC => bo 00401000 con: [199   1  36 .... ]
    all_elems_codes = np.array(all_elems_codes)
    # Ma tran 15000 x 2
    out_ = np.zeros([15000, 2], dtype=np.int64)

    m,count_one,count_two, count_three = extract(all_elems_codes, out_, askii_list)
    
    string_total_len = np.sum(out_[:,1] - out_[:,0]) + count_one + count_two + count_three
    string_ratio = float(string_total_len)/len(all_elems_codes)

    strings = []
    # m la so luong string cua file
    for i in range(m):
        strings.extend(
            [''.join([chr(x) for x in all_elems_codes[out_[i, 0]:out_[i, 1]]])])

    return [name, strings, [count_one,count_two,count_three,string_total_len,string_ratio]]



def extract_length(data):

    print data[0][2]
    another_f = np.vstack([x[2] for x in data])
    print another_f
    sys.exit()

    len_arrays = [np.array([len(y) for y in x[1]] + [0]+[10000]) for x in data]
    bincounts = [ np.bincount(arr) for  arr in len_arrays]

    counts  = np.concatenate([another_f[:,:3],  np.vstack([ arr[4:100] for  arr in bincounts])],axis = 1)
    counts_0_10  =  np.sum(counts[:,0:10],axis = 1)[:,None]
    counts_10_30  =  np.sum(counts[:,10:30],axis = 1)[:,None]
    counts_30_60  =  np.sum(counts[:,30:60],axis = 1)[:,None]
    counts_60_90  =  np.sum(counts[:,60:90],axis = 1)[:,None] 
    counts_0_100  =  np.sum(counts[:,0:100],axis = 1)[:,None] 

    counts_100_150  = [ np.sum(arr[100:150]) for  arr in bincounts]
    counts_150_250  = [ np.sum(arr[150:250]) for  arr in bincounts]
    counts_250_400  = [ np.sum(arr[250:450]) for  arr in bincounts]
    counts_400_600  = [ np.sum(arr[400:600]) for  arr in bincounts]
    counts_600_900  = [ np.sum(arr[600:900]) for  arr in bincounts]
    counts_900_1300  = [ np.sum(arr[900:1300]) for  arr in bincounts]
    counts_1300_2000  = [ np.sum(arr[1300:2000]) for  arr in bincounts]
    counts_2000_3000  = [ np.sum(arr[2000:3000]) for  arr in bincounts]
    counts_3000_6000  = [ np.sum(arr[3000:6000]) for  arr in bincounts]
    counts_6000_15000 = [ np.sum(arr[6000:15000]) for  arr in bincounts]

    med = np.array([np.median([len(y) for y in x[1]] + [0])  for x in data ])[:,None]
    mean = np.array([np.mean([len(y) for y in x[1]] + [0])  for x in data ])[:,None]
    var = np.array([np.var([len(y) for y in x[1]] + [0])  for x in data ])[:,None]


    feats = np.concatenate([np.vstack(counts),
                            counts_0_10,
                            counts_10_30,
                            counts_30_60,
                            counts_60_90,
                            counts_0_100,
                            np.array(counts_100_150)[:,None],
                            np.array(counts_150_250)[:,None],
                            np.array(counts_250_400)[:,None],
                            np.array(counts_400_600)[:,None],
                            np.array(counts_600_900)[:,None],  
                            np.array(counts_900_1300)[:,None], 
                            np.array(counts_1300_2000)[:,None],
                            np.array(counts_2000_3000)[:,None],
                            np.array(counts_3000_6000)[:,None],
                            np.array(counts_6000_15000)[:,None],
                            another_f[:,3:]
                            ],axis = 1)
    return feats



def dump_names(strings_feats_dir):
    n = ['string_len_counts_' + str(x) for x in range(1,100)] + [
        'string_len_counts_0_10',
        'string_len_counts_10_30',
        'string_len_counts_30_60',
        'string_len_counts_60_90',
        'string_len_counts_0_100',
        'string_len_counts_100_150',
        'string_len_counts_150_250',
        'string_len_counts_250_400',
        'string_len_counts_400_600',
        'string_len_counts_600_900',
        'string_len_counts_900_1300',
        'string_len_counts_1300_2000',
        'string_len_counts_2000_3000',
        'string_len_counts_3000_6000',
        'string_len_counts_6000_15000',
        'string_total_len',
        'string_ratio'
    ]


    hickle.dump(n,os.path.join(strings_feats_dir,'strings_feats_names'))

def byte_string_lengths(file_name):
    x = get_strings(file_name)
    strs_len = extract_length([x])
    return strs_len[0].tolist()


file_path = "samples/01IsoiSMh5gxyDYTl4CB.asm"
#file_path = "samples/01SuzwMJEIXsK7A8dQbl.asm"
ff = open("samples/01IsoiSMh5gxyDYTl4CB.bytes", 'r')
with open(file_path) as f:
    byte_code = f.readlines()

print byte_string_lengths(ff)