import json, sys, collections

def features_info(json_report):
    features = {}
    # INFO
    # id, score, category, duration
    if 'info' in json_report:
        for key, value in json_report['info'].iteritems()  :
            if (key == 'score' or key == 'duration') :
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
    if 'target' in json_report:
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
    sign_keys = [u'allocates_execute_remote_process', u'allocates_rwx', u'antianalysis_detectfile', u'antiav_bitdefender_libs', u'antiav_detectreg', u'antiav_servicestop', u'antidbg_devices', u'antidbg_windows', u'antiemu_wine', u'antisandbox_cuckoo_files', u'antisandbox_foregroundwindows', u'antisandbox_idletime', u'antisandbox_mouse_hook', u'antisandbox_restart', u'antisandbox_sleep', u'antivirus_virustotal', u'antivm_disk_size', u'antivm_firmware', u'antivm_generic_bios', u'antivm_generic_cpu', u'antivm_generic_disk', u'antivm_generic_scsi', u'antivm_generic_services', u'antivm_memory_available', u'antivm_network_adapters', u'antivm_queries_computername', u'antivm_sandboxie', u'antivm_shared_device', u'antivm_vbox_devices', u'antivm_vbox_files', u'antivm_vbox_keys', u'antivm_vmware_files', u'antivm_vmware_in_instruction', u'antivm_vmware_keys', u'applcation_raises_exception', u'av_detect_china_key', u'banker_bancos', u'banker_zeus_p2p', u'banking_mutexes', u'bootkit', u'browser_security', u'browser_startpage', u'bypass_firewall', u'checks_debugger', u'console_output', u'creates_doc', u'creates_hidden_file', u'creates_largekey', u'creates_service', u'creates_shortcut', u'cryptomining_stratum_command', u'dead_host', u'deepfreeze_mutex', u'deletes_executed_files', u'detect_putty', u'disables_browser_warn', u'disables_proxy', u'disables_security', u'disables_spdy_ie', u'disables_system_restore', u'dns_freehosting_domain', u'dridex_behavior', u'dropper', u'dumped_buffer', u'dumped_buffer2', u'dyreza', u'emotet_behavior', u'exe_appdata', u'generates_crypto_key', u'has_pdb', u'has_wmi', u'infostealer_bitcoin', u'infostealer_browser', u'infostealer_ftp', u'infostealer_keylogger', u'infostealer_mail', u'injection_createremotethread', u'injection_modifies_memory', u'injection_network_trafic', u'injection_ntsetcontextthread', u'injection_process_search', u'injection_queueapcthread', u'injection_resumethread', u'injection_runpe', u'injection_write_memory', u'injection_write_memory_exe', u'installs_bho', u'locates_browser', u'locates_sniffer', u'locker_taskmgr', u'memdump_ip_urls', u'memdump_urls', u'modifies_boot_config', u'modifies_certificates', u'modifies_desktop_wallpaper', u'modifies_proxy_autoconfig', u'modifies_security_center_warnings', u'modifies_zoneid', u'modify_uac_prompt', u'moves_self', u'multiple_useragents', u'network_bind', u'network_cnc_http', u'network_http', u'network_icmp', u'networkdyndns_checkip', u'nitol', u'nolookup_communication', u'nymaim_behavior', u'origin_langid', u'p2p_cnc', u'packer_entropy', u'packer_upx', u'packer_vmprotect', u'pe_features', u'pe_unknown_resource_name', u'peid_packer', u'persistence_ads', u'persistence_autorun', u'privilege_luid_check', u'process_interest', u'process_martian', u'process_needed', u'protection_rx', u'queries_programs', u'raises_exception', u'ramnit', u'ransomware_appends_extensions', u'ransomware_bcdedit', u'ransomware_dropped_files', u'ransomware_extensions', u'ransomware_file_moves', u'ransomware_files', u'ransomware_mass_file_delete', u'ransomware_message', u'ransomware_shadowcopy', u'rat_flystudio', u'rat_rbot', u'rat_xtreme', u'reads_user_agent', u'recon_beacon', u'recon_checkip', u'recon_fingerprint', u'recon_programs', u'recon_systeminfo', u'removes_zoneid_ads', u'self_delete_bat', u'smtp_gmail', u'smtp_live', u'smtp_yahoo', u'spreading_autoruninf', u'stealth_hiddenfile', u'stealth_system_procname', u'stealth_window', u'stops_service', u'suspicious_command_tools', u'suspicious_powershell', u'suspicious_process', u'suspicious_tld', u'suspicious_write_exe', u'sysinternals_tools_usage', u'terminates_remote_process', u'upatre', u'uses_windows_utilities', u'wmi_antivm']
    sign_name = ['sign_'+sign  for sign in sign_keys]
    sign_markcount = ['sign_' + sign + '_markcount' for sign in sign_keys]
    sign_severity = ['sign_' + sign + '_severity' for sign in sign_keys]
    
    sign = sign_name + sign_markcount + sign_severity

    # Khoi tao
    for i in sign:
        features[i] = 0
    if 'signatures' in json_report:
        len_sign = len(json_report['signatures'])
        features['sign_len'] = len_sign

        for i in range (0, len_sign):
            # for key, value in json_report['signatures'][i].iteritems()  :
            # if (key == 'markcount' or key == 'description' or key == 'severity' or key == 'name') :
            name = json_report['signatures'][i]['name']
            features['sign_' + name] = 1
            features['sign_' + name + '_markcount'] = json_report['signatures'][i]['markcount']
            features['sign_' + name + '_severity'] = json_report['signatures'][i]['severity']
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
    else:
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
    if 'behavior' in json_report:
        features['behavior_generic_count'] = len(json_report['behavior']['generic'])
        features['behavior_apistats_count'] = len(json_report['behavior']['apistats'])
        features['behavior_processes_count'] = len(json_report['behavior']['processes'])
        features['behavior_processtree_count'] = len(json_report['behavior']['processtree'])
        features['behavior_summary_count'] = len(json_report['behavior']['summary'])

        behavior_keys = [u'command_line', u'connects_host', u'connects_ip', u'directory_created', u'directory_enumerated', u'directory_removed', u'dll_loaded', u'downloads_file', u'fetches_url', u'file_copied', u'file_created', u'file_deleted', u'file_exists', u'file_failed', u'file_moved', u'file_opened', u'file_read', u'file_recreated', u'file_written', u'guid', u'mutex', u'regkey_deleted', u'regkey_opened', u'regkey_read', u'regkey_written', u'resolves_host', u'wmi_query']
        behavior_keys = ['behavior_' + be for be in behavior_keys]
        len_summary = len(json_report['behavior']['summary'])

        for i in behavior_keys:
            features[i] = 0
        for key in json_report['behavior']['summary'] :
            features['behavior_' + key] = len(json_report['behavior']['summary'][key])
    return features


