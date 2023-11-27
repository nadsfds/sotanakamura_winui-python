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
import win32more.Windows.ApplicationModel.Core
import win32more.Windows.System
import win32more.Windows.UI.Core
import win32more.Windows.UI.Input
import win32more.Windows.UI.Input.Core
class IRadialControllerIndependentInputSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Core.IRadialControllerIndependentInputSource'
    _iid_ = Guid('{3d577ef6-4cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_Controller(self) -> win32more.Windows.UI.Input.RadialController: ...
    @winrt_commethod(7)
    def get_Dispatcher(self) -> win32more.Windows.UI.Core.CoreDispatcher: ...
    Controller = property(get_Controller, None)
    Dispatcher = property(get_Dispatcher, None)
class IRadialControllerIndependentInputSource2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Core.IRadialControllerIndependentInputSource2'
    _iid_ = Guid('{7073aad8-35f3-4eeb-8751-be4d0a66faf4}')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> win32more.Windows.System.DispatcherQueue: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class IRadialControllerIndependentInputSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Core.IRadialControllerIndependentInputSourceStatics'
    _iid_ = Guid('{3d577ef5-4cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def CreateForView(self, view: win32more.Windows.ApplicationModel.Core.CoreApplicationView) -> win32more.Windows.UI.Input.Core.RadialControllerIndependentInputSource: ...
class RadialControllerIndependentInputSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Core.IRadialControllerIndependentInputSource
    _classid_ = 'Windows.UI.Input.Core.RadialControllerIndependentInputSource'
    @winrt_mixinmethod
    def get_Controller(self: win32more.Windows.UI.Input.Core.IRadialControllerIndependentInputSource) -> win32more.Windows.UI.Input.RadialController: ...
    @winrt_mixinmethod
    def get_Dispatcher(self: win32more.Windows.UI.Input.Core.IRadialControllerIndependentInputSource) -> win32more.Windows.UI.Core.CoreDispatcher: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: win32more.Windows.UI.Input.Core.IRadialControllerIndependentInputSource2) -> win32more.Windows.System.DispatcherQueue: ...
    @winrt_classmethod
    def CreateForView(cls: win32more.Windows.UI.Input.Core.IRadialControllerIndependentInputSourceStatics, view: win32more.Windows.ApplicationModel.Core.CoreApplicationView) -> win32more.Windows.UI.Input.Core.RadialControllerIndependentInputSource: ...
    Controller = property(get_Controller, None)
    Dispatcher = property(get_Dispatcher, None)
    DispatcherQueue = property(get_DispatcherQueue, None)
make_ready(__name__)
