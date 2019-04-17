import argparse
import requests
import json
import time, os, sys

CUCKOO_REST_HOST = 'http://localhost:8090/'

def submit_sample(sample_path) :   
    """
    Submits samples to cuckoo sandbox
    INPUT : sample_path : filepath to sample to submit
    OUTPUT : task_ids : list : task ids return from cuckoo
    """

    REST_URL = "http://localhost:8090/tasks/create/file"

    files = os.listdir(sample_path)
    mal_files = [i for i in files]
    print mal_files
    sys.exit()
    SAMPLE_FILE = sample_path
    
    HEADERS = {"Authorization": "Bearer S4MPL3"}

    with open(SAMPLE_FILE, "rb") as sample:
        print sample
        files = {"file": ("temp_file_name", sample)}
        r = requests.post(REST_URL, headers=HEADERS, files=files)

    print r.json()
    
    # Add your code to error checking for r.status_code.

    task_id = r.json()["task_id"]
    print task_id
    
    # Add your code for error checking if task_id is None.
    
    return task_id


#submit samples to cuckoo sanbox
from os import getcwd
print(getcwd())
#os.chdir(r'Family_Samples/Simda')
#script_dir = os.path.dirname(path) #<-- absolute dir the script is in
#open(script_dir, 'rb')
# submit_sample(getcwd()+'/1')
submit_sample(getcwd())