def features_api(json_report):
    features = {}
    api_dict_keys = [u'CertControlStore', u'CertCreateCertificateContext', u'CertOpenStore', u'CertOpenSystemStoreA', u'CertOpenSystemStoreW', u'CoCreateInstance', u'CoCreateInstanceEx', u'CoGetClassObject', u'CoInitializeEx', u'CoInitializeSecurity', u'CoUninitialize', u'ControlService', u'CopyFileA', u'CopyFileExW', u'CopyFileW', u'CreateActCtxW', u'CreateDirectoryExW', u'CreateDirectoryW', u'CreateJobObjectW', u'CreateProcessInternalW', u'CreateRemoteThread', u'CreateRemoteThreadEx', u'CreateServiceA', u'CreateServiceW', u'CreateThread', u'CreateToolhelp32Snapshot', u'CryptAcquireContextA', u'CryptAcquireContextW', u'CryptCreateHash', u'CryptDecodeObjectEx', u'CryptEncrypt', u'CryptExportKey', u'CryptGenKey', u'CryptHashData', u'CryptProtectData', u'CryptUnprotectData', u'DeleteFileW', u'DeleteService', u'DeleteUrlCacheEntryA', u'DeleteUrlCacheEntryW', u'DeviceIoControl', u'DnsQuery_A', u'DrawTextExA', u'DrawTextExW', u'EnumServicesStatusA', u'EnumServicesStatusW', u'EnumWindows', u'FindFirstFileExW', u'FindResourceA', u'FindResourceExA', u'FindResourceExW', u'FindResourceW', u'FindWindowA', u'FindWindowExA', u'FindWindowExW', u'FindWindowW', u'GetAdaptersAddresses', u'GetAdaptersInfo', u'GetAddrInfoW', u'GetAsyncKeyState', u'GetBestInterfaceEx', u'GetComputerNameA', u'GetComputerNameW', u'GetCursorPos', u'GetDiskFreeSpaceExW', u'GetDiskFreeSpaceW', u'GetFileAttributesExW', u'GetFileAttributesW', u'GetFileInformationByHandle', u'GetFileInformationByHandleEx', u'GetFileSize', u'GetFileSizeEx', u'GetFileType', u'GetFileVersionInfoExW', u'GetFileVersionInfoSizeExW', u'GetFileVersionInfoSizeW', u'GetFileVersionInfoW', u'GetForegroundWindow', u'GetInterfaceInfo', u'GetKeyState', u'GetKeyboardState', u'GetNativeSystemInfo', u'GetShortPathNameW', u'GetSystemDirectoryA', u'GetSystemDirectoryW', u'GetSystemInfo', u'GetSystemMetrics', u'GetSystemTimeAsFileTime', u'GetSystemWindowsDirectoryA', u'GetSystemWindowsDirectoryW', u'GetTempPathW', u'GetTimeZoneInformation', u'GetUserNameA', u'GetUserNameExA', u'GetUserNameExW', u'GetUserNameW', u'GetVolumeNameForVolumeMountPointW', u'GetVolumePathNameW', u'GetVolumePathNamesForVolumeNameW', u'GlobalMemoryStatus', u'GlobalMemoryStatusEx', u'HttpOpenRequestA', u'HttpOpenRequestW', u'HttpQueryInfoA', u'HttpSendRequestA', u'HttpSendRequestW', u'IWbemServices_ExecQuery', u'InternetCloseHandle', u'InternetConnectA', u'InternetConnectW', u'InternetCrackUrlA', u'InternetCrackUrlW', u'InternetGetConnectedState', u'InternetGetConnectedStateExA', u'InternetOpenA', u'InternetOpenUrlA', u'InternetOpenUrlW', u'InternetOpenW', u'InternetQueryOptionA', u'InternetReadFile', u'InternetSetOptionA', u'InternetSetStatusCallback', u'IsDebuggerPresent', u'LdrGetDllHandle', u'LdrGetProcedureAddress', u'LdrLoadDll', u'LdrUnloadDll', u'LoadResource', u'LoadStringA', u'LoadStringW', u'LookupAccountSidW', u'LookupPrivilegeValueW', u'MessageBoxTimeoutA', u'MessageBoxTimeoutW', u'Module32FirstW', u'Module32NextW', u'MoveFileWithProgressW', u'NetGetJoinInformation', u'NetShareEnum', u'NetUserGetInfo', u'NtAllocateVirtualMemory', u'NtClose', u'NtCreateFile', u'NtCreateKey', u'NtCreateMutant', u'NtCreateSection', u'NtCreateThreadEx', u'NtCreateUserProcess', u'NtDelayExecution', u'NtDeleteFile', u'NtDeleteKey', u'NtDeleteValueKey', u'NtDeviceIoControlFile', u'NtDuplicateObject', u'NtEnumerateKey', u'NtEnumerateValueKey', u'NtFreeVirtualMemory', u'NtGetContextThread', u'NtMapViewOfSection', u'NtOpenDirectoryObject', u'NtOpenFile', u'NtOpenKey', u'NtOpenKeyEx', u'NtOpenMutant', u'NtOpenProcess', u'NtOpenSection', u'NtOpenThread', u'NtProtectVirtualMemory', u'NtQueryAttributesFile', u'NtQueryDirectoryFile', u'NtQueryFullAttributesFile', u'NtQueryInformationFile', u'NtQueryKey', u'NtQueryMultipleValueKey', u'NtQuerySystemInformation', u'NtQueryValueKey', u'NtQueueApcThread', u'NtReadFile', u'NtReadVirtualMemory', u'NtResumeThread', u'NtSaveKey', u'NtSetContextThread', u'NtSetInformationFile', u'NtSetValueKey', u'NtShutdownSystem', u'NtSuspendThread', u'NtTerminateProcess', u'NtTerminateThread', u'NtUnmapViewOfSection', u'NtWriteFile', u'NtWriteVirtualMemory', u'ObtainUserAgentString', u'OleInitialize', u'OpenSCManagerA', u'OpenSCManagerW', u'OpenServiceA', u'OpenServiceW', u'OutputDebugStringA', u'Process32FirstW', u'Process32NextW', u'ReadCabinetState', u'ReadProcessMemory', u'RegCloseKey', u'RegCreateKeyExA', u'RegCreateKeyExW', u'RegDeleteKeyA', u'RegDeleteKeyW', u'RegDeleteValueA', u'RegDeleteValueW', u'RegEnumKeyExA', u'RegEnumKeyExW', u'RegEnumKeyW', u'RegEnumValueA', u'RegEnumValueW', u'RegOpenKeyExA', u'RegOpenKeyExW', u'RegQueryInfoKeyA', u'RegQueryInfoKeyW', u'RegQueryValueExA', u'RegQueryValueExW', u'RegSetValueExA', u'RegSetValueExW', u'RegisterHotKey', u'RemoveDirectoryA', u'RemoveDirectoryW', u'RtlAddVectoredContinueHandler', u'RtlAddVectoredExceptionHandler', u'RtlCreateUserThread', u'RtlDecompressBuffer', u'RtlRemoveVectoredExceptionHandler', u'SHGetFolderPathW', u'SHGetSpecialFolderLocation', u'SearchPathW', u'SendNotifyMessageA', u'SendNotifyMessageW', u'SetEndOfFile', u'SetErrorMode', u'SetFileAttributesW', u'SetFileInformationByHandle', u'SetFilePointer', u'SetFilePointerEx', u'SetFileTime', u'SetInformationJobObject', u'SetStdHandle', u'SetUnhandledExceptionFilter', u'SetWindowsHookExA', u'SetWindowsHookExW', u'ShellExecuteExW', u'SizeofResource', u'StartServiceA', u'StartServiceW', u'Thread32First', u'Thread32Next', u'URLDownloadToFileW', u'UnhookWindowsHookEx', u'UuidCreate', u'WSARecv', u'WSASend', u'WSASendTo', u'WSASocketA', u'WSASocketW', u'WSAStartup', u'WriteConsoleA', u'WriteConsoleW', u'WriteProcessMemory', u'__exception__', u'accept', u'bind', u'closesocket', u'connect', u'getaddrinfo', u'gethostbyname', u'getsockname', u'ioctlsocket', u'listen', u'recv', u'recvfrom', u'select', u'send', u'sendto', u'setsockopt', u'shutdown', u'socket', u'timeGetTime']
    api_dict_keys = ['api_'+api for api in api_dict_keys]

    # Khoi tao
    for i in api_dict_keys:
        features[i] = 0

    for key in json_report['behavior']['apistats']:
        for key2, value in json_report['behavior']['apistats'][key].iteritems():
            features['api_' + key2] += value

    return features


