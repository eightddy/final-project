import json, sys, collections

def features_info(json_report):
    features = {}
    # INFO
    # id, score, category, duration
    if 'info' in json_report:
        for key, value in json_report['info'].iteritems()  :
            if (key == 'id' or key == 'score' or key == 'category' or key == 'duration') :
                features['info_'+key] = value
    return features

def features_procmem(json_report):
    # PROCMEMORY
    # procmemory count
    features = {}
    if 'procmemory' in json_report:
        features['procmem_count'] = len(json_report['procmemory'])
    else:
        features['procmem_count'] = 0
    return features

def features_target(json_report):
    # TARGET
    # category, file.size
    features = {}
    if 'signatures' in json_report:
        if 'category' in json_report['target']:
            features['target_category'] = json_report['target']['category']
        else: 
            features['target_category'] = ""
        
        if 'size' in json_report['target']['file']:        
            features['target_size'] = json_report['target']['file']['size']
        else:
            features['target_size'] = 0
    return features

def features_buffer(json_report):
    # BUFFER
    # count of buffer
    features = {}
    if 'buffer' in json_report:
        features['buffer_count'] = len(json_report['buffer'])
    else:
        features['buffer_count'] = 0
    return features

def features_extracted(json_report):
    # EXTRACTED
    # extracted file count
    features = {}
    if 'extracted' in json_report:
        features['extracted_count'] = len(json_report['extracted'])
    else:
        features['extracted_count'] = 0
    return features

def features_virustotal(json_report):
    # VIRUSTOTAL
    # positive, total, proportion positive / total
    features = {}
    if 'virustotal' in json_report and 'total' in json_report['virustotal']:
        features['virustt_total'] = json_report['virustotal']['total']
        features['virustt_positive'] = json_report['virustotal']['positives']
        features['virustt_proportion'] = float(json_report['virustotal']['positives']) / json_report['virustotal']['total']
    else:
        features['virustt_total'] = 0
        features['virustt_positive'] = 0
        features['virustt_proportion'] = 0
    return features

def features_signatures(json_report):
    # SIGNATURES: len_sign
    # Read maximnum 15 signs
    # foreach sign: markcount, description, severity, name
    features = {}
    # refer: https://cuckoo.readthedocs.io/en/latest/customization/signatures/
    SIGN_MAX_COUNT = 15
    if 'signatures' in json_report:
        len_sign = len(json_report['signatures'])
        features['sign_len'] = len_sign
        for i in range (0, len_sign):
            if i == SIGN_MAX_COUNT:
                break
            for key, value in json_report['signatures'][i].iteritems()  :
                if (key == 'markcount' or key == 'description' or key == 'severity' or key == 'name') :
                    features['sign_' + str(i)+ '_' + key] = value
        if len_sign < SIGN_MAX_COUNT:
            for i in range (len_sign, SIGN_MAX_COUNT):
                features['sign_' + str(i)+ '_markcount'] = 0
                features['sign_' + str(i)+ '_description'] = ""
                features['sign_' + str(i)+ '_severity'] = 0
                features['sign_' + str(i)+ '_name'] = ""
    return features

def features_network(json_report):
    features = {}
    # NETWORK
    # count: tls, udp, dns_server, http, icmp, cmtp, tcp, ... http_ex
    if 'network' in json_report : 
        for key, value in json_report['network'].iteritems()  :
            try : 
                features['network_'+key] = len(value)
            except :
                pass
    return features

def features_static(json_report):
    features = {}
    # STATIC
    # COUNT: pe_imports, keys, signature, pe_timestamp, pe_exports, imported_dll_count, pe_resources, pe_versioninfo, pe_sections
    keys = ['pe_imports', 'keys', 'signature', 'pe_timestamp', 'pe_exports', 'imported_dll_count', 'pe_resources', 'pe_versioninfo', 'pe_sections']
    if 'static' in json_report:
        for key, value in json_report['static'].iteritems()  :
            if key == 'imported_dll_count':
                features['static_'+str(key)] = value
            elif key in keys:
                features['static_'+key] = len(value)
    elif:
        for key in keys:
            features['static_'+key] = 0
    return features

def features_dropped(json_report):
    features = {}
    # DROPPED
    # COUNT: dropped
    if 'dropped' in json_report:
        features['dropped_count'] = len(json_report['dropped'])
    else :
        features['dropped_count'] = 0
    return features

def features_strings(json_report):
    features = {}
    # DROPPED
    # COUNT: dropped
    if 'strings' in json_report:
        features['strings_count'] = len(json_report['strings'])
    else :
        features['strings_count'] = 0
    return features

def features_behavior(json_report):
    features = {}
    # BEHAVIOR
    # SUMMARY:
    BEHAVIOR_MAX_COUNT = 20
    if 'behavior' in json_report:
        features['behavior_generic_count'] = len(json_report['behavior']['generic'])
        features['behavior_apistats_count'] = len(json_report['behavior']['apistats'])
        features['behavior_processes_count'] = len(json_report['behavior']['processes'])
        features['behavior_processtree_count'] = len(json_report['behavior']['processtree'])
        features['behavior_summary_count'] = len(json_report['behavior']['summary'])

        len_summary = len(json_report['behavior']['summary'])
        i = 0
        for key in json_report['behavior']['summary'] :
            if i == BEHAVIOR_MAX_COUNT :
                break
            features['behavior_' + str(i)] = key
            i += 1
        if len_summary < BEHAVIOR_MAX_COUNT:
            for i in range (len_summary, BEHAVIOR_MAX_COUNT):
                features['behavior_' + str(i)] = ""
    return features

def features_api(json_report):
    features = {}
    API_COUNT = 100
    # API top 100
    api_dict = {}
    for key in json_report['behavior']['apistats']:
        for key2, value in json_report['behavior']['apistats'][key].iteritems():
            if key2 in api_dict:
                api_dict[key2] += value
            else:
                api_dict[key2] = value
    i = 0
    for key, value in sorted(api_dict.items(), key=lambda kv: kv[1], reverse=True):
        if i == API_COUNT:
            break
        # features['api_'+str(i)] = api_dict[key]
        features['api_'+str(i)] = key
        i += 1
    if len(api_dict) < API_COUNT:
        for i in range(len(api_dict), API_COUNT):
            features['api_'+str(i)] = ""

    return features


def create_feature(json_report) :
    #create container for features
    features = {}
    features['count'] = len(json_report)
    # print features_info(json_report)
    # print features_procmem(json_report)
    # print features_target(json_report)
    # print features_buffer(json_report)
    # print features_extracted(json_report)
    # print features_virustotal(json_report)
    # print features_signatures(json_report)
    # print features_network(json_report)    
    # print features_static(json_report)
    # print features_dropped(json_report)
    # print features_strings(json_report)
    # print features_behavior(json_report)
    # print features_api(json_report)

    features.update(features_info(json_report))
    features.update(features_procmem(json_report))
    features.update(features_target(json_report))
    features.update(features_buffer(json_report))
    features.update(features_extracted(json_report))
    features.update(features_virustotal(json_report))
    features.update(features_signatures(json_report))
    features.update(features_network(json_report))
    features.update(features_static(json_report))
    features.update(features_dropped(json_report))
    features.update(features_strings(json_report))
    features.update(features_behavior(json_report))
    features.update(features_api(json_report))

    print "\nRes: ", features
with open('/home/huydung/.cuckoo/storage/analyses/1/reports/report.json') as json_file:  
    data = json.load(json_file)

create_feature(data)

