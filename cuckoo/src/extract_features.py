import json, sys, collections
dic = {}
def features_api(json_report):
    api_dict = {}
    for key in json_report['behavior']['apistats']:
        for key2, value in json_report['behavior']['apistats'][key].iteritems():
            if key2 in api_dict:
                api_dict[key2] += value
            else:
                api_dict[key2] = value
    dic.update(api_dict)


def features_sign(json_report):
    sign_dict = {}
    len_sign = len(json_report['signatures'])
    for i in range (0, len_sign):
        for key, value in json_report['signatures'][i].iteritems()  :
            if (key == 'name') :
                if value not in sign_dict:
                    sign_dict[value] = 1
    dic.update(sign_dict)

def features_behavior(json_report):
    be_dict = {}
    len_be = len(json_report['behavior'])
    for key in json_report['behavior']['summary'] :
        if key not in be_dict:
            be_dict[key] = 1
    dic.update(be_dict)

def create_feature(json_report) :
    #create container for features
    features = {}
    features.update(features_api(json_report))

    return features

import csv, os
from collections import OrderedDict
from os import getcwd

mal_fam = ['dridex', 'kelihos', 'locky', 'ramnit', 'sality', 'simda', 'vawtrak', 'zeus']

count_fam = []

for i in mal_fam:
    files = os.listdir(getcwd()+'/json_'+i)
    count_fam += [len([name for name in files])]

for i in mal_fam:
    csv_file = open('api.csv', 'w')
    print i.upper() + ' - extracting from json report files:\n'
    for j in range(1, count_fam[mal_fam.index(i)]+1):
        with open('json_'+i+'/'+str(j)+'report.json') as json_file:  
            data = json.load(json_file)
            try:
                features_behavior(data)
            except :
                print str(j), " => FAIL"
                continue

            # x = OrderedDict(sorted(data.items(), key=lambda kv: kv[0]))

            # writer = csv.DictWriter(csv_file, fieldnames=x.keys())
            # if j == 1:
            #     writer.writeheader()
            # writer.writerow(x)
        print (str(j)+' => OK')