def create_feature(json_report, mal_fam) :
    #create container for features
    features = {}

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

    if (mal_fam == 'dridex'):
        features.update({u'zclass': 1})
    if (mal_fam == 'kelihos'):
        features.update({u'zclass': 2})
    if (mal_fam == 'locky'):
        features.update({u'zclass': 3})
    if (mal_fam == 'ramnit'):
        features.update({u'zclass': 4})
    if (mal_fam == 'sality'):
        features.update({u'zclass': 5})
    if (mal_fam == 'simda'):
        features.update({u'zclass': 6})
    if (mal_fam == 'vawtrak'):
        features.update({u'zclass': 7})
    if (mal_fam == 'zeus'):
        features.update({u'zclass': 8})
    
    return features

import csv, os
from collections import OrderedDict
from os import getcwd

mal_fam = ['dridex', 'kelihos', 'locky', 'ramnit', 'sality', 'simda', 'vawtrak', 'zeus']
# mal_fam = ['dridex', 'vawtrak']
count_fam = []

for i in mal_fam:
    files = os.listdir(getcwd()+'/json_'+i)
    count_fam += [len([name for name in files])]

for i in mal_fam:
    csv_file = open('csv/'+ i +'.csv', 'w')
    print 'Malware family: '+ i + ': extracting from json report files\n'
    for j in range(1, count_fam[mal_fam.index(i)]+1):
        with open('json_'+i+'/'+str(j)+'report.json') as json_file:  
            data = json.load(json_file)
            try:
                data = create_feature(data, i)
            except :
                print str(j), " => FAIL"
                continue

            x = OrderedDict(sorted(data.items(), key=lambda kv: kv[0]))

            writer = csv.DictWriter(csv_file, fieldnames=x.keys())
            if j == 1:
                writer.writeheader()
            writer.writerow(x)
        print (str(j)+' => OK')
    csv_file.close()
