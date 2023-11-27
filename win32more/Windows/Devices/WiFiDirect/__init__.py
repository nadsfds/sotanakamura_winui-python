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
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Devices.WiFiDirect
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking
import win32more.Windows.Security.Credentials
import win32more.Windows.Storage.Streams
class IWiFiDirectAdvertisement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement'
    _iid_ = Guid('{ab511a2d-2a06-49a1-a584-61435c7905a6}')
    @winrt_commethod(6)
    def get_InformationElements(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.WiFiDirect.WiFiDirectInformationElement]: ...
    @winrt_commethod(7)
    def put_InformationElements(self, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.WiFiDirect.WiFiDirectInformationElement]) -> Void: ...
    @winrt_commethod(8)
    def get_ListenStateDiscoverability(self) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementListenStateDiscoverability: ...
    @winrt_commethod(9)
    def put_ListenStateDiscoverability(self, value: win32more.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementListenStateDiscoverability) -> Void: ...
    @winrt_commethod(10)
    def get_IsAutonomousGroupOwnerEnabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsAutonomousGroupOwnerEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_LegacySettings(self) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectLegacySettings: ...
    InformationElements = property(get_InformationElements, put_InformationElements)
    ListenStateDiscoverability = property(get_ListenStateDiscoverability, put_ListenStateDiscoverability)
    IsAutonomousGroupOwnerEnabled = property(get_IsAutonomousGroupOwnerEnabled, put_IsAutonomousGroupOwnerEnabled)
    LegacySettings = property(get_LegacySettings, None)
class IWiFiDirectAdvertisement2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement2'
    _iid_ = Guid('{b759aa46-d816-491b-917a-b40d7dc403a2}')
    @winrt_commethod(6)
    def get_SupportedConfigurationMethods(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.WiFiDirect.WiFiDirectConfigurationMethod]: ...
    SupportedConfigurationMethods = property(get_SupportedConfigurationMethods, None)
class IWiFiDirectAdvertisementPublisher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisher'
    _iid_ = Guid('{b35a2d1a-9b1f-45d9-925a-694d66df68ef}')
    @winrt_commethod(6)
    def get_Advertisement(self) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectAdvertisement: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisherStatus: ...
    @winrt_commethod(8)
    def add_StatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisher, win32more.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisherStatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_StatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def Start(self) -> Void: ...
    @winrt_commethod(11)
    def Stop(self) -> Void: ...
    Advertisement = property(get_Advertisement, None)
    Status = property(get_Status, None)
class IWiFiDirectAdvertisementPublisherStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisherStatusChangedEventArgs'
    _iid_ = Guid('{aafde53c-5481-46e6-90dd-32116518f192}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisherStatus: ...
    @winrt_commethod(7)
    def get_Error(self) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectError: ...
    Status = property(get_Status, None)
    Error = property(get_Error, None)
class IWiFiDirectConnectionListener(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.IWiFiDirectConnectionListener'
    _iid_ = Guid('{699c1b0d-8d13-4ee9-b9ec-9c72f8251f7d}')
    @winrt_commethod(6)
    def add_ConnectionRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.WiFiDirectConnectionListener, win32more.Windows.Devices.WiFiDirect.WiFiDirectConnectionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ConnectionRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IWiFiDirectConnectionParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.IWiFiDirectConnectionParameters'
    _iid_ = Guid('{b2e55405-5702-4b16-a02c-bbcd21ef6098}')
    @winrt_commethod(6)
    def get_GroupOwnerIntent(self) -> Int16: ...
    @winrt_commethod(7)
    def put_GroupOwnerIntent(self, value: Int16) -> Void: ...
    GroupOwnerIntent = property(get_GroupOwnerIntent, put_GroupOwnerIntent)
class IWiFiDirectConnectionParameters2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.IWiFiDirectConnectionParameters2'
    _iid_ = Guid('{ab3b0fbe-aa82-44b4-88c8-e3056b89801d}')
    @winrt_commethod(6)
    def get_PreferenceOrderedConfigurationMethods(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.WiFiDirect.WiFiDirectConfigurationMethod]: ...
    @winrt_commethod(7)
    def get_PreferredPairingProcedure(self) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectPairingProcedure: ...
    @winrt_commethod(8)
    def put_PreferredPairingProcedure(self, value: win32more.Windows.Devices.WiFiDirect.WiFiDirectPairingProcedure) -> Void: ...
    PreferenceOrderedConfigurationMethods = property(get_PreferenceOrderedConfigurationMethods, None)
    PreferredPairingProcedure = property(get_PreferredPairingProcedure, put_PreferredPairingProcedure)
class IWiFiDirectConnectionParametersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.IWiFiDirectConnectionParametersStatics'
    _iid_ = Guid('{598af493-7642-456f-b9d8-e8a9eb1f401a}')
    @winrt_commethod(6)
    def GetDevicePairingKinds(self, configurationMethod: win32more.Windows.Devices.WiFiDirect.WiFiDirectConfigurationMethod) -> win32more.Windows.Devices.Enumeration.DevicePairingKinds: ...
class IWiFiDirectConnectionRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.IWiFiDirectConnectionRequest'
    _iid_ = Guid('{8eb99605-914f-49c3-a614-d18dc5b19b43}')
    @winrt_commethod(6)
    def get_DeviceInformation(self) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    DeviceInformation = property(get_DeviceInformation, None)
class IWiFiDirectConnectionRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.IWiFiDirectConnectionRequestedEventArgs'
    _iid_ = Guid('{f99d20be-d38d-484f-8215-e7b65abf244c}')
    @winrt_commethod(6)
    def GetConnectionRequest(self) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectConnectionRequest: ...
class IWiFiDirectDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.IWiFiDirectDevice'
    _iid_ = Guid('{72deaaa8-72eb-4dae-8a28-8513355d2777}')
    @winrt_commethod(6)
    def get_ConnectionStatus(self) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectConnectionStatus: ...
    @winrt_commethod(7)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def add_ConnectionStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.WiFiDirectDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ConnectionStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def GetConnectionEndpointPairs(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.EndpointPair]: ...
    ConnectionStatus = property(get_ConnectionStatus, None)
    DeviceId = property(get_DeviceId, None)
class IWiFiDirectDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.IWiFiDirectDeviceStatics'
    _iid_ = Guid('{e86cb57c-3aac-4851-a792-482aaf931b04}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFiDirect.WiFiDirectDevice]: ...
class IWiFiDirectDeviceStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.IWiFiDirectDeviceStatics2'
    _iid_ = Guid('{1a953e49-b103-437e-9226-ab67971342f9}')
    @winrt_commethod(6)
    def GetDeviceSelector(self, type: win32more.Windows.Devices.WiFiDirect.WiFiDirectDeviceSelectorType) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String, connectionParameters: win32more.Windows.Devices.WiFiDirect.WiFiDirectConnectionParameters) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFiDirect.WiFiDirectDevice]: ...
class IWiFiDirectInformationElement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.IWiFiDirectInformationElement'
    _iid_ = Guid('{affb72d6-76bb-497e-ac8b-dc72838bc309}')
    @winrt_commethod(6)
    def get_Oui(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def put_Oui(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(8)
    def get_OuiType(self) -> Byte: ...
    @winrt_commethod(9)
    def put_OuiType(self, value: Byte) -> Void: ...
    @winrt_commethod(10)
    def get_Value(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(11)
    def put_Value(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    Oui = property(get_Oui, put_Oui)
    OuiType = property(get_OuiType, put_OuiType)
    Value = property(get_Value, put_Value)
class IWiFiDirectInformationElementStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.IWiFiDirectInformationElementStatics'
    _iid_ = Guid('{dbd02f16-11a5-4e60-8caa-34772148378a}')
    @winrt_commethod(6)
    def CreateFromBuffer(self, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.WiFiDirect.WiFiDirectInformationElement]: ...
    @winrt_commethod(7)
    def CreateFromDeviceInformation(self, deviceInformation: win32more.Windows.Devices.Enumeration.DeviceInformation) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.WiFiDirect.WiFiDirectInformationElement]: ...
class IWiFiDirectLegacySettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.WiFiDirect.IWiFiDirectLegacySettings'
    _iid_ = Guid('{a64fdbba-f2fd-4567-a91b-f5c2f5321057}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Ssid(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Ssid(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Passphrase(self) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(11)
    def put_Passphrase(self, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Ssid = property(get_Ssid, put_Ssid)
    Passphrase = property(get_Passphrase, put_Passphrase)
class WiFiDirectAdvertisement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement
    _classid_ = 'Windows.Devices.WiFiDirect.WiFiDirectAdvertisement'
    @winrt_mixinmethod
    def get_InformationElements(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.WiFiDirect.WiFiDirectInformationElement]: ...
    @winrt_mixinmethod
    def put_InformationElements(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.WiFiDirect.WiFiDirectInformationElement]) -> Void: ...
    @winrt_mixinmethod
    def get_ListenStateDiscoverability(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementListenStateDiscoverability: ...
    @winrt_mixinmethod
    def put_ListenStateDiscoverability(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement, value: win32more.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementListenStateDiscoverability) -> Void: ...
    @winrt_mixinmethod
    def get_IsAutonomousGroupOwnerEnabled(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAutonomousGroupOwnerEnabled(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LegacySettings(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectLegacySettings: ...
    @winrt_mixinmethod
    def get_SupportedConfigurationMethods(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisement2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.WiFiDirect.WiFiDirectConfigurationMethod]: ...
    InformationElements = property(get_InformationElements, put_InformationElements)
    ListenStateDiscoverability = property(get_ListenStateDiscoverability, put_ListenStateDiscoverability)
    IsAutonomousGroupOwnerEnabled = property(get_IsAutonomousGroupOwnerEnabled, put_IsAutonomousGroupOwnerEnabled)
    LegacySettings = property(get_LegacySettings, None)
    SupportedConfigurationMethods = property(get_SupportedConfigurationMethods, None)
WiFiDirectAdvertisementListenStateDiscoverability = Int32
WiFiDirectAdvertisementListenStateDiscoverability_None: WiFiDirectAdvertisementListenStateDiscoverability = 0
WiFiDirectAdvertisementListenStateDiscoverability_Normal: WiFiDirectAdvertisementListenStateDiscoverability = 1
WiFiDirectAdvertisementListenStateDiscoverability_Intensive: WiFiDirectAdvertisementListenStateDiscoverability = 2
class WiFiDirectAdvertisementPublisher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisher
    _classid_ = 'Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisher'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisher: ...
    @winrt_mixinmethod
    def get_Advertisement(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisher) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectAdvertisement: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisher) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisherStatus: ...
    @winrt_mixinmethod
    def add_StatusChanged(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisher, win32more.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisherStatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusChanged(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisher) -> Void: ...
    Advertisement = property(get_Advertisement, None)
    Status = property(get_Status, None)
WiFiDirectAdvertisementPublisherStatus = Int32
WiFiDirectAdvertisementPublisherStatus_Created: WiFiDirectAdvertisementPublisherStatus = 0
WiFiDirectAdvertisementPublisherStatus_Started: WiFiDirectAdvertisementPublisherStatus = 1
WiFiDirectAdvertisementPublisherStatus_Stopped: WiFiDirectAdvertisementPublisherStatus = 2
WiFiDirectAdvertisementPublisherStatus_Aborted: WiFiDirectAdvertisementPublisherStatus = 3
class WiFiDirectAdvertisementPublisherStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisherStatusChangedEventArgs
    _classid_ = 'Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisherStatusChangedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisherStatusChangedEventArgs) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisherStatus: ...
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectAdvertisementPublisherStatusChangedEventArgs) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectError: ...
    Status = property(get_Status, None)
    Error = property(get_Error, None)
WiFiDirectConfigurationMethod = Int32
WiFiDirectConfigurationMethod_ProvidePin: WiFiDirectConfigurationMethod = 0
WiFiDirectConfigurationMethod_DisplayPin: WiFiDirectConfigurationMethod = 1
WiFiDirectConfigurationMethod_PushButton: WiFiDirectConfigurationMethod = 2
class WiFiDirectConnectionListener(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.IWiFiDirectConnectionListener
    _classid_ = 'Windows.Devices.WiFiDirect.WiFiDirectConnectionListener'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectConnectionListener: ...
    @winrt_mixinmethod
    def add_ConnectionRequested(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectConnectionListener, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.WiFiDirectConnectionListener, win32more.Windows.Devices.WiFiDirect.WiFiDirectConnectionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionRequested(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectConnectionListener, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class WiFiDirectConnectionParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.IWiFiDirectConnectionParameters
    _classid_ = 'Windows.Devices.WiFiDirect.WiFiDirectConnectionParameters'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectConnectionParameters: ...
    @winrt_mixinmethod
    def get_GroupOwnerIntent(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectConnectionParameters) -> Int16: ...
    @winrt_mixinmethod
    def put_GroupOwnerIntent(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectConnectionParameters, value: Int16) -> Void: ...
    @winrt_mixinmethod
    def get_PreferenceOrderedConfigurationMethods(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectConnectionParameters2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.WiFiDirect.WiFiDirectConfigurationMethod]: ...
    @winrt_mixinmethod
    def get_PreferredPairingProcedure(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectConnectionParameters2) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectPairingProcedure: ...
    @winrt_mixinmethod
    def put_PreferredPairingProcedure(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectConnectionParameters2, value: win32more.Windows.Devices.WiFiDirect.WiFiDirectPairingProcedure) -> Void: ...
    @winrt_classmethod
    def GetDevicePairingKinds(cls: win32more.Windows.Devices.WiFiDirect.IWiFiDirectConnectionParametersStatics, configurationMethod: win32more.Windows.Devices.WiFiDirect.WiFiDirectConfigurationMethod) -> win32more.Windows.Devices.Enumeration.DevicePairingKinds: ...
    GroupOwnerIntent = property(get_GroupOwnerIntent, put_GroupOwnerIntent)
    PreferenceOrderedConfigurationMethods = property(get_PreferenceOrderedConfigurationMethods, None)
    PreferredPairingProcedure = property(get_PreferredPairingProcedure, put_PreferredPairingProcedure)
class WiFiDirectConnectionRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.IWiFiDirectConnectionRequest
    _classid_ = 'Windows.Devices.WiFiDirect.WiFiDirectConnectionRequest'
    @winrt_mixinmethod
    def get_DeviceInformation(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectConnectionRequest) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    DeviceInformation = property(get_DeviceInformation, None)
class WiFiDirectConnectionRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.IWiFiDirectConnectionRequestedEventArgs
    _classid_ = 'Windows.Devices.WiFiDirect.WiFiDirectConnectionRequestedEventArgs'
    @winrt_mixinmethod
    def GetConnectionRequest(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectConnectionRequestedEventArgs) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectConnectionRequest: ...
WiFiDirectConnectionStatus = Int32
WiFiDirectConnectionStatus_Disconnected: WiFiDirectConnectionStatus = 0
WiFiDirectConnectionStatus_Connected: WiFiDirectConnectionStatus = 1
class WiFiDirectDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.IWiFiDirectDevice
    _classid_ = 'Windows.Devices.WiFiDirect.WiFiDirectDevice'
    @winrt_mixinmethod
    def get_ConnectionStatus(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectDevice) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectConnectionStatus: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_ConnectionStatusChanged(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectDevice, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.WiFiDirect.WiFiDirectDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionStatusChanged(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectDevice, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetConnectionEndpointPairs(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectDevice) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.EndpointPair]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.WiFiDirect.IWiFiDirectDeviceStatics, type: win32more.Windows.Devices.WiFiDirect.WiFiDirectDeviceSelectorType) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.WiFiDirect.IWiFiDirectDeviceStatics, deviceId: WinRT_String, connectionParameters: win32more.Windows.Devices.WiFiDirect.WiFiDirectConnectionParameters) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFiDirect.WiFiDirectDevice]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.WiFiDirect.IWiFiDirectDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.WiFiDirect.IWiFiDirectDeviceStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.WiFiDirect.WiFiDirectDevice]: ...
    ConnectionStatus = property(get_ConnectionStatus, None)
    DeviceId = property(get_DeviceId, None)
WiFiDirectDeviceSelectorType = Int32
WiFiDirectDeviceSelectorType_DeviceInterface: WiFiDirectDeviceSelectorType = 0
WiFiDirectDeviceSelectorType_AssociationEndpoint: WiFiDirectDeviceSelectorType = 1
WiFiDirectError = Int32
WiFiDirectError_Success: WiFiDirectError = 0
WiFiDirectError_RadioNotAvailable: WiFiDirectError = 1
WiFiDirectError_ResourceInUse: WiFiDirectError = 2
class WiFiDirectInformationElement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.IWiFiDirectInformationElement
    _classid_ = 'Windows.Devices.WiFiDirect.WiFiDirectInformationElement'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.WiFiDirect.WiFiDirectInformationElement: ...
    @winrt_mixinmethod
    def get_Oui(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectInformationElement) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Oui(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectInformationElement, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_OuiType(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectInformationElement) -> Byte: ...
    @winrt_mixinmethod
    def put_OuiType(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectInformationElement, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectInformationElement) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectInformationElement, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: win32more.Windows.Devices.WiFiDirect.IWiFiDirectInformationElementStatics, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.WiFiDirect.WiFiDirectInformationElement]: ...
    @winrt_classmethod
    def CreateFromDeviceInformation(cls: win32more.Windows.Devices.WiFiDirect.IWiFiDirectInformationElementStatics, deviceInformation: win32more.Windows.Devices.Enumeration.DeviceInformation) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.WiFiDirect.WiFiDirectInformationElement]: ...
    Oui = property(get_Oui, put_Oui)
    OuiType = property(get_OuiType, put_OuiType)
    Value = property(get_Value, put_Value)
class WiFiDirectLegacySettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.WiFiDirect.IWiFiDirectLegacySettings
    _classid_ = 'Windows.Devices.WiFiDirect.WiFiDirectLegacySettings'
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectLegacySettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectLegacySettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Ssid(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectLegacySettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Ssid(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectLegacySettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Passphrase(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectLegacySettings) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_Passphrase(self: win32more.Windows.Devices.WiFiDirect.IWiFiDirectLegacySettings, value: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Ssid = property(get_Ssid, put_Ssid)
    Passphrase = property(get_Passphrase, put_Passphrase)
WiFiDirectPairingProcedure = Int32
WiFiDirectPairingProcedure_GroupOwnerNegotiation: WiFiDirectPairingProcedure = 0
WiFiDirectPairingProcedure_Invitation: WiFiDirectPairingProcedure = 1
make_ready(__name__)
