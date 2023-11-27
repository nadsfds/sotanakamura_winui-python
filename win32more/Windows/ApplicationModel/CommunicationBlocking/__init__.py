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
import win32more.Windows.ApplicationModel.CommunicationBlocking
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
class _CommunicationBlockingAccessManager_Meta_(ComPtr.__class__):
    pass
class CommunicationBlockingAccessManager(ComPtr, metaclass=_CommunicationBlockingAccessManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.CommunicationBlocking.CommunicationBlockingAccessManager'
    @winrt_classmethod
    def get_IsBlockingActive(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def IsBlockedNumberAsync(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics, number: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def ShowBlockNumbersUI(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics, phoneNumbers: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
    @winrt_classmethod
    def ShowUnblockNumbersUI(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics, phoneNumbers: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
    @winrt_classmethod
    def ShowBlockedCallsUI(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics) -> Void: ...
    @winrt_classmethod
    def ShowBlockedMessagesUI(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics) -> Void: ...
    _CommunicationBlockingAccessManager_Meta_.IsBlockingActive = property(get_IsBlockingActive.__wrapped__, None)
class _CommunicationBlockingAppManager_Meta_(ComPtr.__class__):
    pass
class CommunicationBlockingAppManager(ComPtr, metaclass=_CommunicationBlockingAppManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.CommunicationBlocking.CommunicationBlockingAppManager'
    @winrt_classmethod
    def RequestSetAsActiveBlockingAppAsync(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAppManagerStatics2) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_IsCurrentAppActiveBlockingApp(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAppManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def ShowCommunicationBlockingSettingsUI(cls: win32more.Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAppManagerStatics) -> Void: ...
    _CommunicationBlockingAppManager_Meta_.IsCurrentAppActiveBlockingApp = property(get_IsCurrentAppActiveBlockingApp.__wrapped__, None)
CommunicationBlockingContract: UInt32 = 131072
class ICommunicationBlockingAccessManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAccessManagerStatics'
    _iid_ = Guid('{1c969998-9d2a-5db7-edd5-0ce407fc2595}')
    @winrt_commethod(6)
    def get_IsBlockingActive(self) -> Boolean: ...
    @winrt_commethod(7)
    def IsBlockedNumberAsync(self, number: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def ShowBlockNumbersUI(self, phoneNumbers: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
    @winrt_commethod(9)
    def ShowUnblockNumbersUI(self, phoneNumbers: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
    @winrt_commethod(10)
    def ShowBlockedCallsUI(self) -> Void: ...
    @winrt_commethod(11)
    def ShowBlockedMessagesUI(self) -> Void: ...
    IsBlockingActive = property(get_IsBlockingActive, None)
class ICommunicationBlockingAppManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAppManagerStatics'
    _iid_ = Guid('{77db58ec-14a6-4baa-942a-6a673d999bf2}')
    @winrt_commethod(6)
    def get_IsCurrentAppActiveBlockingApp(self) -> Boolean: ...
    @winrt_commethod(7)
    def ShowCommunicationBlockingSettingsUI(self) -> Void: ...
    IsCurrentAppActiveBlockingApp = property(get_IsCurrentAppActiveBlockingApp, None)
class ICommunicationBlockingAppManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.CommunicationBlocking.ICommunicationBlockingAppManagerStatics2'
    _iid_ = Guid('{14a68edd-ed88-457a-a364-a3634d6f166d}')
    @winrt_commethod(6)
    def RequestSetAsActiveBlockingAppAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
make_ready(__name__)
