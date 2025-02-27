from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Diagnostics.Debug
import win32more.Windows.Win32.System.Kernel
OBJ_HANDLE_TAGBITS: Int32 = 3
RTL_BALANCED_NODE_RESERVED_PARENT_MASK: UInt32 = 3
OBJ_INHERIT: Int32 = 2
OBJ_PERMANENT: Int32 = 16
OBJ_EXCLUSIVE: Int32 = 32
OBJ_CASE_INSENSITIVE: Int32 = 64
OBJ_OPENIF: Int32 = 128
OBJ_OPENLINK: Int32 = 256
OBJ_KERNEL_HANDLE: Int32 = 512
OBJ_FORCE_ACCESS_CHECK: Int32 = 1024
OBJ_IGNORE_IMPERSONATED_DEVICEMAP: Int32 = 2048
OBJ_DONT_REPARSE: Int32 = 4096
OBJ_VALID_ATTRIBUTES: Int32 = 8178
NULL64: UInt32 = 0
MAXUCHAR: UInt32 = 255
MAXUSHORT: UInt32 = 65535
MAXULONG: UInt32 = 4294967295
@winfunctype('ntdll.dll')
def RtlInitializeSListHead(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER)) -> Void: ...
@winfunctype('ntdll.dll')
def RtlFirstEntrySList(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER)) -> POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY): ...
@winfunctype('ntdll.dll')
def RtlInterlockedPopEntrySList(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER)) -> POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY): ...
@winfunctype('ntdll.dll')
def RtlInterlockedPushEntrySList(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER), ListEntry: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY)) -> POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY): ...
@winfunctype('ntdll.dll')
def RtlInterlockedPushListSListEx(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER), List: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY), ListEnd: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY), Count: UInt32) -> POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY): ...
@winfunctype('ntdll.dll')
def RtlInterlockedFlushSList(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER)) -> POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY): ...
@winfunctype('ntdll.dll')
def RtlQueryDepthSList(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER)) -> UInt16: ...
COMPARTMENT_ID = Int32
UNSPECIFIED_COMPARTMENT_ID: win32more.Windows.Win32.System.Kernel.COMPARTMENT_ID = 0
DEFAULT_COMPARTMENT_ID: win32more.Windows.Win32.System.Kernel.COMPARTMENT_ID = 1
class CSTRING(EasyCastStructure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: win32more.Windows.Win32.Foundation.PSTR
EVENT_TYPE = Int32
NotificationEvent: win32more.Windows.Win32.System.Kernel.EVENT_TYPE = 0
SynchronizationEvent: win32more.Windows.Win32.System.Kernel.EVENT_TYPE = 1
EXCEPTION_DISPOSITION = Int32
ExceptionContinueExecution: win32more.Windows.Win32.System.Kernel.EXCEPTION_DISPOSITION = 0
ExceptionContinueSearch: win32more.Windows.Win32.System.Kernel.EXCEPTION_DISPOSITION = 1
ExceptionNestedException: win32more.Windows.Win32.System.Kernel.EXCEPTION_DISPOSITION = 2
ExceptionCollidedUnwind: win32more.Windows.Win32.System.Kernel.EXCEPTION_DISPOSITION = 3
class EXCEPTION_REGISTRATION_RECORD(EasyCastStructure):
    Next: POINTER(win32more.Windows.Win32.System.Kernel.EXCEPTION_REGISTRATION_RECORD)
    Handler: win32more.Windows.Win32.System.Kernel.EXCEPTION_ROUTINE
@winfunctype_pointer
def EXCEPTION_ROUTINE(ExceptionRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD), EstablisherFrame: VoidPtr, ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT), DispatcherContext: VoidPtr) -> win32more.Windows.Win32.System.Kernel.EXCEPTION_DISPOSITION: ...
if ARCH in 'X64,ARM64':
    class FLOATING_SAVE_AREA(EasyCastStructure):
        ControlWord: UInt32
        StatusWord: UInt32
        TagWord: UInt32
        ErrorOffset: UInt32
        ErrorSelector: UInt32
        DataOffset: UInt32
        DataSelector: UInt32
        RegisterArea: Byte * 80
        Cr0NpxState: UInt32
elif ARCH in 'X86':
    class FLOATING_SAVE_AREA(EasyCastStructure):
        ControlWord: UInt32
        StatusWord: UInt32
        TagWord: UInt32
        ErrorOffset: UInt32
        ErrorSelector: UInt32
        DataOffset: UInt32
        DataSelector: UInt32
        RegisterArea: Byte * 80
        Spare0: UInt32
class LIST_ENTRY(EasyCastStructure):
    Flink: POINTER(win32more.Windows.Win32.System.Kernel.LIST_ENTRY)
    Blink: POINTER(win32more.Windows.Win32.System.Kernel.LIST_ENTRY)
