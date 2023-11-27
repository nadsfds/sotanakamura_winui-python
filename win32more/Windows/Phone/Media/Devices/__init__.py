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
import win32more.Windows.Phone.Media.Devices
AudioRoutingEndpoint = Int32
AudioRoutingEndpoint_Default: AudioRoutingEndpoint = 0
AudioRoutingEndpoint_Earpiece: AudioRoutingEndpoint = 1
AudioRoutingEndpoint_Speakerphone: AudioRoutingEndpoint = 2
AudioRoutingEndpoint_Bluetooth: AudioRoutingEndpoint = 3
AudioRoutingEndpoint_WiredHeadset: AudioRoutingEndpoint = 4
AudioRoutingEndpoint_WiredHeadsetSpeakerOnly: AudioRoutingEndpoint = 5
AudioRoutingEndpoint_BluetoothWithNoiseAndEchoCancellation: AudioRoutingEndpoint = 6
AudioRoutingEndpoint_BluetoothPreferred: AudioRoutingEndpoint = 7
class AudioRoutingManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Media.Devices.IAudioRoutingManager
    _classid_ = 'Windows.Phone.Media.Devices.AudioRoutingManager'
    @winrt_mixinmethod
    def GetAudioEndpoint(self: win32more.Windows.Phone.Media.Devices.IAudioRoutingManager) -> win32more.Windows.Phone.Media.Devices.AudioRoutingEndpoint: ...
    @winrt_mixinmethod
    def SetAudioEndpoint(self: win32more.Windows.Phone.Media.Devices.IAudioRoutingManager, endpoint: win32more.Windows.Phone.Media.Devices.AudioRoutingEndpoint) -> Void: ...
    @winrt_mixinmethod
    def add_AudioEndpointChanged(self: win32more.Windows.Phone.Media.Devices.IAudioRoutingManager, endpointChangeHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Phone.Media.Devices.AudioRoutingManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AudioEndpointChanged(self: win32more.Windows.Phone.Media.Devices.IAudioRoutingManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AvailableAudioEndpoints(self: win32more.Windows.Phone.Media.Devices.IAudioRoutingManager) -> win32more.Windows.Phone.Media.Devices.AvailableAudioRoutingEndpoints: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Phone.Media.Devices.IAudioRoutingManagerStatics) -> win32more.Windows.Phone.Media.Devices.AudioRoutingManager: ...
    AvailableAudioEndpoints = property(get_AvailableAudioEndpoints, None)
AvailableAudioRoutingEndpoints = UInt32
AvailableAudioRoutingEndpoints_None: AvailableAudioRoutingEndpoints = 0
AvailableAudioRoutingEndpoints_Earpiece: AvailableAudioRoutingEndpoints = 1
AvailableAudioRoutingEndpoints_Speakerphone: AvailableAudioRoutingEndpoints = 2
AvailableAudioRoutingEndpoints_Bluetooth: AvailableAudioRoutingEndpoints = 4
class IAudioRoutingManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Media.Devices.IAudioRoutingManager'
    _iid_ = Guid('{79340d20-71cc-4526-9f29-fc8d2486418b}')
    @winrt_commethod(6)
    def GetAudioEndpoint(self) -> win32more.Windows.Phone.Media.Devices.AudioRoutingEndpoint: ...
    @winrt_commethod(7)
    def SetAudioEndpoint(self, endpoint: win32more.Windows.Phone.Media.Devices.AudioRoutingEndpoint) -> Void: ...
    @winrt_commethod(8)
    def add_AudioEndpointChanged(self, endpointChangeHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Phone.Media.Devices.AudioRoutingManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_AudioEndpointChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_AvailableAudioEndpoints(self) -> win32more.Windows.Phone.Media.Devices.AvailableAudioRoutingEndpoints: ...
    AvailableAudioEndpoints = property(get_AvailableAudioEndpoints, None)
class IAudioRoutingManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Media.Devices.IAudioRoutingManagerStatics'
    _iid_ = Guid('{977fb2a4-5590-4a6f-adde-6a3d0ad58250}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Phone.Media.Devices.AudioRoutingManager: ...
make_ready(__name__)
