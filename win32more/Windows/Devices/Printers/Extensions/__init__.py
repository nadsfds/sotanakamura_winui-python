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
import win32more.Windows.Devices.Printers.Extensions
import win32more.Windows.Foundation
ExtensionsContract: UInt32 = 131072
class IPrint3DWorkflow(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.IPrint3DWorkflow'
    _iid_ = Guid('{c56f74bd-3669-4a66-ab42-c8151930cd34}')
    @winrt_commethod(6)
    def get_DeviceID(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetPrintModelPackage(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(8)
    def get_IsPrintReady(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsPrintReady(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def add_PrintRequested(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Printers.Extensions.Print3DWorkflow, win32more.Windows.Devices.Printers.Extensions.Print3DWorkflowPrintRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PrintRequested(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceID = property(get_DeviceID, None)
    IsPrintReady = property(get_IsPrintReady, put_IsPrintReady)
class IPrint3DWorkflow2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.IPrint3DWorkflow2'
    _iid_ = Guid('{a2a6c54f-8ac1-4918-9741-e34f3004239e}')
    @winrt_commethod(6)
    def add_PrinterChanged(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Printers.Extensions.Print3DWorkflow, win32more.Windows.Devices.Printers.Extensions.Print3DWorkflowPrinterChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PrinterChanged(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IPrint3DWorkflowPrintRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.IPrint3DWorkflowPrintRequestedEventArgs'
    _iid_ = Guid('{19f8c858-5ac8-4b55-8a5f-e61567dafb4d}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Printers.Extensions.Print3DWorkflowStatus: ...
    @winrt_commethod(7)
    def SetExtendedStatus(self, value: win32more.Windows.Devices.Printers.Extensions.Print3DWorkflowDetail) -> Void: ...
    @winrt_commethod(8)
    def SetSource(self, source: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(9)
    def SetSourceChanged(self, value: Boolean) -> Void: ...
    Status = property(get_Status, None)
class IPrint3DWorkflowPrinterChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.IPrint3DWorkflowPrinterChangedEventArgs'
    _iid_ = Guid('{45226402-95fc-4847-93b3-134dbf5c60f7}')
    @winrt_commethod(6)
    def get_NewDeviceId(self) -> WinRT_String: ...
    NewDeviceId = property(get_NewDeviceId, None)
class IPrintExtensionContextStatic(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.IPrintExtensionContextStatic'
    _iid_ = Guid('{e70d9fc1-ff79-4aa4-8c9b-0c93aedfde8a}')
    @winrt_commethod(6)
    def FromDeviceId(self, deviceId: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class IPrintNotificationEventDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.IPrintNotificationEventDetails'
    _iid_ = Guid('{e00e4c8a-4828-4da1-8bb8-8672df8515e7}')
    @winrt_commethod(6)
    def get_PrinterName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EventData(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_EventData(self, value: WinRT_String) -> Void: ...
    PrinterName = property(get_PrinterName, None)
    EventData = property(get_EventData, put_EventData)
class IPrintTaskConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.IPrintTaskConfiguration'
    _iid_ = Guid('{e3c22451-3aa4-4885-9240-311f5f8fbe9d}')
    @winrt_commethod(6)
    def get_PrinterExtensionContext(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def add_SaveRequested(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Printers.Extensions.PrintTaskConfiguration, win32more.Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_SaveRequested(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PrinterExtensionContext = property(get_PrinterExtensionContext, None)
class IPrintTaskConfigurationSaveRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequest'
    _iid_ = Guid('{eeaf2fcb-621e-4b62-ac77-b281cce08d60}')
    @winrt_commethod(6)
    def Cancel(self) -> Void: ...
    @winrt_commethod(7)
    def Save(self, printerExtensionContext: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequestedDeferral: ...
    @winrt_commethod(9)
    def get_Deadline(self) -> win32more.Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
class IPrintTaskConfigurationSaveRequestedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequestedDeferral'
    _iid_ = Guid('{e959d568-f729-44a4-871d-bd0628696a33}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IPrintTaskConfigurationSaveRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequestedEventArgs'
    _iid_ = Guid('{e06c2879-0d61-4938-91d0-96a45bee8479}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequest: ...
    Request = property(get_Request, None)
class Print3DWorkflow(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Printers.Extensions.IPrint3DWorkflow
    _classid_ = 'Windows.Devices.Printers.Extensions.Print3DWorkflow'
    @winrt_mixinmethod
    def get_DeviceID(self: win32more.Windows.Devices.Printers.Extensions.IPrint3DWorkflow) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetPrintModelPackage(self: win32more.Windows.Devices.Printers.Extensions.IPrint3DWorkflow) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_IsPrintReady(self: win32more.Windows.Devices.Printers.Extensions.IPrint3DWorkflow) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPrintReady(self: win32more.Windows.Devices.Printers.Extensions.IPrint3DWorkflow, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_PrintRequested(self: win32more.Windows.Devices.Printers.Extensions.IPrint3DWorkflow, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Printers.Extensions.Print3DWorkflow, win32more.Windows.Devices.Printers.Extensions.Print3DWorkflowPrintRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrintRequested(self: win32more.Windows.Devices.Printers.Extensions.IPrint3DWorkflow, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PrinterChanged(self: win32more.Windows.Devices.Printers.Extensions.IPrint3DWorkflow2, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Printers.Extensions.Print3DWorkflow, win32more.Windows.Devices.Printers.Extensions.Print3DWorkflowPrinterChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrinterChanged(self: win32more.Windows.Devices.Printers.Extensions.IPrint3DWorkflow2, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceID = property(get_DeviceID, None)
    IsPrintReady = property(get_IsPrintReady, put_IsPrintReady)
Print3DWorkflowDetail = Int32
Print3DWorkflowDetail_Unknown: Print3DWorkflowDetail = 0
Print3DWorkflowDetail_ModelExceedsPrintBed: Print3DWorkflowDetail = 1
Print3DWorkflowDetail_UploadFailed: Print3DWorkflowDetail = 2
Print3DWorkflowDetail_InvalidMaterialSelection: Print3DWorkflowDetail = 3
Print3DWorkflowDetail_InvalidModel: Print3DWorkflowDetail = 4
Print3DWorkflowDetail_ModelNotManifold: Print3DWorkflowDetail = 5
Print3DWorkflowDetail_InvalidPrintTicket: Print3DWorkflowDetail = 6
class Print3DWorkflowPrintRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Printers.Extensions.IPrint3DWorkflowPrintRequestedEventArgs
    _classid_ = 'Windows.Devices.Printers.Extensions.Print3DWorkflowPrintRequestedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Printers.Extensions.IPrint3DWorkflowPrintRequestedEventArgs) -> win32more.Windows.Devices.Printers.Extensions.Print3DWorkflowStatus: ...
    @winrt_mixinmethod
    def SetExtendedStatus(self: win32more.Windows.Devices.Printers.Extensions.IPrint3DWorkflowPrintRequestedEventArgs, value: win32more.Windows.Devices.Printers.Extensions.Print3DWorkflowDetail) -> Void: ...
    @winrt_mixinmethod
    def SetSource(self: win32more.Windows.Devices.Printers.Extensions.IPrint3DWorkflowPrintRequestedEventArgs, source: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def SetSourceChanged(self: win32more.Windows.Devices.Printers.Extensions.IPrint3DWorkflowPrintRequestedEventArgs, value: Boolean) -> Void: ...
    Status = property(get_Status, None)
class Print3DWorkflowPrinterChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Printers.Extensions.IPrint3DWorkflowPrinterChangedEventArgs
    _classid_ = 'Windows.Devices.Printers.Extensions.Print3DWorkflowPrinterChangedEventArgs'
    @winrt_mixinmethod
    def get_NewDeviceId(self: win32more.Windows.Devices.Printers.Extensions.IPrint3DWorkflowPrinterChangedEventArgs) -> WinRT_String: ...
    NewDeviceId = property(get_NewDeviceId, None)
Print3DWorkflowStatus = Int32
Print3DWorkflowStatus_Abandoned: Print3DWorkflowStatus = 0
Print3DWorkflowStatus_Canceled: Print3DWorkflowStatus = 1
Print3DWorkflowStatus_Failed: Print3DWorkflowStatus = 2
Print3DWorkflowStatus_Slicing: Print3DWorkflowStatus = 3
Print3DWorkflowStatus_Submitted: Print3DWorkflowStatus = 4
class PrintExtensionContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.PrintExtensionContext'
    @winrt_classmethod
    def FromDeviceId(cls: win32more.Windows.Devices.Printers.Extensions.IPrintExtensionContextStatic, deviceId: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class PrintNotificationEventDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Printers.Extensions.IPrintNotificationEventDetails
    _classid_ = 'Windows.Devices.Printers.Extensions.PrintNotificationEventDetails'
    @winrt_mixinmethod
    def get_PrinterName(self: win32more.Windows.Devices.Printers.Extensions.IPrintNotificationEventDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EventData(self: win32more.Windows.Devices.Printers.Extensions.IPrintNotificationEventDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_EventData(self: win32more.Windows.Devices.Printers.Extensions.IPrintNotificationEventDetails, value: WinRT_String) -> Void: ...
    PrinterName = property(get_PrinterName, None)
    EventData = property(get_EventData, put_EventData)
class PrintTaskConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Printers.Extensions.IPrintTaskConfiguration
    _classid_ = 'Windows.Devices.Printers.Extensions.PrintTaskConfiguration'
    @winrt_mixinmethod
    def get_PrinterExtensionContext(self: win32more.Windows.Devices.Printers.Extensions.IPrintTaskConfiguration) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def add_SaveRequested(self: win32more.Windows.Devices.Printers.Extensions.IPrintTaskConfiguration, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Printers.Extensions.PrintTaskConfiguration, win32more.Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SaveRequested(self: win32more.Windows.Devices.Printers.Extensions.IPrintTaskConfiguration, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PrinterExtensionContext = property(get_PrinterExtensionContext, None)
class PrintTaskConfigurationSaveRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequest
    _classid_ = 'Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequest'
    @winrt_mixinmethod
    def Cancel(self: win32more.Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequest) -> Void: ...
    @winrt_mixinmethod
    def Save(self: win32more.Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequest, printerExtensionContext: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequest) -> win32more.Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequestedDeferral: ...
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequest) -> win32more.Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
class PrintTaskConfigurationSaveRequestedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequestedDeferral
    _classid_ = 'Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequestedDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequestedDeferral) -> Void: ...
class PrintTaskConfigurationSaveRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequestedEventArgs
    _classid_ = 'Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequestedEventArgs) -> win32more.Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequest: ...
    Request = property(get_Request, None)
make_ready(__name__)
