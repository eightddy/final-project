from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import to_categorical


# Initialising the CNN
classifier = Sequential()
IMAGE_SIZE = (41, 44,1)
#IMAGE_SIZE = (50, 50)


# Step 1 - Convolution
classifier.add(Conv2D(filters=64, kernel_size=(3,3), activation='relu', input_shape=IMAGE_SIZE))
#classifier.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=IMAGE_SIZE, padding='same'))
classifier.add(Conv2D(filters=64, kernel_size=(3,3), activation='relu'))

classifier.add(Dropout(0.5))
# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = 2))

# Adding a second convolutional layer

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 9, activation = 'softmax'))

# Compiling the CNN
#classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

print (classifier.summary())

print ("===========================================================================================")

import sys
import numpy as np
import pandas as pd
from keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

dataset_train = pd.read_csv('train/LargeTrain.csv')
X_train = dataset_train.iloc[:, 0:1804].values
X_train = StandardScaler().fit_transform(X_train)
#X_train = X_train.reshape((10868, 41, 44, 1))
print X_train.shape
print X_train
#X_train = np.array()
y_train = dataset_train.iloc[:, 1804:1805].values
enc = OneHotEncoder()
enc.fit(y_train)  
y_train  = enc.transform(y_train)
print(y_train.shape)
print y_train
#y_train = to_categorical(y_train)
#sys.exit()


from sklearn.model_selection import train_test_split
#train_x, test_x, train_y, test_y = train_test_split(train_x_scaled, train_images_y_encoded, random_state = 101, test_size=0.25)
train_x, test_x, train_y, test_y = train_test_split(X_train, y_train, random_state = 101, test_size=0.101)



train_x = train_x.reshape((train_x.shape[0], 41, 44, 1))
test_x = test_x.reshape((test_x.shape[0], 41, 44, 1))
print train_x
print train_y.shape
print train_y

#sys.exit()
#X_train = X_train.reshape(X_train.shape[0],X_train.shape[1], 1)
#classifier.fit(X_train, y_train, batch_size = 10, epochs = 100, verbose=0)
classifier.fit(train_x, train_y, batch_size = 10, epochs = 100)


print("Val Score: ", classifier.evaluate(test_x, test_y))



