class LIST_ENTRY32(EasyCastStructure):
    Flink: UInt32
    Blink: UInt32
class LIST_ENTRY64(EasyCastStructure):
    Flink: UInt64
    Blink: UInt64
NT_PRODUCT_TYPE = Int32
NtProductWinNt: win32more.Windows.Win32.System.Kernel.NT_PRODUCT_TYPE = 1
NtProductLanManNt: win32more.Windows.Win32.System.Kernel.NT_PRODUCT_TYPE = 2
NtProductServer: win32more.Windows.Win32.System.Kernel.NT_PRODUCT_TYPE = 3
class NT_TIB(EasyCastStructure):
    ExceptionList: POINTER(win32more.Windows.Win32.System.Kernel.EXCEPTION_REGISTRATION_RECORD)
    StackBase: VoidPtr
    StackLimit: VoidPtr
    SubSystemTib: VoidPtr
    Anonymous: _Anonymous_e__Union
    ArbitraryUserPointer: VoidPtr
    Self: POINTER(win32more.Windows.Win32.System.Kernel.NT_TIB)
    class _Anonymous_e__Union(EasyCastUnion):
        FiberData: VoidPtr
        Version: UInt32
class OBJECTID(EasyCastStructure):
    Lineage: Guid
    Uniquifier: UInt32
class PROCESSOR_NUMBER(EasyCastStructure):
    Group: UInt16
    Number: Byte
    Reserved: Byte
class QUAD(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        UseThisFieldToCopy: Int64
        DoNotUseThisField: Double
class RTL_BALANCED_NODE(EasyCastStructure):
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Union(EasyCastUnion):
        Children: POINTER(win32more.Windows.Win32.System.Kernel.RTL_BALANCED_NODE) * 2
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            Left: POINTER(win32more.Windows.Win32.System.Kernel.RTL_BALANCED_NODE)
            Right: POINTER(win32more.Windows.Win32.System.Kernel.RTL_BALANCED_NODE)
    class _Anonymous2_e__Union(EasyCastUnion):
        _bitfield: Byte
        ParentValue: UIntPtr
class SINGLE_LIST_ENTRY(EasyCastStructure):
    Next: POINTER(win32more.Windows.Win32.System.Kernel.SINGLE_LIST_ENTRY)
class SINGLE_LIST_ENTRY32(EasyCastStructure):
    Next: UInt32
class SLIST_ENTRY(EasyCastStructure):
    Next: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY)
if ARCH in 'ARM64':
    class SLIST_HEADER(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        HeaderArm64: _HeaderArm64_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            Alignment: UInt64
            Region: UInt64
        class _HeaderArm64_e__Struct(EasyCastStructure):
            _bitfield1: UInt64
            _bitfield2: UInt64
elif ARCH in 'X64':
    class SLIST_HEADER(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        HeaderX64: _HeaderX64_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            Alignment: UInt64
            Region: UInt64
        class _HeaderX64_e__Struct(EasyCastStructure):
            _bitfield1: UInt64
            _bitfield2: UInt64
elif ARCH in 'X86':
    class SLIST_HEADER(EasyCastUnion):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            Next: win32more.Windows.Win32.System.Kernel.SINGLE_LIST_ENTRY
            Depth: UInt16
            CpuId: UInt16
class STRING(EasyCastStructure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: win32more.Windows.Win32.Foundation.PSTR
class STRING32(EasyCastStructure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: UInt32
class STRING64(EasyCastStructure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: UInt64
SUITE_TYPE = Int32
SmallBusiness: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 0
Enterprise: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 1
BackOffice: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 2
CommunicationServer: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 3
TerminalServer: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 4
SmallBusinessRestricted: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 5
EmbeddedNT: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 6
DataCenter: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 7
SingleUserTS: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 8
Personal: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 9
Blade: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 10
EmbeddedRestricted: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 11
SecurityAppliance: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 12
StorageServer: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 13
ComputeServer: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 14
WHServer: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 15
PhoneNT: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 16
MultiUserTS: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 17
MaxSuiteType: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 18
TIMER_TYPE = Int32
NotificationTimer: win32more.Windows.Win32.System.Kernel.TIMER_TYPE = 0
SynchronizationTimer: win32more.Windows.Win32.System.Kernel.TIMER_TYPE = 1
WAIT_TYPE = Int32
WaitAll: win32more.Windows.Win32.System.Kernel.WAIT_TYPE = 0
WaitAny: win32more.Windows.Win32.System.Kernel.WAIT_TYPE = 1
WaitNotification: win32more.Windows.Win32.System.Kernel.WAIT_TYPE = 2
WaitDequeue: win32more.Windows.Win32.System.Kernel.WAIT_TYPE = 3
WaitDpc: win32more.Windows.Win32.System.Kernel.WAIT_TYPE = 4
class WNF_STATE_NAME(EasyCastStructure):
    Data: UInt32 * 2


make_ready(__name__)
