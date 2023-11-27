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
import win32more.Windows.Media
import win32more.Windows.Media.Core.Preview
class ISoundLevelBrokerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.Preview.ISoundLevelBrokerStatics'
    _iid_ = Guid('{6a633961-dbed-464c-a09a-33412f5caa3f}')
    @winrt_commethod(6)
    def get_SoundLevel(self) -> win32more.Windows.Media.SoundLevel: ...
    @winrt_commethod(7)
    def add_SoundLevelChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_SoundLevelChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    SoundLevel = property(get_SoundLevel, None)
class _SoundLevelBroker_Meta_(ComPtr.__class__):
    pass
class SoundLevelBroker(ComPtr, metaclass=_SoundLevelBroker_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.Preview.SoundLevelBroker'
    @winrt_classmethod
    def get_SoundLevel(cls: win32more.Windows.Media.Core.Preview.ISoundLevelBrokerStatics) -> win32more.Windows.Media.SoundLevel: ...
    @winrt_classmethod
    def add_SoundLevelChanged(cls: win32more.Windows.Media.Core.Preview.ISoundLevelBrokerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_SoundLevelChanged(cls: win32more.Windows.Media.Core.Preview.ISoundLevelBrokerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    _SoundLevelBroker_Meta_.SoundLevel = property(get_SoundLevel.__wrapped__, None)
make_ready(__name__)
