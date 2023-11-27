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
import win32more.Windows.ApplicationModel.Contacts
import win32more.Windows.ApplicationModel.Contacts.DataProvider
import win32more.Windows.Foundation
class ContactDataProviderConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection'
    @winrt_mixinmethod
    def add_SyncRequested(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection, win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactListSyncManagerSyncRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SyncRequested(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ServerSearchReadBatchRequested(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection, win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactListServerSearchReadBatchRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServerSearchReadBatchRequested(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection) -> Void: ...
    @winrt_mixinmethod
    def add_CreateOrUpdateContactRequested(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection, win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactListCreateOrUpdateContactRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CreateOrUpdateContactRequested(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DeleteContactRequested(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection, win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactListDeleteContactRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DeleteContactRequested(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class ContactDataProviderTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderTriggerDetails'
    @winrt_mixinmethod
    def get_Connection(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderTriggerDetails) -> win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection: ...
    Connection = property(get_Connection, None)
class ContactListCreateOrUpdateContactRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequest
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactListCreateOrUpdateContactRequest'
    @winrt_mixinmethod
    def get_ContactListId(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequest) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequest, createdOrUpdatedContact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    ContactListId = property(get_ContactListId, None)
    Contact = property(get_Contact, None)
class ContactListCreateOrUpdateContactRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactListCreateOrUpdateContactRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequestEventArgs) -> win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactListCreateOrUpdateContactRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class ContactListDeleteContactRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequest
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactListDeleteContactRequest'
    @winrt_mixinmethod
    def get_ContactListId(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContactId(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    ContactListId = property(get_ContactListId, None)
    ContactId = property(get_ContactId, None)
class ContactListDeleteContactRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactListDeleteContactRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequestEventArgs) -> win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactListDeleteContactRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class ContactListServerSearchReadBatchRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactListServerSearchReadBatchRequest'
    @winrt_mixinmethod
    def get_SessionId(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContactListId(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Options(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest) -> win32more.Windows.ApplicationModel.Contacts.ContactQueryOptions: ...
    @winrt_mixinmethod
    def get_SuggestedBatchSize(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest) -> UInt32: ...
    @winrt_mixinmethod
    def SaveContactAsync(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest, batchStatus: win32more.Windows.ApplicationModel.Contacts.ContactBatchStatus) -> win32more.Windows.Foundation.IAsyncAction: ...
    SessionId = property(get_SessionId, None)
    ContactListId = property(get_ContactListId, None)
    Options = property(get_Options, None)
    SuggestedBatchSize = property(get_SuggestedBatchSize, None)
class ContactListServerSearchReadBatchRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactListServerSearchReadBatchRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequestEventArgs) -> win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactListServerSearchReadBatchRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class ContactListSyncManagerSyncRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListSyncManagerSyncRequest
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactListSyncManagerSyncRequest'
    @winrt_mixinmethod
    def get_ContactListId(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListSyncManagerSyncRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListSyncManagerSyncRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListSyncManagerSyncRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    ContactListId = property(get_ContactListId, None)
class ContactListSyncManagerSyncRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListSyncManagerSyncRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.ContactListSyncManagerSyncRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListSyncManagerSyncRequestEventArgs) -> win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactListSyncManagerSyncRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Contacts.DataProvider.IContactListSyncManagerSyncRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IContactDataProviderConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection'
    _iid_ = Guid('{1a398a52-8c9d-4d6f-a4e0-111e9a125a30}')
    @winrt_commethod(6)
    def add_SyncRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection, win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactListSyncManagerSyncRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SyncRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ServerSearchReadBatchRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection, win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactListServerSearchReadBatchRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ServerSearchReadBatchRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def Start(self) -> Void: ...
class IContactDataProviderConnection2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderConnection2'
    _iid_ = Guid('{a1d327b0-196c-4bfd-8f0f-c68d67f249d3}')
    @winrt_commethod(6)
    def add_CreateOrUpdateContactRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection, win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactListCreateOrUpdateContactRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CreateOrUpdateContactRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_DeleteContactRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection, win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactListDeleteContactRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_DeleteContactRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IContactDataProviderTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.IContactDataProviderTriggerDetails'
    _iid_ = Guid('{527104be-3c62-43c8-9ae7-db531685cd99}')
    @winrt_commethod(6)
    def get_Connection(self) -> win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactDataProviderConnection: ...
    Connection = property(get_Connection, None)
class IContactListCreateOrUpdateContactRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequest'
    _iid_ = Guid('{b4af411f-c849-47d0-b119-91cf605b2f2a}')
    @winrt_commethod(6)
    def get_ContactListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Contact(self) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self, createdOrUpdatedContact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    ContactListId = property(get_ContactListId, None)
    Contact = property(get_Contact, None)
class IContactListCreateOrUpdateContactRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.IContactListCreateOrUpdateContactRequestEventArgs'
    _iid_ = Guid('{851c1690-1a51-4b0c-aeef-1240ac5bed75}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactListCreateOrUpdateContactRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IContactListDeleteContactRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequest'
    _iid_ = Guid('{5e114687-ce03-4de5-8557-9ccf552d472a}')
    @winrt_commethod(6)
    def get_ContactListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ContactId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    ContactListId = property(get_ContactListId, None)
    ContactId = property(get_ContactId, None)
class IContactListDeleteContactRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.IContactListDeleteContactRequestEventArgs'
    _iid_ = Guid('{b22054a1-e8fa-4db5-9389-2d12ee7d15ee}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactListDeleteContactRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IContactListServerSearchReadBatchRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequest'
    _iid_ = Guid('{ba776a97-4030-4925-9fb4-143b295e653b}')
    @winrt_commethod(6)
    def get_SessionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ContactListId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Options(self) -> win32more.Windows.ApplicationModel.Contacts.ContactQueryOptions: ...
    @winrt_commethod(9)
    def get_SuggestedBatchSize(self) -> UInt32: ...
    @winrt_commethod(10)
    def SaveContactAsync(self, contact: win32more.Windows.ApplicationModel.Contacts.Contact) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def ReportFailedAsync(self, batchStatus: win32more.Windows.ApplicationModel.Contacts.ContactBatchStatus) -> win32more.Windows.Foundation.IAsyncAction: ...
    SessionId = property(get_SessionId, None)
    ContactListId = property(get_ContactListId, None)
    Options = property(get_Options, None)
    SuggestedBatchSize = property(get_SuggestedBatchSize, None)
class IContactListServerSearchReadBatchRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.IContactListServerSearchReadBatchRequestEventArgs'
    _iid_ = Guid('{1a27e87b-69d7-4e4e-8042-861cba61471e}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactListServerSearchReadBatchRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IContactListSyncManagerSyncRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.IContactListSyncManagerSyncRequest'
    _iid_ = Guid('{3c0e57a4-c4e7-4970-9a8f-9a66a2bb6c1a}')
    @winrt_commethod(6)
    def get_ContactListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    ContactListId = property(get_ContactListId, None)
class IContactListSyncManagerSyncRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Contacts.DataProvider.IContactListSyncManagerSyncRequestEventArgs'
    _iid_ = Guid('{158e4dac-446d-4f10-afc2-02683ec533a6}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Contacts.DataProvider.ContactListSyncManagerSyncRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
make_ready(__name__)
