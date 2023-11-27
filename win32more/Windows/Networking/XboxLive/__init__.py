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
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking
import win32more.Windows.Networking.XboxLive
import win32more.Windows.Storage.Streams
class IXboxLiveDeviceAddress(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveDeviceAddress'
    _iid_ = Guid('{f5bbd279-3c86-4b57-a31a-b9462408fd01}')
    @winrt_commethod(6)
    def add_SnapshotChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SnapshotChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def GetSnapshotAsBase64(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetSnapshotAsBuffer(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(10)
    def GetSnapshotAsBytes(self, buffer: Annotated[SZArray[Byte], 'Out'], bytesWritten: POINTER(UInt32)) -> Void: ...
    @winrt_commethod(11)
    def Compare(self, otherDeviceAddress: win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress) -> Int32: ...
    @winrt_commethod(12)
    def get_IsValid(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_IsLocal(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_NetworkAccessKind(self) -> win32more.Windows.Networking.XboxLive.XboxLiveNetworkAccessKind: ...
    IsValid = property(get_IsValid, None)
    IsLocal = property(get_IsLocal, None)
    NetworkAccessKind = property(get_NetworkAccessKind, None)
class IXboxLiveDeviceAddressStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveDeviceAddressStatics'
    _iid_ = Guid('{5954a819-4a79-4931-827c-7f503e963263}')
    @winrt_commethod(6)
    def CreateFromSnapshotBase64(self, base64: WinRT_String) -> win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_commethod(7)
    def CreateFromSnapshotBuffer(self, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_commethod(8)
    def CreateFromSnapshotBytes(self, buffer: Annotated[SZArray[Byte], 'In']) -> win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_commethod(9)
    def GetLocal(self) -> win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_commethod(10)
    def get_MaxSnapshotBytesSize(self) -> UInt32: ...
    MaxSnapshotBytesSize = property(get_MaxSnapshotBytesSize, None)
class IXboxLiveEndpointPair(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveEndpointPair'
    _iid_ = Guid('{1e9a839b-813e-44e0-b87f-c87a093475e4}')
    @winrt_commethod(6)
    def add_StateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.XboxLive.XboxLiveEndpointPair, win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_StateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def DeleteAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def GetRemoteSocketAddressBytes(self, socketAddress: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    @winrt_commethod(10)
    def GetLocalSocketAddressBytes(self, socketAddress: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    @winrt_commethod(11)
    def get_State(self) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairState: ...
    @winrt_commethod(12)
    def get_Template(self) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate: ...
    @winrt_commethod(13)
    def get_RemoteDeviceAddress(self) -> win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_commethod(14)
    def get_RemoteHostName(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(15)
    def get_RemotePort(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_LocalHostName(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(17)
    def get_LocalPort(self) -> WinRT_String: ...
    State = property(get_State, None)
    Template = property(get_Template, None)
    RemoteDeviceAddress = property(get_RemoteDeviceAddress, None)
    RemoteHostName = property(get_RemoteHostName, None)
    RemotePort = property(get_RemotePort, None)
    LocalHostName = property(get_LocalHostName, None)
    LocalPort = property(get_LocalPort, None)
class IXboxLiveEndpointPairCreationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveEndpointPairCreationResult'
    _iid_ = Guid('{d9a8bb95-2aab-4d1e-9794-33ecc0dcf0fe}')
    @winrt_commethod(6)
    def get_DeviceAddress(self) -> win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationStatus: ...
    @winrt_commethod(8)
    def get_IsExistingPathEvaluation(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_EndpointPair(self) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPair: ...
    DeviceAddress = property(get_DeviceAddress, None)
    Status = property(get_Status, None)
    IsExistingPathEvaluation = property(get_IsExistingPathEvaluation, None)
    EndpointPair = property(get_EndpointPair, None)
class IXboxLiveEndpointPairStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveEndpointPairStateChangedEventArgs'
    _iid_ = Guid('{592e3b55-de08-44e7-ac3b-b9b9a169583a}')
    @winrt_commethod(6)
    def get_OldState(self) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairState: ...
    @winrt_commethod(7)
    def get_NewState(self) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairState: ...
    OldState = property(get_OldState, None)
    NewState = property(get_NewState, None)
class IXboxLiveEndpointPairStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveEndpointPairStatics'
    _iid_ = Guid('{64316b30-217a-4243-8ee1-6729281d27db}')
    @winrt_commethod(6)
    def FindEndpointPairBySocketAddressBytes(self, localSocketAddress: Annotated[SZArray[Byte], 'In'], remoteSocketAddress: Annotated[SZArray[Byte], 'In']) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPair: ...
    @winrt_commethod(7)
    def FindEndpointPairByHostNamesAndPorts(self, localHostName: win32more.Windows.Networking.HostName, localPort: WinRT_String, remoteHostName: win32more.Windows.Networking.HostName, remotePort: WinRT_String) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPair: ...
class IXboxLiveEndpointPairTemplate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate'
    _iid_ = Guid('{6b286ecf-3457-40ce-b9a1-c0cfe0213ea7}')
    @winrt_commethod(6)
    def add_InboundEndpointPairCreated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate, win32more.Windows.Networking.XboxLive.XboxLiveInboundEndpointPairCreatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_InboundEndpointPairCreated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def CreateEndpointPairDefaultAsync(self, deviceAddress: win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult]: ...
    @winrt_commethod(9)
    def CreateEndpointPairWithBehaviorsAsync(self, deviceAddress: win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress, behaviors: win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationBehaviors) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult]: ...
    @winrt_commethod(10)
    def CreateEndpointPairForPortsDefaultAsync(self, deviceAddress: win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress, initiatorPort: WinRT_String, acceptorPort: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult]: ...
    @winrt_commethod(11)
    def CreateEndpointPairForPortsWithBehaviorsAsync(self, deviceAddress: win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress, initiatorPort: WinRT_String, acceptorPort: WinRT_String, behaviors: win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationBehaviors) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult]: ...
    @winrt_commethod(12)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_SocketKind(self) -> win32more.Windows.Networking.XboxLive.XboxLiveSocketKind: ...
    @winrt_commethod(14)
    def get_InitiatorBoundPortRangeLower(self) -> UInt16: ...
    @winrt_commethod(15)
    def get_InitiatorBoundPortRangeUpper(self) -> UInt16: ...
    @winrt_commethod(16)
    def get_AcceptorBoundPortRangeLower(self) -> UInt16: ...
    @winrt_commethod(17)
    def get_AcceptorBoundPortRangeUpper(self) -> UInt16: ...
    @winrt_commethod(18)
    def get_EndpointPairs(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.XboxLive.XboxLiveEndpointPair]: ...
    Name = property(get_Name, None)
    SocketKind = property(get_SocketKind, None)
    InitiatorBoundPortRangeLower = property(get_InitiatorBoundPortRangeLower, None)
    InitiatorBoundPortRangeUpper = property(get_InitiatorBoundPortRangeUpper, None)
    AcceptorBoundPortRangeLower = property(get_AcceptorBoundPortRangeLower, None)
    AcceptorBoundPortRangeUpper = property(get_AcceptorBoundPortRangeUpper, None)
    EndpointPairs = property(get_EndpointPairs, None)
class IXboxLiveEndpointPairTemplateStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplateStatics'
    _iid_ = Guid('{1e13137b-737b-4a23-bc64-0870f75655ba}')
    @winrt_commethod(6)
    def GetTemplateByName(self, name: WinRT_String) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate: ...
    @winrt_commethod(7)
    def get_Templates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate]: ...
    Templates = property(get_Templates, None)
class IXboxLiveInboundEndpointPairCreatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveInboundEndpointPairCreatedEventArgs'
    _iid_ = Guid('{dc183b62-22ba-48d2-80de-c23968bd198b}')
    @winrt_commethod(6)
    def get_EndpointPair(self) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPair: ...
    EndpointPair = property(get_EndpointPair, None)
class IXboxLiveQualityOfServiceMeasurement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement'
    _iid_ = Guid('{4d682bce-a5d6-47e6-a236-cfde5fbdf2ed}')
    @winrt_commethod(6)
    def MeasureAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def GetMetricResultsForDevice(self, deviceAddress: win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult]: ...
    @winrt_commethod(8)
    def GetMetricResultsForMetric(self, metric: win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult]: ...
    @winrt_commethod(9)
    def GetMetricResult(self, deviceAddress: win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress, metric: win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric) -> win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult: ...
    @winrt_commethod(10)
    def GetPrivatePayloadResult(self, deviceAddress: win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress) -> win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServicePrivatePayloadResult: ...
    @winrt_commethod(11)
    def get_Metrics(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric]: ...
    @winrt_commethod(12)
    def get_DeviceAddresses(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress]: ...
    @winrt_commethod(13)
    def get_ShouldRequestPrivatePayloads(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_ShouldRequestPrivatePayloads(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_TimeoutInMilliseconds(self) -> UInt32: ...
    @winrt_commethod(16)
    def put_TimeoutInMilliseconds(self, value: UInt32) -> Void: ...
    @winrt_commethod(17)
    def get_NumberOfProbesToAttempt(self) -> UInt32: ...
    @winrt_commethod(18)
    def put_NumberOfProbesToAttempt(self, value: UInt32) -> Void: ...
    @winrt_commethod(19)
    def get_NumberOfResultsPending(self) -> UInt32: ...
    @winrt_commethod(20)
    def get_MetricResults(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult]: ...
    @winrt_commethod(21)
    def get_PrivatePayloadResults(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServicePrivatePayloadResult]: ...
    Metrics = property(get_Metrics, None)
    DeviceAddresses = property(get_DeviceAddresses, None)
    ShouldRequestPrivatePayloads = property(get_ShouldRequestPrivatePayloads, put_ShouldRequestPrivatePayloads)
    TimeoutInMilliseconds = property(get_TimeoutInMilliseconds, put_TimeoutInMilliseconds)
    NumberOfProbesToAttempt = property(get_NumberOfProbesToAttempt, put_NumberOfProbesToAttempt)
    NumberOfResultsPending = property(get_NumberOfResultsPending, None)
    MetricResults = property(get_MetricResults, None)
    PrivatePayloadResults = property(get_PrivatePayloadResults, None)
class IXboxLiveQualityOfServiceMeasurementStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics'
    _iid_ = Guid('{6e352dca-23cf-440a-b077-5e30857a8234}')
    @winrt_commethod(6)
    def PublishPrivatePayloadBytes(self, payload: Annotated[SZArray[Byte], 'In']) -> Void: ...
    @winrt_commethod(7)
    def ClearPrivatePayload(self) -> Void: ...
    @winrt_commethod(8)
    def get_MaxSimultaneousProbeConnections(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_MaxSimultaneousProbeConnections(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_IsSystemOutboundBandwidthConstrained(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsSystemOutboundBandwidthConstrained(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsSystemInboundBandwidthConstrained(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsSystemInboundBandwidthConstrained(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_PublishedPrivatePayload(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(15)
    def put_PublishedPrivatePayload(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(16)
    def get_MaxPrivatePayloadSize(self) -> UInt32: ...
    MaxSimultaneousProbeConnections = property(get_MaxSimultaneousProbeConnections, put_MaxSimultaneousProbeConnections)
    IsSystemOutboundBandwidthConstrained = property(get_IsSystemOutboundBandwidthConstrained, put_IsSystemOutboundBandwidthConstrained)
    IsSystemInboundBandwidthConstrained = property(get_IsSystemInboundBandwidthConstrained, put_IsSystemInboundBandwidthConstrained)
    PublishedPrivatePayload = property(get_PublishedPrivatePayload, put_PublishedPrivatePayload)
    MaxPrivatePayloadSize = property(get_MaxPrivatePayloadSize, None)
class IXboxLiveQualityOfServiceMetricResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMetricResult'
    _iid_ = Guid('{aeec53d1-3561-4782-b0cf-d3ae29d9fa87}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMeasurementStatus: ...
    @winrt_commethod(7)
    def get_DeviceAddress(self) -> win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_commethod(8)
    def get_Metric(self) -> win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric: ...
    @winrt_commethod(9)
    def get_Value(self) -> UInt64: ...
    Status = property(get_Status, None)
    DeviceAddress = property(get_DeviceAddress, None)
    Metric = property(get_Metric, None)
    Value = property(get_Value, None)
class IXboxLiveQualityOfServicePrivatePayloadResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.XboxLive.IXboxLiveQualityOfServicePrivatePayloadResult'
    _iid_ = Guid('{5a6302ae-6f38-41c0-9fcc-ea6cb978cafc}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMeasurementStatus: ...
    @winrt_commethod(7)
    def get_DeviceAddress(self) -> win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_commethod(8)
    def get_Value(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Status = property(get_Status, None)
    DeviceAddress = property(get_DeviceAddress, None)
    Value = property(get_Value, None)
class _XboxLiveDeviceAddress_Meta_(ComPtr.__class__):
    pass
class XboxLiveDeviceAddress(ComPtr, metaclass=_XboxLiveDeviceAddress_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.XboxLive.IXboxLiveDeviceAddress
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveDeviceAddress'
    @winrt_mixinmethod
    def add_SnapshotChanged(self: win32more.Windows.Networking.XboxLive.IXboxLiveDeviceAddress, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SnapshotChanged(self: win32more.Windows.Networking.XboxLive.IXboxLiveDeviceAddress, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetSnapshotAsBase64(self: win32more.Windows.Networking.XboxLive.IXboxLiveDeviceAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetSnapshotAsBuffer(self: win32more.Windows.Networking.XboxLive.IXboxLiveDeviceAddress) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def GetSnapshotAsBytes(self: win32more.Windows.Networking.XboxLive.IXboxLiveDeviceAddress, buffer: Annotated[SZArray[Byte], 'Out'], bytesWritten: POINTER(UInt32)) -> Void: ...
    @winrt_mixinmethod
    def Compare(self: win32more.Windows.Networking.XboxLive.IXboxLiveDeviceAddress, otherDeviceAddress: win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress) -> Int32: ...
    @winrt_mixinmethod
    def get_IsValid(self: win32more.Windows.Networking.XboxLive.IXboxLiveDeviceAddress) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsLocal(self: win32more.Windows.Networking.XboxLive.IXboxLiveDeviceAddress) -> Boolean: ...
    @winrt_mixinmethod
    def get_NetworkAccessKind(self: win32more.Windows.Networking.XboxLive.IXboxLiveDeviceAddress) -> win32more.Windows.Networking.XboxLive.XboxLiveNetworkAccessKind: ...
    @winrt_classmethod
    def CreateFromSnapshotBase64(cls: win32more.Windows.Networking.XboxLive.IXboxLiveDeviceAddressStatics, base64: WinRT_String) -> win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_classmethod
    def CreateFromSnapshotBuffer(cls: win32more.Windows.Networking.XboxLive.IXboxLiveDeviceAddressStatics, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_classmethod
    def CreateFromSnapshotBytes(cls: win32more.Windows.Networking.XboxLive.IXboxLiveDeviceAddressStatics, buffer: Annotated[SZArray[Byte], 'In']) -> win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_classmethod
    def GetLocal(cls: win32more.Windows.Networking.XboxLive.IXboxLiveDeviceAddressStatics) -> win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_classmethod
    def get_MaxSnapshotBytesSize(cls: win32more.Windows.Networking.XboxLive.IXboxLiveDeviceAddressStatics) -> UInt32: ...
    IsValid = property(get_IsValid, None)
    IsLocal = property(get_IsLocal, None)
    NetworkAccessKind = property(get_NetworkAccessKind, None)
    _XboxLiveDeviceAddress_Meta_.MaxSnapshotBytesSize = property(get_MaxSnapshotBytesSize.__wrapped__, None)
class XboxLiveEndpointPair(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPair
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveEndpointPair'
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPair, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.XboxLive.XboxLiveEndpointPair, win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPair, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPair) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetRemoteSocketAddressBytes(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPair, socketAddress: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    @winrt_mixinmethod
    def GetLocalSocketAddressBytes(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPair, socketAddress: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPair) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairState: ...
    @winrt_mixinmethod
    def get_Template(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPair) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate: ...
    @winrt_mixinmethod
    def get_RemoteDeviceAddress(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPair) -> win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_mixinmethod
    def get_RemoteHostName(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPair) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_RemotePort(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPair) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LocalHostName(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPair) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_LocalPort(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPair) -> WinRT_String: ...
    @winrt_classmethod
    def FindEndpointPairBySocketAddressBytes(cls: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairStatics, localSocketAddress: Annotated[SZArray[Byte], 'In'], remoteSocketAddress: Annotated[SZArray[Byte], 'In']) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPair: ...
    @winrt_classmethod
    def FindEndpointPairByHostNamesAndPorts(cls: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairStatics, localHostName: win32more.Windows.Networking.HostName, localPort: WinRT_String, remoteHostName: win32more.Windows.Networking.HostName, remotePort: WinRT_String) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPair: ...
    State = property(get_State, None)
    Template = property(get_Template, None)
    RemoteDeviceAddress = property(get_RemoteDeviceAddress, None)
    RemoteHostName = property(get_RemoteHostName, None)
    RemotePort = property(get_RemotePort, None)
    LocalHostName = property(get_LocalHostName, None)
    LocalPort = property(get_LocalPort, None)
XboxLiveEndpointPairCreationBehaviors = UInt32
XboxLiveEndpointPairCreationBehaviors_None: XboxLiveEndpointPairCreationBehaviors = 0
XboxLiveEndpointPairCreationBehaviors_ReevaluatePath: XboxLiveEndpointPairCreationBehaviors = 1
class XboxLiveEndpointPairCreationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairCreationResult
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult'
    @winrt_mixinmethod
    def get_DeviceAddress(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairCreationResult) -> win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairCreationResult) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationStatus: ...
    @winrt_mixinmethod
    def get_IsExistingPathEvaluation(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairCreationResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_EndpointPair(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairCreationResult) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPair: ...
    DeviceAddress = property(get_DeviceAddress, None)
    Status = property(get_Status, None)
    IsExistingPathEvaluation = property(get_IsExistingPathEvaluation, None)
    EndpointPair = property(get_EndpointPair, None)
XboxLiveEndpointPairCreationStatus = Int32
XboxLiveEndpointPairCreationStatus_Succeeded: XboxLiveEndpointPairCreationStatus = 0
XboxLiveEndpointPairCreationStatus_NoLocalNetworks: XboxLiveEndpointPairCreationStatus = 1
XboxLiveEndpointPairCreationStatus_NoCompatibleNetworkPaths: XboxLiveEndpointPairCreationStatus = 2
XboxLiveEndpointPairCreationStatus_LocalSystemNotAuthorized: XboxLiveEndpointPairCreationStatus = 3
XboxLiveEndpointPairCreationStatus_Canceled: XboxLiveEndpointPairCreationStatus = 4
XboxLiveEndpointPairCreationStatus_TimedOut: XboxLiveEndpointPairCreationStatus = 5
XboxLiveEndpointPairCreationStatus_RemoteSystemNotAuthorized: XboxLiveEndpointPairCreationStatus = 6
XboxLiveEndpointPairCreationStatus_RefusedDueToConfiguration: XboxLiveEndpointPairCreationStatus = 7
XboxLiveEndpointPairCreationStatus_UnexpectedInternalError: XboxLiveEndpointPairCreationStatus = 8
XboxLiveEndpointPairState = Int32
XboxLiveEndpointPairState_Invalid: XboxLiveEndpointPairState = 0
XboxLiveEndpointPairState_CreatingOutbound: XboxLiveEndpointPairState = 1
XboxLiveEndpointPairState_CreatingInbound: XboxLiveEndpointPairState = 2
XboxLiveEndpointPairState_Ready: XboxLiveEndpointPairState = 3
XboxLiveEndpointPairState_DeletingLocally: XboxLiveEndpointPairState = 4
XboxLiveEndpointPairState_RemoteEndpointTerminating: XboxLiveEndpointPairState = 5
XboxLiveEndpointPairState_Deleted: XboxLiveEndpointPairState = 6
class XboxLiveEndpointPairStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairStateChangedEventArgs
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveEndpointPairStateChangedEventArgs'
    @winrt_mixinmethod
    def get_OldState(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairStateChangedEventArgs) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairState: ...
    @winrt_mixinmethod
    def get_NewState(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairStateChangedEventArgs) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairState: ...
    OldState = property(get_OldState, None)
    NewState = property(get_NewState, None)
class _XboxLiveEndpointPairTemplate_Meta_(ComPtr.__class__):
    pass
class XboxLiveEndpointPairTemplate(ComPtr, metaclass=_XboxLiveEndpointPairTemplate_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate'
    @winrt_mixinmethod
    def add_InboundEndpointPairCreated(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate, win32more.Windows.Networking.XboxLive.XboxLiveInboundEndpointPairCreatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InboundEndpointPairCreated(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateEndpointPairDefaultAsync(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate, deviceAddress: win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult]: ...
    @winrt_mixinmethod
    def CreateEndpointPairWithBehaviorsAsync(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate, deviceAddress: win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress, behaviors: win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationBehaviors) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult]: ...
    @winrt_mixinmethod
    def CreateEndpointPairForPortsDefaultAsync(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate, deviceAddress: win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress, initiatorPort: WinRT_String, acceptorPort: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult]: ...
    @winrt_mixinmethod
    def CreateEndpointPairForPortsWithBehaviorsAsync(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate, deviceAddress: win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress, initiatorPort: WinRT_String, acceptorPort: WinRT_String, behaviors: win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationBehaviors) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationResult]: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SocketKind(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate) -> win32more.Windows.Networking.XboxLive.XboxLiveSocketKind: ...
    @winrt_mixinmethod
    def get_InitiatorBoundPortRangeLower(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate) -> UInt16: ...
    @winrt_mixinmethod
    def get_InitiatorBoundPortRangeUpper(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate) -> UInt16: ...
    @winrt_mixinmethod
    def get_AcceptorBoundPortRangeLower(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate) -> UInt16: ...
    @winrt_mixinmethod
    def get_AcceptorBoundPortRangeUpper(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate) -> UInt16: ...
    @winrt_mixinmethod
    def get_EndpointPairs(self: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplate) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.XboxLive.XboxLiveEndpointPair]: ...
    @winrt_classmethod
    def GetTemplateByName(cls: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplateStatics, name: WinRT_String) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate: ...
    @winrt_classmethod
    def get_Templates(cls: win32more.Windows.Networking.XboxLive.IXboxLiveEndpointPairTemplateStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.XboxLive.XboxLiveEndpointPairTemplate]: ...
    Name = property(get_Name, None)
    SocketKind = property(get_SocketKind, None)
    InitiatorBoundPortRangeLower = property(get_InitiatorBoundPortRangeLower, None)
    InitiatorBoundPortRangeUpper = property(get_InitiatorBoundPortRangeUpper, None)
    AcceptorBoundPortRangeLower = property(get_AcceptorBoundPortRangeLower, None)
    AcceptorBoundPortRangeUpper = property(get_AcceptorBoundPortRangeUpper, None)
    EndpointPairs = property(get_EndpointPairs, None)
    _XboxLiveEndpointPairTemplate_Meta_.Templates = property(get_Templates.__wrapped__, None)
class XboxLiveInboundEndpointPairCreatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.XboxLive.IXboxLiveInboundEndpointPairCreatedEventArgs
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveInboundEndpointPairCreatedEventArgs'
    @winrt_mixinmethod
    def get_EndpointPair(self: win32more.Windows.Networking.XboxLive.IXboxLiveInboundEndpointPairCreatedEventArgs) -> win32more.Windows.Networking.XboxLive.XboxLiveEndpointPair: ...
    EndpointPair = property(get_EndpointPair, None)
XboxLiveNetworkAccessKind = Int32
XboxLiveNetworkAccessKind_Open: XboxLiveNetworkAccessKind = 0
XboxLiveNetworkAccessKind_Moderate: XboxLiveNetworkAccessKind = 1
XboxLiveNetworkAccessKind_Strict: XboxLiveNetworkAccessKind = 2
class _XboxLiveQualityOfServiceMeasurement_Meta_(ComPtr.__class__):
    pass
class XboxLiveQualityOfServiceMeasurement(ComPtr, metaclass=_XboxLiveQualityOfServiceMeasurement_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveQualityOfServiceMeasurement'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMeasurement: ...
    @winrt_mixinmethod
    def MeasureAsync(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetMetricResultsForDevice(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement, deviceAddress: win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult]: ...
    @winrt_mixinmethod
    def GetMetricResultsForMetric(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement, metric: win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult]: ...
    @winrt_mixinmethod
    def GetMetricResult(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement, deviceAddress: win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress, metric: win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric) -> win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult: ...
    @winrt_mixinmethod
    def GetPrivatePayloadResult(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement, deviceAddress: win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress) -> win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServicePrivatePayloadResult: ...
    @winrt_mixinmethod
    def get_Metrics(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric]: ...
    @winrt_mixinmethod
    def get_DeviceAddresses(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress]: ...
    @winrt_mixinmethod
    def get_ShouldRequestPrivatePayloads(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldRequestPrivatePayloads(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TimeoutInMilliseconds(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> UInt32: ...
    @winrt_mixinmethod
    def put_TimeoutInMilliseconds(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_NumberOfProbesToAttempt(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> UInt32: ...
    @winrt_mixinmethod
    def put_NumberOfProbesToAttempt(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_NumberOfResultsPending(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> UInt32: ...
    @winrt_mixinmethod
    def get_MetricResults(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult]: ...
    @winrt_mixinmethod
    def get_PrivatePayloadResults(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurement) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServicePrivatePayloadResult]: ...
    @winrt_classmethod
    def PublishPrivatePayloadBytes(cls: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics, payload: Annotated[SZArray[Byte], 'In']) -> Void: ...
    @winrt_classmethod
    def ClearPrivatePayload(cls: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics) -> Void: ...
    @winrt_classmethod
    def get_MaxSimultaneousProbeConnections(cls: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics) -> UInt32: ...
    @winrt_classmethod
    def put_MaxSimultaneousProbeConnections(cls: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics, value: UInt32) -> Void: ...
    @winrt_classmethod
    def get_IsSystemOutboundBandwidthConstrained(cls: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics) -> Boolean: ...
    @winrt_classmethod
    def put_IsSystemOutboundBandwidthConstrained(cls: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsSystemInboundBandwidthConstrained(cls: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics) -> Boolean: ...
    @winrt_classmethod
    def put_IsSystemInboundBandwidthConstrained(cls: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_PublishedPrivatePayload(cls: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def put_PublishedPrivatePayload(cls: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_classmethod
    def get_MaxPrivatePayloadSize(cls: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMeasurementStatics) -> UInt32: ...
    Metrics = property(get_Metrics, None)
    DeviceAddresses = property(get_DeviceAddresses, None)
    ShouldRequestPrivatePayloads = property(get_ShouldRequestPrivatePayloads, put_ShouldRequestPrivatePayloads)
    TimeoutInMilliseconds = property(get_TimeoutInMilliseconds, put_TimeoutInMilliseconds)
    NumberOfProbesToAttempt = property(get_NumberOfProbesToAttempt, put_NumberOfProbesToAttempt)
    NumberOfResultsPending = property(get_NumberOfResultsPending, None)
    MetricResults = property(get_MetricResults, None)
    PrivatePayloadResults = property(get_PrivatePayloadResults, None)
    _XboxLiveQualityOfServiceMeasurement_Meta_.MaxSimultaneousProbeConnections = property(get_MaxSimultaneousProbeConnections.__wrapped__, put_MaxSimultaneousProbeConnections.__wrapped__)
    _XboxLiveQualityOfServiceMeasurement_Meta_.IsSystemOutboundBandwidthConstrained = property(get_IsSystemOutboundBandwidthConstrained.__wrapped__, put_IsSystemOutboundBandwidthConstrained.__wrapped__)
    _XboxLiveQualityOfServiceMeasurement_Meta_.IsSystemInboundBandwidthConstrained = property(get_IsSystemInboundBandwidthConstrained.__wrapped__, put_IsSystemInboundBandwidthConstrained.__wrapped__)
    _XboxLiveQualityOfServiceMeasurement_Meta_.PublishedPrivatePayload = property(get_PublishedPrivatePayload.__wrapped__, put_PublishedPrivatePayload.__wrapped__)
    _XboxLiveQualityOfServiceMeasurement_Meta_.MaxPrivatePayloadSize = property(get_MaxPrivatePayloadSize.__wrapped__, None)
XboxLiveQualityOfServiceMeasurementStatus = Int32
XboxLiveQualityOfServiceMeasurementStatus_NotStarted: XboxLiveQualityOfServiceMeasurementStatus = 0
XboxLiveQualityOfServiceMeasurementStatus_InProgress: XboxLiveQualityOfServiceMeasurementStatus = 1
XboxLiveQualityOfServiceMeasurementStatus_InProgressWithProvisionalResults: XboxLiveQualityOfServiceMeasurementStatus = 2
XboxLiveQualityOfServiceMeasurementStatus_Succeeded: XboxLiveQualityOfServiceMeasurementStatus = 3
XboxLiveQualityOfServiceMeasurementStatus_NoLocalNetworks: XboxLiveQualityOfServiceMeasurementStatus = 4
XboxLiveQualityOfServiceMeasurementStatus_NoCompatibleNetworkPaths: XboxLiveQualityOfServiceMeasurementStatus = 5
XboxLiveQualityOfServiceMeasurementStatus_LocalSystemNotAuthorized: XboxLiveQualityOfServiceMeasurementStatus = 6
XboxLiveQualityOfServiceMeasurementStatus_Canceled: XboxLiveQualityOfServiceMeasurementStatus = 7
XboxLiveQualityOfServiceMeasurementStatus_TimedOut: XboxLiveQualityOfServiceMeasurementStatus = 8
XboxLiveQualityOfServiceMeasurementStatus_RemoteSystemNotAuthorized: XboxLiveQualityOfServiceMeasurementStatus = 9
XboxLiveQualityOfServiceMeasurementStatus_RefusedDueToConfiguration: XboxLiveQualityOfServiceMeasurementStatus = 10
XboxLiveQualityOfServiceMeasurementStatus_UnexpectedInternalError: XboxLiveQualityOfServiceMeasurementStatus = 11
XboxLiveQualityOfServiceMetric = Int32
XboxLiveQualityOfServiceMetric_AverageLatencyInMilliseconds: XboxLiveQualityOfServiceMetric = 0
XboxLiveQualityOfServiceMetric_MinLatencyInMilliseconds: XboxLiveQualityOfServiceMetric = 1
XboxLiveQualityOfServiceMetric_MaxLatencyInMilliseconds: XboxLiveQualityOfServiceMetric = 2
XboxLiveQualityOfServiceMetric_AverageOutboundBitsPerSecond: XboxLiveQualityOfServiceMetric = 3
XboxLiveQualityOfServiceMetric_MinOutboundBitsPerSecond: XboxLiveQualityOfServiceMetric = 4
XboxLiveQualityOfServiceMetric_MaxOutboundBitsPerSecond: XboxLiveQualityOfServiceMetric = 5
XboxLiveQualityOfServiceMetric_AverageInboundBitsPerSecond: XboxLiveQualityOfServiceMetric = 6
XboxLiveQualityOfServiceMetric_MinInboundBitsPerSecond: XboxLiveQualityOfServiceMetric = 7
XboxLiveQualityOfServiceMetric_MaxInboundBitsPerSecond: XboxLiveQualityOfServiceMetric = 8
class XboxLiveQualityOfServiceMetricResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMetricResult
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetricResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMetricResult) -> win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMeasurementStatus: ...
    @winrt_mixinmethod
    def get_DeviceAddress(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMetricResult) -> win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_mixinmethod
    def get_Metric(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMetricResult) -> win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServiceMetricResult) -> UInt64: ...
    Status = property(get_Status, None)
    DeviceAddress = property(get_DeviceAddress, None)
    Metric = property(get_Metric, None)
    Value = property(get_Value, None)
class XboxLiveQualityOfServicePrivatePayloadResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServicePrivatePayloadResult
    _classid_ = 'Windows.Networking.XboxLive.XboxLiveQualityOfServicePrivatePayloadResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServicePrivatePayloadResult) -> win32more.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMeasurementStatus: ...
    @winrt_mixinmethod
    def get_DeviceAddress(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServicePrivatePayloadResult) -> win32more.Windows.Networking.XboxLive.XboxLiveDeviceAddress: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Networking.XboxLive.IXboxLiveQualityOfServicePrivatePayloadResult) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Status = property(get_Status, None)
    DeviceAddress = property(get_DeviceAddress, None)
    Value = property(get_Value, None)
XboxLiveSecureSocketsContract: UInt32 = 65536
XboxLiveSocketKind = Int32
XboxLiveSocketKind_None: XboxLiveSocketKind = 0
XboxLiveSocketKind_Datagram: XboxLiveSocketKind = 1
XboxLiveSocketKind_Stream: XboxLiveSocketKind = 2
make_ready(__name__)
