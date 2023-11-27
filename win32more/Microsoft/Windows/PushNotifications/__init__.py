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
import win32more.Microsoft.Windows.PushNotifications
import win32more.Windows.ApplicationModel.Background
import win32more.Windows.Foundation
class IPushNotificationChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.PushNotifications.IPushNotificationChannel'
    _iid_ = Guid('{da28bbcb-7695-5d38-af82-f30b72fef1f6}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_ExpirationTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def Close(self) -> Void: ...
    Uri = property(get_Uri, None)
    ExpirationTime = property(get_ExpirationTime, None)
class IPushNotificationCreateChannelResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.PushNotifications.IPushNotificationCreateChannelResult'
    _iid_ = Guid('{4df3717f-5d33-56e9-b381-1b350c95722e}')
    @winrt_commethod(6)
    def get_Channel(self) -> win32more.Microsoft.Windows.PushNotifications.PushNotificationChannel: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_Status(self) -> win32more.Microsoft.Windows.PushNotifications.PushNotificationChannelStatus: ...
    Channel = property(get_Channel, None)
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class IPushNotificationManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.PushNotifications.IPushNotificationManager'
    _iid_ = Guid('{902f4aba-ff63-5dfe-a88f-15cc6bed55ff}')
    @winrt_commethod(6)
    def Register(self) -> Void: ...
    @winrt_commethod(7)
    def Unregister(self) -> Void: ...
    @winrt_commethod(8)
    def UnregisterAll(self) -> Void: ...
    @winrt_commethod(9)
    def CreateChannelAsync(self, remoteId: Guid) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.PushNotifications.PushNotificationCreateChannelResult, win32more.Microsoft.Windows.PushNotifications.PushNotificationCreateChannelStatus]: ...
    @winrt_commethod(10)
    def add_PushReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.PushNotifications.PushNotificationManager, win32more.Microsoft.Windows.PushNotifications.PushNotificationReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PushReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IPushNotificationManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.PushNotifications.IPushNotificationManagerStatics'
    _iid_ = Guid('{71329470-1b55-58dc-a00c-68c26f2d8bd9}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Default(self) -> win32more.Microsoft.Windows.PushNotifications.PushNotificationManager: ...
    Default = property(get_Default, None)
class IPushNotificationReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.PushNotifications.IPushNotificationReceivedEventArgs'
    _iid_ = Guid('{fbd4ec53-bb83-5495-8777-d3cf13e4299c}')
    @winrt_commethod(6)
    def get_Payload(self) -> SZArray[Byte]: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskDeferral: ...
    @winrt_commethod(8)
    def add_Canceled(self, handler: win32more.Windows.ApplicationModel.Background.BackgroundTaskCanceledEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Canceled(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Payload = property(get_Payload, None)
class PushNotificationChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.PushNotifications.IPushNotificationChannel
    _classid_ = 'Microsoft.Windows.PushNotifications.PushNotificationChannel'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationChannel) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationChannel) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def Close(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationChannel) -> Void: ...
    Uri = property(get_Uri, None)
    ExpirationTime = property(get_ExpirationTime, None)
PushNotificationChannelStatus = Int32
PushNotificationChannelStatus_InProgress: PushNotificationChannelStatus = 0
PushNotificationChannelStatus_InProgressRetry: PushNotificationChannelStatus = 1
PushNotificationChannelStatus_CompletedSuccess: PushNotificationChannelStatus = 2
PushNotificationChannelStatus_CompletedFailure: PushNotificationChannelStatus = 3
class PushNotificationCreateChannelResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.PushNotifications.IPushNotificationCreateChannelResult
    _classid_ = 'Microsoft.Windows.PushNotifications.PushNotificationCreateChannelResult'
    @winrt_mixinmethod
    def get_Channel(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationCreateChannelResult) -> win32more.Microsoft.Windows.PushNotifications.PushNotificationChannel: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationCreateChannelResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationCreateChannelResult) -> win32more.Microsoft.Windows.PushNotifications.PushNotificationChannelStatus: ...
    Channel = property(get_Channel, None)
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class PushNotificationCreateChannelStatus(EasyCastStructure):
    status: win32more.Microsoft.Windows.PushNotifications.PushNotificationChannelStatus
    extendedError: win32more.Windows.Foundation.HResult
    retryCount: UInt32
class _PushNotificationManager_Meta_(ComPtr.__class__):
    pass
class PushNotificationManager(ComPtr, metaclass=_PushNotificationManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManager
    _classid_ = 'Microsoft.Windows.PushNotifications.PushNotificationManager'
    @winrt_mixinmethod
    def Register(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManager) -> Void: ...
    @winrt_mixinmethod
    def Unregister(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManager) -> Void: ...
    @winrt_mixinmethod
    def UnregisterAll(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManager) -> Void: ...
    @winrt_mixinmethod
    def CreateChannelAsync(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManager, remoteId: Guid) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.PushNotifications.PushNotificationCreateChannelResult, win32more.Microsoft.Windows.PushNotifications.PushNotificationCreateChannelStatus]: ...
    @winrt_mixinmethod
    def add_PushReceived(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Windows.PushNotifications.PushNotificationManager, win32more.Microsoft.Windows.PushNotifications.PushNotificationReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PushReceived(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def get_Default(cls: win32more.Microsoft.Windows.PushNotifications.IPushNotificationManagerStatics) -> win32more.Microsoft.Windows.PushNotifications.PushNotificationManager: ...
    _PushNotificationManager_Meta_.Default = property(get_Default.__wrapped__, None)
class PushNotificationReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.PushNotifications.IPushNotificationReceivedEventArgs
    _classid_ = 'Microsoft.Windows.PushNotifications.PushNotificationReceivedEventArgs'
    @winrt_mixinmethod
    def get_Payload(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationReceivedEventArgs) -> SZArray[Byte]: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationReceivedEventArgs) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskDeferral: ...
    @winrt_mixinmethod
    def add_Canceled(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationReceivedEventArgs, handler: win32more.Windows.ApplicationModel.Background.BackgroundTaskCanceledEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Canceled(self: win32more.Microsoft.Windows.PushNotifications.IPushNotificationReceivedEventArgs, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Payload = property(get_Payload, None)
PushNotificationsContract: UInt32 = 65536
make_ready(__name__)
