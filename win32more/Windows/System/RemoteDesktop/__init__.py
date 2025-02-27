from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.System.RemoteDesktop
import win32more.Windows.Win32.System.WinRT
class IInteractiveSessionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.IInteractiveSessionStatics'
    _iid_ = Guid('{60884631-dd3a-4576-9c8d-e8027618bdce}')
    @winrt_commethod(6)
    def get_IsRemote(self) -> Boolean: ...
    IsRemote = property(get_IsRemote, None)
class _InteractiveSession_Meta_(ComPtr.__class__):
    pass
class InteractiveSession(ComPtr, metaclass=_InteractiveSession_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.InteractiveSession'
    @winrt_classmethod
    def get_IsRemote(cls: win32more.Windows.System.RemoteDesktop.IInteractiveSessionStatics) -> Boolean: ...
    _InteractiveSession_Meta_.IsRemote = property(get_IsRemote.__wrapped__, None)


make_ready(__name__)
