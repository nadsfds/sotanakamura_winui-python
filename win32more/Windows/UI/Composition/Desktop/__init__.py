from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Composition.Desktop
import win32more.Windows.Win32.System.WinRT
class DesktopWindowTarget(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionTarget
    default_interface: win32more.Windows.UI.Composition.Desktop.IDesktopWindowTarget
    _classid_ = 'Windows.UI.Composition.Desktop.DesktopWindowTarget'
    @winrt_mixinmethod
    def get_IsTopmost(self: win32more.Windows.UI.Composition.Desktop.IDesktopWindowTarget) -> Boolean: ...
    IsTopmost = property(get_IsTopmost, None)
class IDesktopWindowTarget(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Desktop.IDesktopWindowTarget'
    _iid_ = Guid('{6329d6ca-3366-490e-9db3-25312929ac51}')
    @winrt_commethod(6)
    def get_IsTopmost(self) -> Boolean: ...
    IsTopmost = property(get_IsTopmost, None)


make_ready(__name__)
