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
import win32more.Windows.Perception
class IPerceptionTimestamp(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.IPerceptionTimestamp'
    _iid_ = Guid('{87c24804-a22e-4adb-ba26-d78ef639bcf4}')
    @winrt_commethod(6)
    def get_TargetTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_PredictionAmount(self) -> win32more.Windows.Foundation.TimeSpan: ...
    TargetTime = property(get_TargetTime, None)
    PredictionAmount = property(get_PredictionAmount, None)
class IPerceptionTimestamp2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.IPerceptionTimestamp2'
    _iid_ = Guid('{e354b7ed-2bd1-41b7-9ed0-74a15c354537}')
    @winrt_commethod(6)
    def get_SystemRelativeTargetTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    SystemRelativeTargetTime = property(get_SystemRelativeTargetTime, None)
class IPerceptionTimestampHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.IPerceptionTimestampHelperStatics'
    _iid_ = Guid('{47a611d4-a9df-4edc-855d-f4d339d967ac}')
    @winrt_commethod(6)
    def FromHistoricalTargetTime(self, targetTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Perception.PerceptionTimestamp: ...
class IPerceptionTimestampHelperStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.IPerceptionTimestampHelperStatics2'
    _iid_ = Guid('{73d1a7fe-3fb9-4571-87d4-3c920a5e86eb}')
    @winrt_commethod(6)
    def FromSystemRelativeTargetTime(self, targetTime: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Perception.PerceptionTimestamp: ...
class PerceptionTimestamp(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Perception.IPerceptionTimestamp
    _classid_ = 'Windows.Perception.PerceptionTimestamp'
    @winrt_mixinmethod
    def get_TargetTime(self: win32more.Windows.Perception.IPerceptionTimestamp) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_PredictionAmount(self: win32more.Windows.Perception.IPerceptionTimestamp) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_SystemRelativeTargetTime(self: win32more.Windows.Perception.IPerceptionTimestamp2) -> win32more.Windows.Foundation.TimeSpan: ...
    TargetTime = property(get_TargetTime, None)
    PredictionAmount = property(get_PredictionAmount, None)
    SystemRelativeTargetTime = property(get_SystemRelativeTargetTime, None)
class PerceptionTimestampHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.PerceptionTimestampHelper'
    @winrt_classmethod
    def FromSystemRelativeTargetTime(cls: win32more.Windows.Perception.IPerceptionTimestampHelperStatics2, targetTime: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Perception.PerceptionTimestamp: ...
    @winrt_classmethod
    def FromHistoricalTargetTime(cls: win32more.Windows.Perception.IPerceptionTimestampHelperStatics, targetTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Perception.PerceptionTimestamp: ...
make_ready(__name__)
