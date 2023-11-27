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
import win32more.Windows.Devices.Pwm
import win32more.Windows.Devices.Pwm.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
class IPwmController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Pwm.IPwmController'
    _iid_ = Guid('{c45f5c85-d2e8-42cf-9bd6-cf5ed029e6a7}')
    @winrt_commethod(6)
    def get_PinCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_ActualFrequency(self) -> Double: ...
    @winrt_commethod(8)
    def SetDesiredFrequency(self, desiredFrequency: Double) -> Double: ...
    @winrt_commethod(9)
    def get_MinFrequency(self) -> Double: ...
    @winrt_commethod(10)
    def get_MaxFrequency(self) -> Double: ...
    @winrt_commethod(11)
    def OpenPin(self, pinNumber: Int32) -> win32more.Windows.Devices.Pwm.PwmPin: ...
    PinCount = property(get_PinCount, None)
    ActualFrequency = property(get_ActualFrequency, None)
    MinFrequency = property(get_MinFrequency, None)
    MaxFrequency = property(get_MaxFrequency, None)
class IPwmControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Pwm.IPwmControllerStatics'
    _iid_ = Guid('{4263bda1-8946-4404-bd48-81dd124af4d9}')
    @winrt_commethod(6)
    def GetControllersAsync(self, provider: win32more.Windows.Devices.Pwm.Provider.IPwmProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Pwm.PwmController]]: ...
class IPwmControllerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Pwm.IPwmControllerStatics2'
    _iid_ = Guid('{44fc5b1f-f119-4bdd-97ad-f76ef986736d}')
    @winrt_commethod(6)
    def GetDefaultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Pwm.PwmController]: ...
class IPwmControllerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Pwm.IPwmControllerStatics3'
    _iid_ = Guid('{b2581871-0229-4344-ae3f-9b7cd0e66b94}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromFriendlyName(self, friendlyName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Pwm.PwmController]: ...
class IPwmPin(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Pwm.IPwmPin'
    _iid_ = Guid('{22972dc8-c6cf-4821-b7f9-c6454fb6af79}')
    @winrt_commethod(6)
    def get_Controller(self) -> win32more.Windows.Devices.Pwm.PwmController: ...
    @winrt_commethod(7)
    def GetActiveDutyCyclePercentage(self) -> Double: ...
    @winrt_commethod(8)
    def SetActiveDutyCyclePercentage(self, dutyCyclePercentage: Double) -> Void: ...
    @winrt_commethod(9)
    def get_Polarity(self) -> win32more.Windows.Devices.Pwm.PwmPulsePolarity: ...
    @winrt_commethod(10)
    def put_Polarity(self, value: win32more.Windows.Devices.Pwm.PwmPulsePolarity) -> Void: ...
    @winrt_commethod(11)
    def Start(self) -> Void: ...
    @winrt_commethod(12)
    def Stop(self) -> Void: ...
    @winrt_commethod(13)
    def get_IsStarted(self) -> Boolean: ...
    Controller = property(get_Controller, None)
    Polarity = property(get_Polarity, put_Polarity)
    IsStarted = property(get_IsStarted, None)
class PwmController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Pwm.IPwmController
    _classid_ = 'Windows.Devices.Pwm.PwmController'
    @winrt_mixinmethod
    def get_PinCount(self: win32more.Windows.Devices.Pwm.IPwmController) -> Int32: ...
    @winrt_mixinmethod
    def get_ActualFrequency(self: win32more.Windows.Devices.Pwm.IPwmController) -> Double: ...
    @winrt_mixinmethod
    def SetDesiredFrequency(self: win32more.Windows.Devices.Pwm.IPwmController, desiredFrequency: Double) -> Double: ...
    @winrt_mixinmethod
    def get_MinFrequency(self: win32more.Windows.Devices.Pwm.IPwmController) -> Double: ...
    @winrt_mixinmethod
    def get_MaxFrequency(self: win32more.Windows.Devices.Pwm.IPwmController) -> Double: ...
    @winrt_mixinmethod
    def OpenPin(self: win32more.Windows.Devices.Pwm.IPwmController, pinNumber: Int32) -> win32more.Windows.Devices.Pwm.PwmPin: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Pwm.IPwmControllerStatics3) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromFriendlyName(cls: win32more.Windows.Devices.Pwm.IPwmControllerStatics3, friendlyName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Pwm.IPwmControllerStatics3, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Pwm.PwmController]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: win32more.Windows.Devices.Pwm.IPwmControllerStatics2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Pwm.PwmController]: ...
    @winrt_classmethod
    def GetControllersAsync(cls: win32more.Windows.Devices.Pwm.IPwmControllerStatics, provider: win32more.Windows.Devices.Pwm.Provider.IPwmProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Pwm.PwmController]]: ...
    PinCount = property(get_PinCount, None)
    ActualFrequency = property(get_ActualFrequency, None)
    MinFrequency = property(get_MinFrequency, None)
    MaxFrequency = property(get_MaxFrequency, None)
class PwmPin(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Pwm.IPwmPin
    _classid_ = 'Windows.Devices.Pwm.PwmPin'
    @winrt_mixinmethod
    def get_Controller(self: win32more.Windows.Devices.Pwm.IPwmPin) -> win32more.Windows.Devices.Pwm.PwmController: ...
    @winrt_mixinmethod
    def GetActiveDutyCyclePercentage(self: win32more.Windows.Devices.Pwm.IPwmPin) -> Double: ...
    @winrt_mixinmethod
    def SetActiveDutyCyclePercentage(self: win32more.Windows.Devices.Pwm.IPwmPin, dutyCyclePercentage: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Polarity(self: win32more.Windows.Devices.Pwm.IPwmPin) -> win32more.Windows.Devices.Pwm.PwmPulsePolarity: ...
    @winrt_mixinmethod
    def put_Polarity(self: win32more.Windows.Devices.Pwm.IPwmPin, value: win32more.Windows.Devices.Pwm.PwmPulsePolarity) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.Pwm.IPwmPin) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.Pwm.IPwmPin) -> Void: ...
    @winrt_mixinmethod
    def get_IsStarted(self: win32more.Windows.Devices.Pwm.IPwmPin) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Controller = property(get_Controller, None)
    Polarity = property(get_Polarity, put_Polarity)
    IsStarted = property(get_IsStarted, None)
PwmPulsePolarity = Int32
PwmPulsePolarity_ActiveHigh: PwmPulsePolarity = 0
PwmPulsePolarity_ActiveLow: PwmPulsePolarity = 1
make_ready(__name__)