def features_api2(json_report):
    features = {}
    api_dict_keys = [u'CertControlStore', u'CertCreateCertificateContext', u'CertOpenStore', u'CertOpenSystemStoreA', u'CertOpenSystemStoreW', u'CoCreateInstance', u'CoCreateInstanceEx', u'CoGetClassObject', u'CoInitializeEx', u'CoInitializeSecurity', u'CoUninitialize', u'ControlService', u'CopyFileA', u'CopyFileExW', u'CopyFileW', u'CreateActCtxW', u'CreateDirectoryExW', u'CreateDirectoryW', u'CreateJobObjectW', u'CreateProcessInternalW', u'CreateRemoteThread', u'CreateRemoteThreadEx', u'CreateServiceA', u'CreateServiceW', u'CreateThread', u'CreateToolhelp32Snapshot', u'CryptAcquireContextA', u'CryptAcquireContextW', u'CryptCreateHash', u'CryptDecodeObjectEx', u'CryptEncrypt', u'CryptExportKey', u'CryptGenKey', u'CryptHashData', u'CryptProtectData', u'CryptUnprotectData', u'DeleteFileW', u'DeleteService', u'DeleteUrlCacheEntryA', u'DeleteUrlCacheEntryW', u'DeviceIoControl', u'DnsQuery_A', u'DrawTextExA', u'DrawTextExW', u'EnumServicesStatusA', u'EnumServicesStatusW', u'EnumWindows', u'FindFirstFileExW', u'FindResourceA', u'FindResourceExA', u'FindResourceExW', u'FindResourceW', u'FindWindowA', u'FindWindowExA', u'FindWindowExW', u'FindWindowW', u'GetAdaptersAddresses', u'GetAdaptersInfo', u'GetAddrInfoW', u'GetAsyncKeyState', u'GetBestInterfaceEx', u'GetComputerNameA', u'GetComputerNameW', u'GetCursorPos', u'GetDiskFreeSpaceExW', u'GetDiskFreeSpaceW', u'GetFileAttributesExW', u'GetFileAttributesW', u'GetFileInformationByHandle', u'GetFileInformationByHandleEx', u'GetFileSize', u'GetFileSizeEx', u'GetFileType', u'GetFileVersionInfoExW', u'GetFileVersionInfoSizeExW', u'GetFileVersionInfoSizeW', u'GetFileVersionInfoW', u'GetForegroundWindow', u'GetInterfaceInfo', u'GetKeyState', u'GetKeyboardState', u'GetNativeSystemInfo', u'GetShortPathNameW', u'GetSystemDirectoryA', u'GetSystemDirectoryW', u'GetSystemInfo', u'GetSystemMetrics', u'GetSystemTimeAsFileTime', u'GetSystemWindowsDirectoryA', u'GetSystemWindowsDirectoryW', u'GetTempPathW', u'GetTimeZoneInformation', u'GetUserNameA', u'GetUserNameExA', u'GetUserNameExW', u'GetUserNameW', u'GetVolumeNameForVolumeMountPointW', u'GetVolumePathNameW', u'GetVolumePathNamesForVolumeNameW', u'GlobalMemoryStatus', u'GlobalMemoryStatusEx', u'HttpOpenRequestA', u'HttpOpenRequestW', u'HttpQueryInfoA', u'HttpSendRequestA', u'HttpSendRequestW', u'IWbemServices_ExecQuery', u'InternetCloseHandle', u'InternetConnectA', u'InternetConnectW', u'InternetCrackUrlA', u'InternetCrackUrlW', u'InternetGetConnectedState', u'InternetGetConnectedStateExA', u'InternetOpenA', u'InternetOpenUrlA', u'InternetOpenUrlW', u'InternetOpenW', u'InternetQueryOptionA', u'InternetReadFile', u'InternetSetOptionA', u'InternetSetStatusCallback', u'IsDebuggerPresent', u'LdrGetDllHandle', u'LdrGetProcedureAddress', u'LdrLoadDll', u'LdrUnloadDll', u'LoadResource', u'LoadStringA', u'LoadStringW', u'LookupAccountSidW', u'LookupPrivilegeValueW', u'MessageBoxTimeoutA', u'MessageBoxTimeoutW', u'Module32FirstW', u'Module32NextW', u'MoveFileWithProgressW', u'NetGetJoinInformation', u'NetShareEnum', u'NetUserGetInfo', u'NtAllocateVirtualMemory', u'NtClose', u'NtCreateFile', u'NtCreateKey', u'NtCreateMutant', u'NtCreateSection', u'NtCreateThreadEx', u'NtCreateUserProcess', u'NtDelayExecution', u'NtDeleteFile', u'NtDeleteKey', u'NtDeleteValueKey', u'NtDeviceIoControlFile', u'NtDuplicateObject', u'NtEnumerateKey', u'NtEnumerateValueKey', u'NtFreeVirtualMemory', u'NtGetContextThread', u'NtMapViewOfSection', u'NtOpenDirectoryObject', u'NtOpenFile', u'NtOpenKey', u'NtOpenKeyEx', u'NtOpenMutant', u'NtOpenProcess', u'NtOpenSection', u'NtOpenThread', u'NtProtectVirtualMemory', u'NtQueryAttributesFile', u'NtQueryDirectoryFile', u'NtQueryFullAttributesFile', u'NtQueryInformationFile', u'NtQueryKey', u'NtQueryMultipleValueKey', u'NtQuerySystemInformation', u'NtQueryValueKey', u'NtQueueApcThread', u'NtReadFile', u'NtReadVirtualMemory', u'NtResumeThread', u'NtSaveKey', u'NtSetContextThread', u'NtSetInformationFile', u'NtSetValueKey', u'NtShutdownSystem', u'NtSuspendThread', u'NtTerminateProcess', u'NtTerminateThread', u'NtUnmapViewOfSection', u'NtWriteFile', u'NtWriteVirtualMemory', u'ObtainUserAgentString', u'OleInitialize', u'OpenSCManagerA', u'OpenSCManagerW', u'OpenServiceA', u'OpenServiceW', u'OutputDebugStringA', u'Process32FirstW', u'Process32NextW', u'ReadCabinetState', u'ReadProcessMemory', u'RegCloseKey', u'RegCreateKeyExA', u'RegCreateKeyExW', u'RegDeleteKeyA', u'RegDeleteKeyW', u'RegDeleteValueA', u'RegDeleteValueW', u'RegEnumKeyExA', u'RegEnumKeyExW', u'RegEnumKeyW', u'RegEnumValueA', u'RegEnumValueW', u'RegOpenKeyExA', u'RegOpenKeyExW', u'RegQueryInfoKeyA', u'RegQueryInfoKeyW', u'RegQueryValueExA', u'RegQueryValueExW', u'RegSetValueExA', u'RegSetValueExW', u'RegisterHotKey', u'RemoveDirectoryA', u'RemoveDirectoryW', u'RtlAddVectoredContinueHandler', u'RtlAddVectoredExceptionHandler', u'RtlCreateUserThread', u'RtlDecompressBuffer', u'RtlRemoveVectoredExceptionHandler', u'SHGetFolderPathW', u'SHGetSpecialFolderLocation', u'SearchPathW', u'SendNotifyMessageA', u'SendNotifyMessageW', u'SetEndOfFile', u'SetErrorMode', u'SetFileAttributesW', u'SetFileInformationByHandle', u'SetFilePointer', u'SetFilePointerEx', u'SetFileTime', u'SetInformationJobObject', u'SetStdHandle', u'SetUnhandledExceptionFilter', u'SetWindowsHookExA', u'SetWindowsHookExW', u'ShellExecuteExW', u'SizeofResource', u'StartServiceA', u'StartServiceW', u'Thread32First', u'Thread32Next', u'URLDownloadToFileW', u'UnhookWindowsHookEx', u'UuidCreate', u'WSARecv', u'WSASend', u'WSASendTo', u'WSASocketA', u'WSASocketW', u'WSAStartup', u'WriteConsoleA', u'WriteConsoleW', u'WriteProcessMemory', u'__exception__', u'accept', u'bind', u'closesocket', u'connect', u'getaddrinfo', u'gethostbyname', u'getsockname', u'ioctlsocket', u'listen', u'recv', u'recvfrom', u'select', u'send', u'sendto', u'setsockopt', u'shutdown', u'socket', u'timeGetTime']
    # Khoi tao
    for i in api_dict_keys:
        features[i] = 0

    for key in json_report['behavior']['apistats']:
        for key2, value in json_report['behavior']['apistats'][key].iteritems():
            features['api_' + key2] += value

    return features
print dic
list_api = []
for key in OrderedDict(sorted(dic.items(), key=lambda kv: kv[0])):
    list_api.append(key)
print list_api