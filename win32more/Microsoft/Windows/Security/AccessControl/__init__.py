from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.Security.AccessControl
import win32more.Windows.Win32.System.WinRT
AccessControlContract: UInt32 = 65536
class AppContainerNameAndAccess(EasyCastStructure):
    appContainerName: WinRT_String
    accessMask: UInt32
class ISecurityDescriptorHelpersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Security.AccessControl.ISecurityDescriptorHelpersStatics'
    _iid_ = Guid('{14fa9e8d-59f0-5017-852f-3ae24fd5ebb1}')
    @winrt_commethod(6)
    def GetSddlForAppContainerNames(self, accessRequests: Annotated[SZArray[win32more.Microsoft.Windows.Security.AccessControl.AppContainerNameAndAccess], 'In'], principalStringSid: WinRT_String, principalAccessMask: UInt32) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetSecurityDescriptorBytesFromAppContainerNames(self, accessRequests: Annotated[SZArray[win32more.Microsoft.Windows.Security.AccessControl.AppContainerNameAndAccess], 'In'], principalStringSid: WinRT_String, principalAccessMask: UInt32) -> SZArray[Byte]: ...
class SecurityDescriptorHelpers(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Security.AccessControl.SecurityDescriptorHelpers'
    @winrt_classmethod
    def GetSddlForAppContainerNames(cls: win32more.Microsoft.Windows.Security.AccessControl.ISecurityDescriptorHelpersStatics, accessRequests: Annotated[SZArray[win32more.Microsoft.Windows.Security.AccessControl.AppContainerNameAndAccess], 'In'], principalStringSid: WinRT_String, principalAccessMask: UInt32) -> WinRT_String: ...
    @winrt_classmethod
    def GetSecurityDescriptorBytesFromAppContainerNames(cls: win32more.Microsoft.Windows.Security.AccessControl.ISecurityDescriptorHelpersStatics, accessRequests: Annotated[SZArray[win32more.Microsoft.Windows.Security.AccessControl.AppContainerNameAndAccess], 'In'], principalStringSid: WinRT_String, principalAccessMask: UInt32) -> SZArray[Byte]: ...


make_ready(__name__)
