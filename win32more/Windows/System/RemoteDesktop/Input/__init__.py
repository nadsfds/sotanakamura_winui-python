from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.System.RemoteDesktop.Input
class IRemoteTextConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.Input.IRemoteTextConnection'
    _iid_ = Guid('{4e7bb02a-183e-5e66-b5e4-3e6e5c570cf1}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def RegisterThread(self, threadId: UInt32) -> Void: ...
    @winrt_commethod(9)
    def UnregisterThread(self, threadId: UInt32) -> Void: ...
    @winrt_commethod(10)
    def ReportDataReceived(self, pduData: Annotated[SZArray[Byte], 'In']) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class IRemoteTextConnectionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.Input.IRemoteTextConnectionFactory'
    _iid_ = Guid('{88e075c2-0cae-596c-850f-78d345cd728b}')
    @winrt_commethod(6)
    def CreateInstance(self, connectionId: Guid, pduForwarder: win32more.Windows.System.RemoteDesktop.Input.RemoteTextConnectionDataHandler) -> win32more.Windows.System.RemoteDesktop.Input.RemoteTextConnection: ...
class RemoteTextConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteDesktop.Input.IRemoteTextConnection
    _classid_ = 'Windows.System.RemoteDesktop.Input.RemoteTextConnection'
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.System.RemoteDesktop.Input.IRemoteTextConnectionFactory, connectionId: Guid, pduForwarder: win32more.Windows.System.RemoteDesktop.Input.RemoteTextConnectionDataHandler) -> win32more.Windows.System.RemoteDesktop.Input.RemoteTextConnection: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.System.RemoteDesktop.Input.IRemoteTextConnection) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.System.RemoteDesktop.Input.IRemoteTextConnection, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def RegisterThread(self: win32more.Windows.System.RemoteDesktop.Input.IRemoteTextConnection, threadId: UInt32) -> Void: ...
    @winrt_mixinmethod
    def UnregisterThread(self: win32more.Windows.System.RemoteDesktop.Input.IRemoteTextConnection, threadId: UInt32) -> Void: ...
    @winrt_mixinmethod
    def ReportDataReceived(self: win32more.Windows.System.RemoteDesktop.Input.IRemoteTextConnection, pduData: Annotated[SZArray[Byte], 'In']) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class RemoteTextConnectionDataHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{099ffbc8-8bcb-41b5-b056-57e77021bf1b}')
    def Invoke(self, pduData: Annotated[SZArray[Byte], 'In']) -> Boolean: ...
make_ready(__name__)