# Virtual,Offset,loc,Import,Imports,var,Forwarder,UINT,LONG,BOOL,WORD,BYTES,large,short,dd,db,dw,XREF,ptr,DATA,FUNCTION,extrn,byte,word,dword,char,DWORD,stdcall,arg,locret,asc,align,WinMain,unk,cookie,off,nullsub,DllEntryPoint,System32,dll,CHUNK,BASS,HMENU,DLL,LPWSTR,void,HRESULT,HDC,LRESULT,HANDLE,HWND,LPSTR,int,HLOCAL,FARPROC,ATOM,HMODULE,WPARAM,HGLOBAL,entry,rva,COLLAPSED,config,exe,Software,CurrentVersion,__imp_,INT_PTR,UINT_PTR,---Seperator,PCCTL_CONTEXT,__IMPORT_,INTERNET_STATUS_CALLBACK,.rdata:,.data:,.text:,misc_case,misc_installdir,misc_market,misc_microsoft,misc_policies,misc_proc,misc_scrollwindow,misc_search,misc_trap,misc_visualc,misc1____security_cookie,misc1_assume,misc1_callvirtualalloc,misc1_exportedentry,misc1_hardware,misc1_hkey_current_user,misc1_hkey_local_machine,misc1_sp-analysisfailed,misc1_unableto,ent_q_diffs_0,ent_q_diffs_1,ent_q_diffs_2,ent_q_diffs_3,ent_q_diffs_4,ent_q_diffs_5,ent_q_diffs_6,ent_q_diffs_7,ent_q_diffs_8,ent_q_diffs_9,ent_q_diffs_10,ent_q_diffs_11,ent_q_diffs_12,ent_q_diffs_13,ent_q_diffs_14,ent_q_diffs_15,ent_q_diffs_16,ent_q_diffs_17,ent_q_diffs_18,ent_q_diffs_19,ent_q_diffs_20,ent_q_diffs_mean,ent_q_diffs_var,ent_q_diffs_median,ent_q_diffs_max,ent_q_diffs_min,ent_q_diffs_max-min,ent_q_diff_diffs_0,ent_q_diff_diffs_1,ent_q_diff_diffs_2,ent_q_diff_diffs_3,ent_q_diff_diffs_4,ent_q_diff_diffs_5,ent_q_diff_diffs_6,ent_q_diff_diffs_7,ent_q_diff_diffs_8,ent_q_diff_diffs_9,ent_q_diff_diffs_10,ent_q_diff_diffs_11,ent_q_diff_diffs_12,ent_q_diff_diffs_13,ent_q_diff_diffs_14,ent_q_diff_diffs_15,ent_q_diff_diffs_16,ent_q_diff_diffs_17,ent_q_diff_diffs_18,ent_q_diff_diffs_19,ent_q_diff_diffs_20,ent_q_diff_diffs_mean,ent_q_diff_diffs_var,ent_q_diff_diffs_median,ent_q_diff_diffs_max,ent_q_diff_diffs_min,ent_q_diff_diffs_max-min,ent_q_diff_block_0_0,ent_q_diff_block_0_1,ent_q_diff_block_0_2,ent_q_diff_block_0_3,ent_q_diff_block_0_4,ent_q_diff_block_0_5,ent_q_diff_block_0_6,ent_q_diff_block_0_7,ent_q_diff_block_0_8,ent_q_diff_block_0_9,ent_q_diff_block_0_10,ent_q_diff_block_0_11,ent_q_diff_block_0_12,ent_q_diff_block_0_13,ent_q_diff_block_0_14,ent_q_diff_block_0_15,ent_q_diff_block_0_16,ent_q_diff_block_0_17,ent_q_diff_block_0_18,ent_q_diff_block_0_19,ent_q_diff_block_0_20,ent_q_diff_diffs_0_mean,ent_q_diff_diffs_0_var,ent_q_diff_diffs_0_median,ent_q_diff_diffs_0_max,ent_q_diff_diffs_0_min,ent_q_diff_diffs_0_max-min,ent_q_diff_block_1_0,ent_q_diff_block_1_1,ent_q_diff_block_1_2,ent_q_diff_block_1_3,ent_q_diff_block_1_4,ent_q_diff_block_1_5,ent_q_diff_block_1_6,ent_q_diff_block_1_7,ent_q_diff_block_1_8,ent_q_diff_block_1_9,ent_q_diff_block_1_10,ent_q_diff_block_1_11,ent_q_diff_block_1_12,ent_q_diff_block_1_13,ent_q_diff_block_1_14,ent_q_diff_block_1_15,ent_q_diff_block_1_16,ent_q_diff_block_1_17,ent_q_diff_block_1_18,ent_q_diff_block_1_19,ent_q_diff_block_1_20,ent_q_diff_diffs_1_mean,ent_q_diff_diffs_1_var,ent_q_diff_diffs_1_median,ent_q_diff_diffs_1_max,ent_q_diff_diffs_1_min,ent_q_diff_diffs_1_max-min,ent_q_diff_block_2_0,ent_q_diff_block_2_1,ent_q_diff_block_2_2,ent_q_diff_block_2_3,ent_q_diff_block_2_4,ent_q_diff_block_2_5,ent_q_diff_block_2_6,ent_q_diff_block_2_7,ent_q_diff_block_2_8,ent_q_diff_block_2_9,ent_q_diff_block_2_10,ent_q_diff_block_2_11,ent_q_diff_block_2_12,ent_q_diff_block_2_13,ent_q_diff_block_2_14,ent_q_diff_block_2_15,ent_q_diff_block_2_16,ent_q_diff_block_2_17,ent_q_diff_block_2_18,ent_q_diff_block_2_19,ent_q_diff_block_2_20,ent_q_diff_diffs_2_mean,ent_q_diff_diffs_2_var,ent_q_diff_diffs_2_median,ent_q_diff_diffs_2_max,ent_q_diff_diffs_2_min,ent_q_diff_diffs_2_max-min,ent_q_diff_block_3_0,ent_q_diff_block_3_1,ent_q_diff_block_3_2,ent_q_diff_block_3_3,ent_q_diff_block_3_4,ent_q_diff_block_3_5,ent_q_diff_block_3_6,ent_q_diff_block_3_7,ent_q_diff_block_3_8,ent_q_diff_block_3_9,ent_q_diff_block_3_10,ent_q_diff_block_3_11,ent_q_diff_block_3_12,ent_q_diff_block_3_13,ent_q_diff_block_3_14,ent_q_diff_block_3_15,ent_q_diff_block_3_16,ent_q_diff_block_3_17,ent_q_diff_block_3_18,ent_q_diff_block_3_19,ent_q_diff_block_3_20,ent_q_diff_diffs_3_mean,ent_q_diff_diffs_3_var,ent_q_diff_diffs_3_median,ent_q_diff_diffs_3_max,ent_q_diff_diffs_3_min,ent_q_diff_diffs_3_max-min,ent_p_0,ent_p_1,ent_p_2,ent_p_3,ent_p_4,ent_p_5,ent_p_6,ent_p_7,ent_p_8,ent_p_9,ent_p_10,ent_p_11,ent_p_12,ent_p_13,ent_p_14,ent_p_15,ent_p_16,ent_p_17,ent_p_18,ent_p_19,ent_p_diffs_0,ent_p_diffs_1,ent_p_diffs_2,ent_p_diffs_3,ent_p_diffs_4,ent_p_diffs_5,ent_p_diffs_6,ent_p_diffs_7,ent_p_diffs_8,ent_p_diffs_9,ent_p_diffs_10,ent_p_diffs_11,ent_p_diffs_12,ent_p_diffs_13,ent_p_diffs_14,ent_p_diffs_15,ent_p_diffs_16,ent_p_diffs_17,ent_p_diffs_18,ent_p_diffs_19,Entropy,section_names_.bss,section_names_.data,section_names_.edata,section_names_.idata,section_names_.rdata,section_names_.rsrc,section_names_.text,section_names_.tls,section_names_header,Num_Sections,Unknown_Sections,Unknown_Sections_lines,.reloc,known_Sections_por,Unknown_Sections_por,Unknown_Sections_lines_por,.text_por,.data_por,.bss_por,.rdata_por,.edata_por,.idata_por,.rsrc_por,.tls_por,.reloc_por,wcslen,__vbaUI1I2,send,MoveFileExA,VariantCopyInd,__vbaStrI2,DispatchMessageW,WaitForMultipleObjects,CoGetClassObject,IsEqualGUID,GetUserNameA,GetWindowTextLengthA,__vbaErase,WSAStartup,RegCreateKeyExW,__vbaVarSub,GetOpenFileNameA,VirtualProtectEx,IsDBCSLeadByte,SetWindowLongW,time,wvsprintfA,*invalid*,GetDlgCtrlID,__vbaLsetFixstr,CreateWindowExW,__vbaAryVar,__vbaExitProc,__vbaFixstrConstruct,TextOutA,CreateDirectoryW,SuspendThread,DeviceIoControl,GetWindowLongW,GlobalSize,DefWindowProcW,DrawFocusRect,gethostbyname,GetErrorInfo,_strlwr,HttpQueryInfoA,__vbaI2Var,strncmp,PostMessageW,LocalFileTimeToFileTime,InternetConnectA,_cexit,SHGetSpecialFolderPathA,htons,SetCursorPos,DeleteService,CharNextW,FindResourceW,__vbaRedimPreserve,ValidateRect,__vbaBoolVarNull,GetClassLongA,LPtoDP,PeekMessageW,__vbaPutOwner3,socket,closesocket,CreateEventW,memmove,lstrcmpW,ClosePrinter,GetVersionExW,Netbios,CreateServiceA,StringFromCLSID,CLSIDFromProgID,GlobalMemoryStatus,EnumChildWindows,OpenPrinterA,ControlService,IsValidLocale,LoadLibraryExW,GetTimeFormatA,Shell_NotifyIconA,connect,lstrcpyW,DisableThreadLibraryCalls,__vbaStrVarCopy,__vbaInStrVar,wcscmp,SetViewportExtEx,SetWindowExtEx,InitCommonControlsEx,lstrcmpiW,__vbaVarTstNe,wcscpy,ShellExecuteExA,HttpOpenRequestA,RegQueryValueA,HttpSendRequestA,fwrite,__vbaGet3,recv,FormatMessageW,GetStartupInfoW,__vbaVarZero,GlobalGetAtomNameA,__vbaI4ErrVar,FindNextFileW,BringWindowToTop,FreeSid,CreateRectRgn,wsprintfW,__vbaStrFixstr,GetUserDefaultLangID,TranslateAcceleratorA,CreateProcessW,Escape,__vbaVarIndexLoad,RegDeleteValueW,Polyline,SetWindowTextW,LoadCursorW,inet_addr,CreateRemoteThread,GetThreadContext,InternetGetConnectedState,GetTextExtentPointA,UnlockFile,ShellExecuteW,GetSaveFileNameA,GetFileTitleA,EnumSystemLocalesA,GetTempPathW,GetTokenInformation,VerQueryValueW,CreatePipe,GdiFlush,GetWindowTextW,__vbaRecAnsiToUni,__vbaRecUniToAnsi,LockFile,keybd_event,SetServiceStatus,SetFileAttributesW,QueryServiceStatus,GetProcAddress,LoadLibraryA,GetModuleHandleA,ExitProcess,VirtualAlloc,WriteFile,GetModuleFileNameA,CloseHandle,RegCloseKey,VirtualFree,GetLastError,Sleep,CreateFileA,FreeLibrary,GetCommandLineA,MultiByteToWideChar,ReadFile,SetFilePointer,RegQueryValueExA,GetCurrentThreadId,GetTickCount,GetStdHandle,MessageBoxA,GetStartupInfoA,RegOpenKeyExA,GetCurrentProcess,EnterCriticalSection,LeaveCriticalSection,WideCharToMultiByte,DeleteCriticalSection,VirtualProtect,InitializeCriticalSection,LocalAlloc,FindClose,CreateThread,RtlUnwind,lstrlenA,GetDC,UnhandledExceptionFilter,WaitForSingleObject,GetLocaleInfoA,GetFileSize,FindFirstFileA,GetACP,DeleteFileA,GetVersionExA,GetVersion,GetCurrentProcessId,TlsSetValue,TlsGetValue,RaiseException,TerminateProcess,CharNextA,HeapAlloc,LocalFree,GetCPInfo,GetFileType,GlobalAlloc,HeapFree,VirtualQuery,DispatchMessageA,ShowWindow,SetEndOfFile,RegSetValueExA,DestroyWindow,CreateWindowExA,GetSystemMetrics,GlobalFree,InterlockedIncrement,InterlockedDecrement,LoadStringA,GetThreadLocale,SendMessageA,DeleteObject,GetTempPathA,GetClientRect,SelectObject,GetWindowRect,wsprintfA,SetLastError,QueryPerformanceCounter,GetSystemDirectoryA,DefWindowProcA,GlobalLock,GlobalUnlock,TranslateMessage,ShellExecuteA,HeapReAlloc,GetDeviceCaps,SetTimer,LoadCursorA,CreateFontIndirectA,CreateMutexA,GetClassInfoA,SetFocus,CreateCompatibleBitmap,CoTaskMemFree,_initterm,EndDialog,KillTimer,CreatePopupMenu,RegDeleteValueA,GetForegroundWindow,FlushFileBuffers,TrackPopupMenu,GetSystemMenu,FindWindowA,OpenProcess,HeapSize,GetExitCodeProcess,GetClassNameA,DllFunctionCall,GetCursorPos,EVENT_SINK_Release,EVENT_SINK_QueryInterface,GetPrivateProfileStringA,EVENT_SINK_AddRef,_adjust_fdiv,CallNextHookEx,GetMessageA,ImageList_Destroy,SetFileTime,GetObjectA,GetFocus,GetFileVersionInfoA,ImageList_Create,SaveDC,UnhookWindowsHookEx,SetStdHandle,RemoveDirectoryA,MoveFileA,GetFileVersionInfoSizeA,IsIconic,CreateBrushIndirect,EnumWindows,SetWindowsHookExA,CreateSolidBrush,exit,WritePrivateProfileStringA,free,FileTimeToLocalFileTime,InternetOpenA,OpenProcessToken,OleInitialize,GetKeyState,SetCurrentDirectoryA,GetModuleHandleW,OpenClipboard,GetActiveWindow,CloseClipboard,ClientToScreen,SetClassLongA,ExitWindowsEx,UnregisterClassA,FreeResource,RegisterWindowMessageA,GetShortPathNameA,ResetEvent,_except_handler3,malloc,OleUninitialize,GetSubMenu,MapWindowPoints,GetMenu,GetTempFileNameA,RegEnumValueA,EmptyClipboard,GetDIBits,SetCapture,PtInRect,SetClipboardData,InternetCloseHandle,DestroyMenu,FindWindowExA,ReleaseCapture,VariantClear,GetSystemTime,CheckMenuItem,ResumeThread,GetMessagePos,SetRect,CoUninitialize,GetModuleFileNameW,GetCurrentThread,IsDebuggerPresent,InternetReadFile,SetActiveWindow,GetWindowDC,SysAllocStringLen,OffsetRect,DestroyIcon,GetMenuItemCount,DialogBoxParamA,DrawIcon,CreateBitmap,VariantCopy,GetWindowPlacement,GetCapture,memset,lstrlenW,RestoreDC,IsChild,GetEnvironmentVariableA,AdjustWindowRectEx,ExitThread,GetMenuState,SelectPalette,IsBadReadPtr,GlobalDeleteAtom,ImageList_Add,GetLastActivePopup,GetTopWindow,__set_app_type,GetDateFormatA,SysReAllocStringLen,CreateFileW,RealizePalette,GetMenuItemID,InflateRect,SafeArrayPtrOfIndex,_CIcos,GlobalReAlloc,PatBlt,SetViewportOrgEx,UnrealizeObject,GetPixel,SetPropA,_allmul,LineTo,SetDlgItemTextA,GlobalHandle,memcpy,CreateProcessA,IsWindow,RegCreateKeyExA,SetWindowLongA,EnableWindow,GetWindowsDirectoryA,HeapCreate,PostQuitMessage,SetWindowPos,LoadResource,GetFileAttributesA,PeekMessageA,lstrcpynA,GetOEMCP,BeginPaint,EndPaint,SetErrorMode,SysFreeString,GetStringTypeW,lstrcpyA,SizeofResource,CallWindowProcA,IsWindowVisible,SetUnhandledExceptionFilter,LoadLibraryExA,GetWindowLongA,LCMapStringW,LCMapStringA,SetHandleCount,SetForegroundWindow,GetStringTypeA,GetProcessHeap,GetEnvironmentStringsW,GetSysColor,RegisterClassA,CreateDirectoryA,LockResource,FreeEnvironmentStringsA,InvalidateRect,FreeEnvironmentStringsW,InterlockedExchange,FindResourceA,SetTextColor,TlsAlloc,GetEnvironmentStrings,GetSystemTimeAsFileTime,BitBlt,SetCursor,VerQueryValueA,HeapDestroy,lstrcatA,CompareStringA,ReleaseDC,GetFullPathNameA,CoCreateInstance,MulDiv,GetWindowTextA,CopyFileA,FindNextFileA,lstrcmpiA,CreateEventA,FillRect,DeleteDC,SetEvent,GetDesktopWindow,SetBkColor,GetDlgItem,SetFileAttributesA,IsWindowEnabled,SetWindowTextA,SetBkMode,ScreenToClient,GetSystemInfo,TlsFree,GetKeyboardType,SystemParametersInfoA,CreateCompatibleDC,GetParent,EnableMenuItem,PostMessageA,GetDiskFreeSpaceA,LoadIconA,UpdateWindow,GetWindowThreadProcessId,GetLocalTime,lstrcmpA,GetStockObject,LoadBitmapA,GetWindow,FormatMessageA,CoInitialize,RegDeleteKeyA,GetClipBox,IsDialogMessageA,SetMenu,WinExec,_CIsqrt,GetCurrentDirectoryA,IntersectRect,GlobalAddAtomA,_CIsin,MapViewOfFile,StretchBlt,_CIlog,__p__fmode,_CIexp,_CIatan,_adj_fdiv_m64,_CItan,_adj_fdiv_m32,_adj_fprem1,_adj_fptan,_adj_fprem,_adj_fdiv_r,_adj_fdivr_m16i,_adj_fpatan,_adj_fdivr_m64,GetPropA,_adj_fdivr_m32,_adj_fdiv_m32i,_adj_fdivr_m32i,RegEnumKeyA,__vbaFPException,_adj_fdiv_m16i,__vbaChkstk,CompareStringW,GetTimeZoneInformation,AdjustTokenPrivileges,__vbaFreeVar,RectVisible,__getmainargs,sprintf,SHGetSpecialFolderLocation,RedrawWindow,__vbaFreeStr,__vbaHresultCheckObj,WindowFromPoint,EnumCalendarInfoA,RemovePropA,__vbaStrMove,EqualRect,_XcptFilter,__vbaFreeVarList,ExpandEnvironmentStringsA,__vbaFreeStrList,GetSysColorBrush,ImageList_SetIconSize,LoadImageA,GetComputerNameA,UnmapViewOfFile,CreateDIBSection,MoveToEx,__setusermatherr,__vbaNew2,_exit,SetEnvironmentVariableA,DrawEdge,__vbaStrCat,__p__commode,__vbaStrCopy,IsRectEmpty,__vbaFreeObj,SetStretchBltMode,_onexit,IsZoomed,GetIconInfo,CreatePalette,CharLowerA,SHGetPathFromIDListA,GlobalFindAtomA,RegOpenKeyA,CreateDIBitmap,GetKeyboardState,LookupPrivilegeValueA,_controlfp,strstr,GetDlgItemTextA,__vbaStrVarMove,__vbaSetSystemError,DeleteMenu,LoadLibraryW,IsValidCodePage,CharPrevA,GetTextExtentPoint32A,CreateToolhelp32Snapshot,CharToOemA,DestroyCursor,RegisterClipboardFormatA,__vbaOnError,GetStringTypeExA,CreateMenu,DrawIconEx,EnumThreadWindows,SetWindowOrgEx,DrawMenuBar,GetDriveTypeA,WinHelpA,SetScrollPos,SHFileOperationA,VariantInit,FrameRect,__vbaLenBstr,ShowOwnedPopups,__vbaVarDup,__dllonexit,SHGetFileInfoA,atoi,GetScrollPos,AppendMenuA,SetPixel,__vbaVarMove,ExcludeClipRect,strncpy,SetROP2,GetTextMetricsA,GetDCEx,CreateDialogParamA,DrawFrameControl,SetWindowPlacement,__CxxFrameHandler,??2@YAPAXI@Z,MapVirtualKeyA,__vbaErrorOverflow,OemToCharA,WaitMessage,InternetOpenUrlA,GetKeyboardLayout,FileTimeToDosDateTime,RemoveMenu,SafeArrayCreate,__vbaAryDestruct,SetScrollRange,GetVolumeInformationA,__vbaStrCmp,FileTimeToSystemTime,ImageList_Remove,ScrollWindow,SetScrollInfo,RegEnumKeyExA,GetCursor,IntersectClipRect,GetScrollRange,GetClipboardData,GetSystemPaletteEntries,SafeArrayGetUBound,CheckDlgButton,CompareFileTime,GetMenuItemInfoA,CreateIcon,SetThreadLocale,InsertMenuItemA,CreateFileMappingA,SafeArrayGetLBound,ImageList_Draw,InsertMenuA,Process32Next,SHBrowseForFolderA,ReleaseMutex,__vbaStrToAnsi,WriteProcessMemory,SetBrushOrgEx,ShowScrollBar,SendMessageTimeoutA,Process32First,__vbaFileOpen,MsgWaitForMultipleObjects,GetScrollInfo,GetBitmapBits,__vbaFileClose,strlen,GetPaletteEntries,ImageList_DragEnter,MessageBeep,TranslateMDISysAccel,ActivateKeyboardLayout,GetWindowOrgEx,__vbaObjSet,GetMenuStringA,CreateHalftonePalette,GetFileTime,GetDIBColorTable,ImageList_EndDrag,ImageList_GetIconSize,GetCurrentPositionEx,SetDIBColorTable,__vbaVarCat,ImageList_DragLeave,CloseServiceHandle,ImageList_SetBkColor,RegFlushKey,EnableScrollBar,ImageList_DragMove,_acmdln,ImageList_DrawEx,SetParent,__vbaStrVarVal,ImageList_GetImageCount,ImageList_BeginDrag,SearchPathA,GetKeyNameTextA,ImageList_DragShowNolock,ImageList_Read,GetKeyboardLayoutList,MoveWindow,RegOpenKeyExW,__vbaStrToUnicode,GetConsoleCP,CreatePenIndirect,RegQueryValueExW,RegQueryInfoKeyA,DefFrameProcA,GetBrushOrgEx,ImageList_ReplaceIcon,GetUserDefaultLCID,__vbaGenerateBoundsError,strchr,GetConsoleMode,__vbaEnd,SetThreadPriority,GetCommandLineW,DefMDIChildProcA,_stricmp,__vbaI4Var,SetMenuItemInfoA,ImageList_GetBkColor,ImageList_AddMasked,ImageList_Write,MaskBlt,GetDCOrgEx,CharLowerBuffA,RegisterClassExA,ShowCursor,VariantChangeTypeEx,SetMapMode,IsBadWritePtr,DuplicateHandle,URLDownloadToFileA,InitCommonControls,GetConsoleOutputCP,strcpy,WriteConsoleW,ImageList_GetDragImage,VariantChangeType,Rectangle,LoadKeyboardLayoutA,WriteConsoleA,__vbaFreeObjList,__vbaUbound,CoTaskMemAlloc,strrchr,GetExitCodeThread,FindFirstFileW,__vbaAryMove,ProcCallEngine,__vbaAryUnlock,__vbaRedim,TerminateThread,OpenSCManagerA,CopyRect,CreateStreamOnHGlobal,WSACleanup,ImageList_SetDragCursorImage,__vbaInStr,MessageBoxW,fclose,OpenServiceA,CharUpperBuffA,??3@YAXPAX@Z,InitializeCriticalSectionAndSpinCount,rand,MethCallEngine,__vbaI2I4,SystemTimeToFileTime,__vbaAryLock,GetFileAttributesW,ReadProcessMemory,__vbaFpI4,strcat,RegSetValueExW,GetLocaleInfoW,__vbaVar2Vec,VirtualAllocEx,DeleteFileW,GetMessageTime,SendMessageW,__vbaVarTstEq,PostThreadMessageA,CLSIDFromString,fopen,InterlockedCompareExchange,RegCreateKeyA,OutputDebugStringA,strcmp,MessageBoxIndirectA,StartServiceA,PlayEnhMetaFile,SHGetMalloc,DeleteEnhMetaFile,SendDlgItemMessageA,CharUpperA,__vbaAryConstruct2,GetEnhMetaFileHeader,__vbaVarAdd,SetEnhMetaFileBits,__vbaObjSetAddref,GetEnhMetaFileBits,LoadStringW,SetWinMetaFileBits,GetWinMetaFileBits,__vbaVarVargNofree,ExtTextOutA,GetEnhMetaFilePaletteEntries,IsBadCodePtr,OpenMutexA,__vbaStrI4,__vbaVarCopy,CopyEnhMetaFileA,LocalReAlloc,srand,__vbaAryCopy,CreateDCA,TB_00,TB_01,TB_02,TB_03,TB_04,TB_05,TB_06,TB_07,TB_08,TB_09,TB_0a,TB_0b,TB_0c,TB_0d,TB_0e,TB_0f,TB_10,TB_11,TB_12,TB_13,TB_14,TB_15,TB_16,TB_17,TB_18,TB_19,TB_1a,TB_1b,TB_1c,TB_1d,TB_1e,TB_1f,TB_20,TB_21,TB_22,TB_23,TB_24,TB_25,TB_26,TB_27,TB_28,TB_29,TB_2a,TB_2b,TB_2c,TB_2d,TB_2e,TB_2f,TB_30,TB_31,TB_32,TB_33,TB_34,TB_35,TB_36,TB_37,TB_38,TB_39,TB_3a,TB_3b,TB_3c,TB_3d,TB_3e,TB_3f,TB_40,TB_41,TB_42,TB_43,TB_44,TB_45,TB_46,TB_47,TB_48,TB_49,TB_4a,TB_4b,TB_4c,TB_4d,TB_4e,TB_4f,TB_50,TB_51,TB_52,TB_53,TB_54,TB_55,TB_56,TB_57,TB_58,TB_59,TB_5a,TB_5b,TB_5c,TB_5d,TB_5e,TB_5f,TB_60,TB_61,TB_62,TB_63,TB_64,TB_65,TB_66,TB_67,TB_68,TB_69,TB_6a,TB_6b,TB_6c,TB_6d,TB_6e,TB_6f,TB_70,TB_71,TB_72,TB_73,TB_74,TB_75,TB_76,TB_77,TB_78,TB_79,TB_7a,TB_7b,TB_7c,TB_7d,TB_7e,TB_7f,TB_80,TB_81,TB_82,TB_83,TB_84,TB_85,TB_86,TB_87,TB_88,TB_89,TB_8a,TB_8b,TB_8c,TB_8d,TB_8e,TB_8f,TB_90,TB_91,TB_92,TB_93,TB_94,TB_95,TB_96,TB_97,TB_98,TB_99,TB_9a,TB_9b,TB_9c,TB_9d,TB_9e,TB_9f,TB_a0,TB_a1,TB_a2,TB_a3,TB_a4,TB_a5,TB_a6,TB_a7,TB_a8,TB_a9,TB_aa,TB_ab,TB_ac,TB_ad,TB_ae,TB_af,TB_b0,TB_b1,TB_b2,TB_b3,TB_b4,TB_b5,TB_b6,TB_b7,TB_b8,TB_b9,TB_ba,TB_bb,TB_bc,TB_bd,TB_be,TB_bf,TB_c0,TB_c1,TB_c2,TB_c3,TB_c4,TB_c5,TB_c6,TB_c7,TB_c8,TB_c9,TB_ca,TB_cb,TB_cc,TB_cd,TB_ce,TB_cf,TB_d0,TB_d1,TB_d2,TB_d3,TB_d4,TB_d5,TB_d6,TB_d7,TB_d8,TB_d9,TB_da,TB_db,TB_dc,TB_dd,TB_de,TB_df,TB_e0,TB_e1,TB_e2,TB_e3,TB_e4,TB_e5,TB_e6,TB_e7,TB_e8,TB_e9,TB_ea,TB_eb,TB_ec,TB_ed,TB_ee,TB_ef,TB_f0,TB_f1,TB_f2,TB_f3,TB_f4,TB_f5,TB_f6,TB_f7,TB_f8,TB_f9,TB_fa,TB_fb,TB_fc,TB_fd,TB_fe,TB_ff,edx,esi,es,fs,ds,ss,gs,cs,regs_ah,regs_al,regs_ax,regs_bh,regs_bl,regs_bx,regs_ch,regs_cl,regs_cx,regs_dh,regs_dl,regs_dx,regs_eax,regs_ebp,regs_ebx,regs_ecx,regs_edi,regs_esp,asm_commands_add,asm_commands_call,asm_commands_cdq,asm_commands_cld,asm_commands_cli,asm_commands_cmc,asm_commands_cmp,asm_commands_cwd,asm_commands_daa,asm_commands_dd,asm_commands_dec,asm_commands_dw,asm_commands_endp,asm_commands_faddp,asm_commands_fchs,asm_commands_fdiv,asm_commands_fdivr,asm_commands_fistp,asm_commands_fld,asm_commands_fstp,asm_commands_fword,asm_commands_fxch,asm_commands_imul,asm_commands_in,asm_commands_inc,asm_commands_ins,asm_commands_jb,asm_commands_je,asm_commands_jg,asm_commands_jl,asm_commands_jmp,asm_commands_jnb,asm_commands_jno,asm_commands_jo,asm_commands_jz,asm_commands_lea,asm_commands_mov,asm_commands_mul,asm_commands_not,asm_commands_or,asm_commands_out,asm_commands_outs,asm_commands_pop,asm_commands_push,asm_commands_rcl,asm_commands_rcr,asm_commands_rep,asm_commands_ret,asm_commands_rol,asm_commands_ror,asm_commands_sal,asm_commands_sar,asm_commands_sbb,asm_commands_scas,asm_commands_shl,asm_commands_shr,asm_commands_sidt,asm_commands_stc,asm_commands_std,asm_commands_sti,asm_commands_stos,asm_commands_sub,asm_commands_test,asm_commands_wait,asm_commands_xchg,asm_commands_xor,fstcw,imul,proc,const,setnle,popf,loope,bt,fild,fdivp,fstcwimul,int,jnz,rdtsc,retn,setb,setle,shld,pushf,al,near,neg,movzx,ends,setz,jge,setnz,FileSize,Offset,db_por,dd_por,dw_por,dc_por,db0_por,dbN0_por,dd_text,db_text,dd_rdata,db3_rdata,db3_data,db3_all,dd4,dd5,dd6,dd4_all,dd5_all,dd6_all,db3_idata,db3_NdNt,dd4_NdNt,dd5_NdNt,dd6_NdNt,db3_all_zero,string_len_counts_1,string_len_counts_2,string_len_counts_3,string_len_counts_4,string_len_counts_5,string_len_counts_6,string_len_counts_7,string_len_counts_8,string_len_counts_9,string_len_counts_10,string_len_counts_11,string_len_counts_12,string_len_counts_13,string_len_counts_14,string_len_counts_15,string_len_counts_16,string_len_counts_17,string_len_counts_18,string_len_counts_19,string_len_counts_20,string_len_counts_21,string_len_counts_22,string_len_counts_23,string_len_counts_24,string_len_counts_25,string_len_counts_26,string_len_counts_27,string_len_counts_28,string_len_counts_29,string_len_counts_30,string_len_counts_31,string_len_counts_32,string_len_counts_33,string_len_counts_34,string_len_counts_35,string_len_counts_36,string_len_counts_37,string_len_counts_38,string_len_counts_39,string_len_counts_40,string_len_counts_41,string_len_counts_42,string_len_counts_43,string_len_counts_44,string_len_counts_45,string_len_counts_46,string_len_counts_47,string_len_counts_48,string_len_counts_49,string_len_counts_50,string_len_counts_51,string_len_counts_52,string_len_counts_53,string_len_counts_54,string_len_counts_55,string_len_counts_56,string_len_counts_57,string_len_counts_58,string_len_counts_59,string_len_counts_60,string_len_counts_61,string_len_counts_62,string_len_counts_63,string_len_counts_64,string_len_counts_65,string_len_counts_66,string_len_counts_67,string_len_counts_68,string_len_counts_69,string_len_counts_70,string_len_counts_71,string_len_counts_72,string_len_counts_73,string_len_counts_74,string_len_counts_75,string_len_counts_76,string_len_counts_77,string_len_counts_78,string_len_counts_79,string_len_counts_80,string_len_counts_81,string_len_counts_82,string_len_counts_83,string_len_counts_84,string_len_counts_85,string_len_counts_86,string_len_counts_87,string_len_counts_88,string_len_counts_89,string_len_counts_90,string_len_counts_91,string_len_counts_92,string_len_counts_93,string_len_counts_94,string_len_counts_95,string_len_counts_96,string_len_counts_97,string_len_counts_98,string_len_counts_99,string_len_counts_0_10,string_len_counts_10_30,string_len_counts_30_60,string_len_counts_60_90,string_len_counts_0_100,string_len_counts_100_150,string_len_counts_150_250,string_len_counts_250_400,string_len_counts_400_600,string_len_counts_600_900,string_len_counts_900_1300,string_len_counts_1300_2000,string_len_counts_2000_3000,string_len_counts_3000_6000,string_len_counts_6000_15000,string_total_len,string_ratio,Img0,Img1,Img2,Img3,Img4,Img5,Img6,Img7,Img8,Img9,Img10,Img11,Img12,Img13,Img14,Img15,Img16,Img17,Img18,Img19,Img20,Img21,Img22,Img23,Img24,Img25,Img26,Img27,Img28,Img29,Img30,Img31,Img32,Img33,Img34,Img35,Img36,Img37,Img38,Img39,Img40,Img41,Img42,Img43,Img44,Img45,Img46,Img47,Img48,Img49,Img50,Img51,line_count_asm,size_asm,Star,Dash,Plus,Bracket_Open,Bracket_Close,AtSign,Question,ExtendedAscii,Img0,Img1,Img2,Img3,Img4,Img5,Img6,Img7,Img8,Img9,Img10,Img11,Img12,Img13,Img14,Img15,Img16,Img17,Img18,Img19,Img20,Img21,Img22,Img23,Img24,Img25,Img26,Img27,Img28,Img29,Img30,Img31,Img32,Img33,Img34,Img35,Img36,Img37,Img38,Img39,Img40,Img41,Img42,Img43,Img44,Img45,Img46,Img47,Img48,Img49,Img50,Img51,Img52,Img53,Img54,Img55,Img56,Img57,Img58,Img59,Img60,Img61,Img62,Img63,Img64,Img65,Img66,Img67,Img68,Img69,Img70,Img71,Img72,Img73,Img74,Img75,Img76,Img77,Img78,Img79,Img80,Img81,Img82,Img83,Img84,Img85,Img86,Img87,Img88,Img89,Img90,Img91,Img92,Img93,Img94,Img95,Img96,Img97,Img98,Img99,Img100,Img101,Img102,Img103,Img104,Img105,Img106,Img107,Class































