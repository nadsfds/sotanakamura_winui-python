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
import win32more.Windows.Media.Import
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
class IPhotoImportDeleteImportedItemsFromSourceResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult'
    _iid_ = Guid('{f4e112f8-843d-428a-a1a6-81510292b0ae}')
    @winrt_commethod(6)
    def get_Session(self) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_commethod(7)
    def get_HasSucceeded(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_DeletedItems(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportItem]: ...
    @winrt_commethod(9)
    def get_PhotosCount(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_PhotosSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(11)
    def get_VideosCount(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_VideosSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(13)
    def get_SidecarsCount(self) -> UInt32: ...
    @winrt_commethod(14)
    def get_SidecarsSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(15)
    def get_SiblingsCount(self) -> UInt32: ...
    @winrt_commethod(16)
    def get_SiblingsSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(17)
    def get_TotalCount(self) -> UInt32: ...
    @winrt_commethod(18)
    def get_TotalSizeInBytes(self) -> UInt64: ...
    Session = property(get_Session, None)
    HasSucceeded = property(get_HasSucceeded, None)
    DeletedItems = property(get_DeletedItems, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
class IPhotoImportFindItemsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportFindItemsResult'
    _iid_ = Guid('{3915e647-6c78-492b-844e-8fe5e8f6bfb9}')
    @winrt_commethod(6)
    def get_Session(self) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_commethod(7)
    def get_HasSucceeded(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_FoundItems(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportItem]: ...
    @winrt_commethod(9)
    def get_PhotosCount(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_PhotosSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(11)
    def get_VideosCount(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_VideosSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(13)
    def get_SidecarsCount(self) -> UInt32: ...
    @winrt_commethod(14)
    def get_SidecarsSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(15)
    def get_SiblingsCount(self) -> UInt32: ...
    @winrt_commethod(16)
    def get_SiblingsSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(17)
    def get_TotalCount(self) -> UInt32: ...
    @winrt_commethod(18)
    def get_TotalSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(19)
    def SelectAll(self) -> Void: ...
    @winrt_commethod(20)
    def SelectNone(self) -> Void: ...
    @winrt_commethod(21)
    def SelectNewAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(22)
    def SetImportMode(self, value: win32more.Windows.Media.Import.PhotoImportImportMode) -> Void: ...
    @winrt_commethod(23)
    def get_ImportMode(self) -> win32more.Windows.Media.Import.PhotoImportImportMode: ...
    @winrt_commethod(24)
    def get_SelectedPhotosCount(self) -> UInt32: ...
    @winrt_commethod(25)
    def get_SelectedPhotosSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(26)
    def get_SelectedVideosCount(self) -> UInt32: ...
    @winrt_commethod(27)
    def get_SelectedVideosSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(28)
    def get_SelectedSidecarsCount(self) -> UInt32: ...
    @winrt_commethod(29)
    def get_SelectedSidecarsSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(30)
    def get_SelectedSiblingsCount(self) -> UInt32: ...
    @winrt_commethod(31)
    def get_SelectedSiblingsSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(32)
    def get_SelectedTotalCount(self) -> UInt32: ...
    @winrt_commethod(33)
    def get_SelectedTotalSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(34)
    def add_SelectionChanged(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Import.PhotoImportFindItemsResult, win32more.Windows.Media.Import.PhotoImportSelectionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(35)
    def remove_SelectionChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(36)
    def ImportItemsAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportImportItemsResult, win32more.Windows.Media.Import.PhotoImportProgress]: ...
    @winrt_commethod(37)
    def add_ItemImported(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Import.PhotoImportFindItemsResult, win32more.Windows.Media.Import.PhotoImportItemImportedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(38)
    def remove_ItemImported(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Session = property(get_Session, None)
    HasSucceeded = property(get_HasSucceeded, None)
    FoundItems = property(get_FoundItems, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
    ImportMode = property(get_ImportMode, None)
    SelectedPhotosCount = property(get_SelectedPhotosCount, None)
    SelectedPhotosSizeInBytes = property(get_SelectedPhotosSizeInBytes, None)
    SelectedVideosCount = property(get_SelectedVideosCount, None)
    SelectedVideosSizeInBytes = property(get_SelectedVideosSizeInBytes, None)
    SelectedSidecarsCount = property(get_SelectedSidecarsCount, None)
    SelectedSidecarsSizeInBytes = property(get_SelectedSidecarsSizeInBytes, None)
    SelectedSiblingsCount = property(get_SelectedSiblingsCount, None)
    SelectedSiblingsSizeInBytes = property(get_SelectedSiblingsSizeInBytes, None)
    SelectedTotalCount = property(get_SelectedTotalCount, None)
    SelectedTotalSizeInBytes = property(get_SelectedTotalSizeInBytes, None)
class IPhotoImportFindItemsResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportFindItemsResult2'
    _iid_ = Guid('{fbdd6a3b-ecf9-406a-815e-5015625b0a88}')
    @winrt_commethod(6)
    def AddItemsInDateRangeToSelection(self, rangeStart: win32more.Windows.Foundation.DateTime, rangeLength: win32more.Windows.Foundation.TimeSpan) -> Void: ...
class IPhotoImportImportItemsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportImportItemsResult'
    _iid_ = Guid('{e4d4f478-d419-4443-a84e-f06a850c0b00}')
    @winrt_commethod(6)
    def get_Session(self) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_commethod(7)
    def get_HasSucceeded(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ImportedItems(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportItem]: ...
    @winrt_commethod(9)
    def get_PhotosCount(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_PhotosSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(11)
    def get_VideosCount(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_VideosSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(13)
    def get_SidecarsCount(self) -> UInt32: ...
    @winrt_commethod(14)
    def get_SidecarsSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(15)
    def get_SiblingsCount(self) -> UInt32: ...
    @winrt_commethod(16)
    def get_SiblingsSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(17)
    def get_TotalCount(self) -> UInt32: ...
    @winrt_commethod(18)
    def get_TotalSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(19)
    def DeleteImportedItemsFromSourceAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportDeleteImportedItemsFromSourceResult, Double]: ...
    Session = property(get_Session, None)
    HasSucceeded = property(get_HasSucceeded, None)
    ImportedItems = property(get_ImportedItems, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
class IPhotoImportItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportItem'
    _iid_ = Guid('{a9d07e76-9bfc-43b8-b356-633b6a988c9e}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ItemKey(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_ContentType(self) -> win32more.Windows.Media.Import.PhotoImportContentType: ...
    @winrt_commethod(9)
    def get_SizeInBytes(self) -> UInt64: ...
    @winrt_commethod(10)
    def get_Date(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(11)
    def get_Sibling(self) -> win32more.Windows.Media.Import.PhotoImportSidecar: ...
    @winrt_commethod(12)
    def get_Sidecars(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportSidecar]: ...
    @winrt_commethod(13)
    def get_VideoSegments(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportVideoSegment]: ...
    @winrt_commethod(14)
    def get_IsSelected(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsSelected(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_Thumbnail(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(17)
    def get_ImportedFileNames(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(18)
    def get_DeletedFileNames(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    Name = property(get_Name, None)
    ItemKey = property(get_ItemKey, None)
    ContentType = property(get_ContentType, None)
    SizeInBytes = property(get_SizeInBytes, None)
    Date = property(get_Date, None)
    Sibling = property(get_Sibling, None)
    Sidecars = property(get_Sidecars, None)
    VideoSegments = property(get_VideoSegments, None)
    IsSelected = property(get_IsSelected, put_IsSelected)
    Thumbnail = property(get_Thumbnail, None)
    ImportedFileNames = property(get_ImportedFileNames, None)
    DeletedFileNames = property(get_DeletedFileNames, None)
class IPhotoImportItem2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportItem2'
    _iid_ = Guid('{f1053505-f53b-46a3-9e30-3610791a9110}')
    @winrt_commethod(6)
    def get_Path(self) -> WinRT_String: ...
    Path = property(get_Path, None)
class IPhotoImportItemImportedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportItemImportedEventArgs'
    _iid_ = Guid('{42cb2fdd-7d68-47b5-bc7c-ceb73e0c77dc}')
    @winrt_commethod(6)
    def get_ImportedItem(self) -> win32more.Windows.Media.Import.PhotoImportItem: ...
    ImportedItem = property(get_ImportedItem, None)
class IPhotoImportManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportManagerStatics'
    _iid_ = Guid('{2771903d-a046-4f06-9b9c-bfd662e83287}')
    @winrt_commethod(6)
    def IsSupportedAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def FindAllSourcesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportSource]]: ...
    @winrt_commethod(8)
    def GetPendingOperations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportOperation]: ...
class IPhotoImportOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportOperation'
    _iid_ = Guid('{d9f797e4-a09a-4ee4-a4b1-20940277a5be}')
    @winrt_commethod(6)
    def get_Stage(self) -> win32more.Windows.Media.Import.PhotoImportStage: ...
    @winrt_commethod(7)
    def get_Session(self) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_commethod(8)
    def get_ContinueFindingItemsAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportFindItemsResult, UInt32]: ...
    @winrt_commethod(9)
    def get_ContinueImportingItemsAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportImportItemsResult, win32more.Windows.Media.Import.PhotoImportProgress]: ...
    @winrt_commethod(10)
    def get_ContinueDeletingImportedItemsFromSourceAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportDeleteImportedItemsFromSourceResult, Double]: ...
    Stage = property(get_Stage, None)
    Session = property(get_Session, None)
    ContinueFindingItemsAsync = property(get_ContinueFindingItemsAsync, None)
    ContinueImportingItemsAsync = property(get_ContinueImportingItemsAsync, None)
    ContinueDeletingImportedItemsFromSourceAsync = property(get_ContinueDeletingImportedItemsFromSourceAsync, None)
class IPhotoImportSelectionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportSelectionChangedEventArgs'
    _iid_ = Guid('{10461782-fa9d-4c30-8bc9-4d64911572d5}')
    @winrt_commethod(6)
    def get_IsSelectionEmpty(self) -> Boolean: ...
    IsSelectionEmpty = property(get_IsSelectionEmpty, None)
class IPhotoImportSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportSession'
    _iid_ = Guid('{aa63916e-ecdb-4efe-94c6-5f5cafe34cfb}')
    @winrt_commethod(6)
    def get_Source(self) -> win32more.Windows.Media.Import.PhotoImportSource: ...
    @winrt_commethod(7)
    def get_SessionId(self) -> Guid: ...
    @winrt_commethod(8)
    def put_DestinationFolder(self, value: win32more.Windows.Storage.IStorageFolder) -> Void: ...
    @winrt_commethod(9)
    def get_DestinationFolder(self) -> win32more.Windows.Storage.IStorageFolder: ...
    @winrt_commethod(10)
    def put_AppendSessionDateToDestinationFolder(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_AppendSessionDateToDestinationFolder(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_SubfolderCreationMode(self, value: win32more.Windows.Media.Import.PhotoImportSubfolderCreationMode) -> Void: ...
    @winrt_commethod(13)
    def get_SubfolderCreationMode(self) -> win32more.Windows.Media.Import.PhotoImportSubfolderCreationMode: ...
    @winrt_commethod(14)
    def put_DestinationFileNamePrefix(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_DestinationFileNamePrefix(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def FindItemsAsync(self, contentTypeFilter: win32more.Windows.Media.Import.PhotoImportContentTypeFilter, itemSelectionMode: win32more.Windows.Media.Import.PhotoImportItemSelectionMode) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportFindItemsResult, UInt32]: ...
    Source = property(get_Source, None)
    SessionId = property(get_SessionId, None)
    DestinationFolder = property(get_DestinationFolder, put_DestinationFolder)
    AppendSessionDateToDestinationFolder = property(get_AppendSessionDateToDestinationFolder, put_AppendSessionDateToDestinationFolder)
    SubfolderCreationMode = property(get_SubfolderCreationMode, put_SubfolderCreationMode)
    DestinationFileNamePrefix = property(get_DestinationFileNamePrefix, put_DestinationFileNamePrefix)
class IPhotoImportSession2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportSession2'
    _iid_ = Guid('{2a526710-3ec6-469d-a375-2b9f4785391e}')
    @winrt_commethod(6)
    def put_SubfolderDateFormat(self, value: win32more.Windows.Media.Import.PhotoImportSubfolderDateFormat) -> Void: ...
    @winrt_commethod(7)
    def get_SubfolderDateFormat(self) -> win32more.Windows.Media.Import.PhotoImportSubfolderDateFormat: ...
    @winrt_commethod(8)
    def put_RememberDeselectedItems(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_RememberDeselectedItems(self) -> Boolean: ...
    SubfolderDateFormat = property(get_SubfolderDateFormat, put_SubfolderDateFormat)
    RememberDeselectedItems = property(get_RememberDeselectedItems, put_RememberDeselectedItems)
class IPhotoImportSidecar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportSidecar'
    _iid_ = Guid('{46d7d757-f802-44c7-9c98-7a71f4bc1486}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SizeInBytes(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_Date(self) -> win32more.Windows.Foundation.DateTime: ...
    Name = property(get_Name, None)
    SizeInBytes = property(get_SizeInBytes, None)
    Date = property(get_Date, None)
class IPhotoImportSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportSource'
    _iid_ = Guid('{1f8ea35e-145b-4cd6-87f1-54965a982fef}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Manufacturer(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Model(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_SerialNumber(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_ConnectionProtocol(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_ConnectionTransport(self) -> win32more.Windows.Media.Import.PhotoImportConnectionTransport: ...
    @winrt_commethod(14)
    def get_Type(self) -> win32more.Windows.Media.Import.PhotoImportSourceType: ...
    @winrt_commethod(15)
    def get_PowerSource(self) -> win32more.Windows.Media.Import.PhotoImportPowerSource: ...
    @winrt_commethod(16)
    def get_BatteryLevelPercent(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(17)
    def get_DateTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(18)
    def get_StorageMedia(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportStorageMedium]: ...
    @winrt_commethod(19)
    def get_IsLocked(self) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(20)
    def get_IsMassStorage(self) -> Boolean: ...
    @winrt_commethod(21)
    def get_Thumbnail(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(22)
    def CreateImportSession(self) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    Description = property(get_Description, None)
    Manufacturer = property(get_Manufacturer, None)
    Model = property(get_Model, None)
    SerialNumber = property(get_SerialNumber, None)
    ConnectionProtocol = property(get_ConnectionProtocol, None)
    ConnectionTransport = property(get_ConnectionTransport, None)
    Type = property(get_Type, None)
    PowerSource = property(get_PowerSource, None)
    BatteryLevelPercent = property(get_BatteryLevelPercent, None)
    DateTime = property(get_DateTime, None)
    StorageMedia = property(get_StorageMedia, None)
    IsLocked = property(get_IsLocked, None)
    IsMassStorage = property(get_IsMassStorage, None)
    Thumbnail = property(get_Thumbnail, None)
class IPhotoImportSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportSourceStatics'
    _iid_ = Guid('{0528e586-32d8-467c-8cee-23a1b2f43e85}')
    @winrt_commethod(6)
    def FromIdAsync(self, sourceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Import.PhotoImportSource]: ...
    @winrt_commethod(7)
    def FromFolderAsync(self, sourceRootFolder: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Import.PhotoImportSource]: ...
class IPhotoImportStorageMedium(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportStorageMedium'
    _iid_ = Guid('{f2b9b093-fc85-487f-87c2-58d675d05b07}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SerialNumber(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_StorageMediumType(self) -> win32more.Windows.Media.Import.PhotoImportStorageMediumType: ...
    @winrt_commethod(10)
    def get_SupportedAccessMode(self) -> win32more.Windows.Media.Import.PhotoImportAccessMode: ...
    @winrt_commethod(11)
    def get_CapacityInBytes(self) -> UInt64: ...
    @winrt_commethod(12)
    def get_AvailableSpaceInBytes(self) -> UInt64: ...
    @winrt_commethod(13)
    def Refresh(self) -> Void: ...
    Name = property(get_Name, None)
    Description = property(get_Description, None)
    SerialNumber = property(get_SerialNumber, None)
    StorageMediumType = property(get_StorageMediumType, None)
    SupportedAccessMode = property(get_SupportedAccessMode, None)
    CapacityInBytes = property(get_CapacityInBytes, None)
    AvailableSpaceInBytes = property(get_AvailableSpaceInBytes, None)
class IPhotoImportVideoSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.IPhotoImportVideoSegment'
    _iid_ = Guid('{623c0289-321a-41d8-9166-8c62a333276c}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SizeInBytes(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_Date(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def get_Sibling(self) -> win32more.Windows.Media.Import.PhotoImportSidecar: ...
    @winrt_commethod(10)
    def get_Sidecars(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportSidecar]: ...
    Name = property(get_Name, None)
    SizeInBytes = property(get_SizeInBytes, None)
    Date = property(get_Date, None)
    Sibling = property(get_Sibling, None)
    Sidecars = property(get_Sidecars, None)
PhotoImportAccessMode = Int32
PhotoImportAccessMode_ReadWrite: PhotoImportAccessMode = 0
PhotoImportAccessMode_ReadOnly: PhotoImportAccessMode = 1
PhotoImportAccessMode_ReadAndDelete: PhotoImportAccessMode = 2
PhotoImportConnectionTransport = Int32
PhotoImportConnectionTransport_Unknown: PhotoImportConnectionTransport = 0
PhotoImportConnectionTransport_Usb: PhotoImportConnectionTransport = 1
PhotoImportConnectionTransport_IP: PhotoImportConnectionTransport = 2
PhotoImportConnectionTransport_Bluetooth: PhotoImportConnectionTransport = 3
PhotoImportContentType = Int32
PhotoImportContentType_Unknown: PhotoImportContentType = 0
PhotoImportContentType_Image: PhotoImportContentType = 1
PhotoImportContentType_Video: PhotoImportContentType = 2
PhotoImportContentTypeFilter = Int32
PhotoImportContentTypeFilter_OnlyImages: PhotoImportContentTypeFilter = 0
PhotoImportContentTypeFilter_OnlyVideos: PhotoImportContentTypeFilter = 1
PhotoImportContentTypeFilter_ImagesAndVideos: PhotoImportContentTypeFilter = 2
PhotoImportContentTypeFilter_ImagesAndVideosFromCameraRoll: PhotoImportContentTypeFilter = 3
class PhotoImportDeleteImportedItemsFromSourceResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult
    _classid_ = 'Windows.Media.Import.PhotoImportDeleteImportedItemsFromSourceResult'
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_mixinmethod
    def get_HasSucceeded(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_DeletedItems(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportItem]: ...
    @winrt_mixinmethod
    def get_PhotosCount(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_PhotosSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_VideosCount(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_VideosSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SidecarsCount(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SidecarsSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SiblingsCount(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SiblingsSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalCount(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_TotalSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportDeleteImportedItemsFromSourceResult) -> UInt64: ...
    Session = property(get_Session, None)
    HasSucceeded = property(get_HasSucceeded, None)
    DeletedItems = property(get_DeletedItems, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
class PhotoImportFindItemsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportFindItemsResult
    _classid_ = 'Windows.Media.Import.PhotoImportFindItemsResult'
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_mixinmethod
    def get_HasSucceeded(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_FoundItems(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportItem]: ...
    @winrt_mixinmethod
    def get_PhotosCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_PhotosSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_VideosCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_VideosSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SidecarsCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SidecarsSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SiblingsCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SiblingsSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_TotalSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def SelectAll(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> Void: ...
    @winrt_mixinmethod
    def SelectNone(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> Void: ...
    @winrt_mixinmethod
    def SelectNewAsync(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetImportMode(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult, value: win32more.Windows.Media.Import.PhotoImportImportMode) -> Void: ...
    @winrt_mixinmethod
    def get_ImportMode(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> win32more.Windows.Media.Import.PhotoImportImportMode: ...
    @winrt_mixinmethod
    def get_SelectedPhotosCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelectedPhotosSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SelectedVideosCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelectedVideosSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SelectedSidecarsCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelectedSidecarsSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SelectedSiblingsCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelectedSiblingsSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SelectedTotalCount(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelectedTotalSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def add_SelectionChanged(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Import.PhotoImportFindItemsResult, win32more.Windows.Media.Import.PhotoImportSelectionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SelectionChanged(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ImportItemsAsync(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportImportItemsResult, win32more.Windows.Media.Import.PhotoImportProgress]: ...
    @winrt_mixinmethod
    def add_ItemImported(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Import.PhotoImportFindItemsResult, win32more.Windows.Media.Import.PhotoImportItemImportedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ItemImported(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddItemsInDateRangeToSelection(self: win32more.Windows.Media.Import.IPhotoImportFindItemsResult2, rangeStart: win32more.Windows.Foundation.DateTime, rangeLength: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    Session = property(get_Session, None)
    HasSucceeded = property(get_HasSucceeded, None)
    FoundItems = property(get_FoundItems, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
    ImportMode = property(get_ImportMode, None)
    SelectedPhotosCount = property(get_SelectedPhotosCount, None)
    SelectedPhotosSizeInBytes = property(get_SelectedPhotosSizeInBytes, None)
    SelectedVideosCount = property(get_SelectedVideosCount, None)
    SelectedVideosSizeInBytes = property(get_SelectedVideosSizeInBytes, None)
    SelectedSidecarsCount = property(get_SelectedSidecarsCount, None)
    SelectedSidecarsSizeInBytes = property(get_SelectedSidecarsSizeInBytes, None)
    SelectedSiblingsCount = property(get_SelectedSiblingsCount, None)
    SelectedSiblingsSizeInBytes = property(get_SelectedSiblingsSizeInBytes, None)
    SelectedTotalCount = property(get_SelectedTotalCount, None)
    SelectedTotalSizeInBytes = property(get_SelectedTotalSizeInBytes, None)
class PhotoImportImportItemsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportImportItemsResult
    _classid_ = 'Windows.Media.Import.PhotoImportImportItemsResult'
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_mixinmethod
    def get_HasSucceeded(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ImportedItems(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportItem]: ...
    @winrt_mixinmethod
    def get_PhotosCount(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_PhotosSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_VideosCount(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_VideosSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SidecarsCount(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SidecarsSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SiblingsCount(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_SiblingsSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_TotalCount(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_TotalSizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> UInt64: ...
    @winrt_mixinmethod
    def DeleteImportedItemsFromSourceAsync(self: win32more.Windows.Media.Import.IPhotoImportImportItemsResult) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportDeleteImportedItemsFromSourceResult, Double]: ...
    Session = property(get_Session, None)
    HasSucceeded = property(get_HasSucceeded, None)
    ImportedItems = property(get_ImportedItems, None)
    PhotosCount = property(get_PhotosCount, None)
    PhotosSizeInBytes = property(get_PhotosSizeInBytes, None)
    VideosCount = property(get_VideosCount, None)
    VideosSizeInBytes = property(get_VideosSizeInBytes, None)
    SidecarsCount = property(get_SidecarsCount, None)
    SidecarsSizeInBytes = property(get_SidecarsSizeInBytes, None)
    SiblingsCount = property(get_SiblingsCount, None)
    SiblingsSizeInBytes = property(get_SiblingsSizeInBytes, None)
    TotalCount = property(get_TotalCount, None)
    TotalSizeInBytes = property(get_TotalSizeInBytes, None)
PhotoImportImportMode = Int32
PhotoImportImportMode_ImportEverything: PhotoImportImportMode = 0
PhotoImportImportMode_IgnoreSidecars: PhotoImportImportMode = 1
PhotoImportImportMode_IgnoreSiblings: PhotoImportImportMode = 2
PhotoImportImportMode_IgnoreSidecarsAndSiblings: PhotoImportImportMode = 3
class PhotoImportItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportItem
    _classid_ = 'Windows.Media.Import.PhotoImportItem'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Import.IPhotoImportItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ItemKey(self: win32more.Windows.Media.Import.IPhotoImportItem) -> UInt64: ...
    @winrt_mixinmethod
    def get_ContentType(self: win32more.Windows.Media.Import.IPhotoImportItem) -> win32more.Windows.Media.Import.PhotoImportContentType: ...
    @winrt_mixinmethod
    def get_SizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportItem) -> UInt64: ...
    @winrt_mixinmethod
    def get_Date(self: win32more.Windows.Media.Import.IPhotoImportItem) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Sibling(self: win32more.Windows.Media.Import.IPhotoImportItem) -> win32more.Windows.Media.Import.PhotoImportSidecar: ...
    @winrt_mixinmethod
    def get_Sidecars(self: win32more.Windows.Media.Import.IPhotoImportItem) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportSidecar]: ...
    @winrt_mixinmethod
    def get_VideoSegments(self: win32more.Windows.Media.Import.IPhotoImportItem) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportVideoSegment]: ...
    @winrt_mixinmethod
    def get_IsSelected(self: win32more.Windows.Media.Import.IPhotoImportItem) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSelected(self: win32more.Windows.Media.Import.IPhotoImportItem, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.Media.Import.IPhotoImportItem) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_ImportedFileNames(self: win32more.Windows.Media.Import.IPhotoImportItem) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DeletedFileNames(self: win32more.Windows.Media.Import.IPhotoImportItem) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Media.Import.IPhotoImportItem2) -> WinRT_String: ...
    Name = property(get_Name, None)
    ItemKey = property(get_ItemKey, None)
    ContentType = property(get_ContentType, None)
    SizeInBytes = property(get_SizeInBytes, None)
    Date = property(get_Date, None)
    Sibling = property(get_Sibling, None)
    Sidecars = property(get_Sidecars, None)
    VideoSegments = property(get_VideoSegments, None)
    IsSelected = property(get_IsSelected, put_IsSelected)
    Thumbnail = property(get_Thumbnail, None)
    ImportedFileNames = property(get_ImportedFileNames, None)
    DeletedFileNames = property(get_DeletedFileNames, None)
    Path = property(get_Path, None)
class PhotoImportItemImportedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportItemImportedEventArgs
    _classid_ = 'Windows.Media.Import.PhotoImportItemImportedEventArgs'
    @winrt_mixinmethod
    def get_ImportedItem(self: win32more.Windows.Media.Import.IPhotoImportItemImportedEventArgs) -> win32more.Windows.Media.Import.PhotoImportItem: ...
    ImportedItem = property(get_ImportedItem, None)
PhotoImportItemSelectionMode = Int32
PhotoImportItemSelectionMode_SelectAll: PhotoImportItemSelectionMode = 0
PhotoImportItemSelectionMode_SelectNone: PhotoImportItemSelectionMode = 1
PhotoImportItemSelectionMode_SelectNew: PhotoImportItemSelectionMode = 2
class PhotoImportManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Import.PhotoImportManager'
    @winrt_classmethod
    def IsSupportedAsync(cls: win32more.Windows.Media.Import.IPhotoImportManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def FindAllSourcesAsync(cls: win32more.Windows.Media.Import.IPhotoImportManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportSource]]: ...
    @winrt_classmethod
    def GetPendingOperations(cls: win32more.Windows.Media.Import.IPhotoImportManagerStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportOperation]: ...
class PhotoImportOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportOperation
    _classid_ = 'Windows.Media.Import.PhotoImportOperation'
    @winrt_mixinmethod
    def get_Stage(self: win32more.Windows.Media.Import.IPhotoImportOperation) -> win32more.Windows.Media.Import.PhotoImportStage: ...
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Media.Import.IPhotoImportOperation) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_mixinmethod
    def get_ContinueFindingItemsAsync(self: win32more.Windows.Media.Import.IPhotoImportOperation) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportFindItemsResult, UInt32]: ...
    @winrt_mixinmethod
    def get_ContinueImportingItemsAsync(self: win32more.Windows.Media.Import.IPhotoImportOperation) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportImportItemsResult, win32more.Windows.Media.Import.PhotoImportProgress]: ...
    @winrt_mixinmethod
    def get_ContinueDeletingImportedItemsFromSourceAsync(self: win32more.Windows.Media.Import.IPhotoImportOperation) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportDeleteImportedItemsFromSourceResult, Double]: ...
    Stage = property(get_Stage, None)
    Session = property(get_Session, None)
    ContinueFindingItemsAsync = property(get_ContinueFindingItemsAsync, None)
    ContinueImportingItemsAsync = property(get_ContinueImportingItemsAsync, None)
    ContinueDeletingImportedItemsFromSourceAsync = property(get_ContinueDeletingImportedItemsFromSourceAsync, None)
PhotoImportPowerSource = Int32
PhotoImportPowerSource_Unknown: PhotoImportPowerSource = 0
PhotoImportPowerSource_Battery: PhotoImportPowerSource = 1
PhotoImportPowerSource_External: PhotoImportPowerSource = 2
class PhotoImportProgress(EasyCastStructure):
    ItemsImported: UInt32
    TotalItemsToImport: UInt32
    BytesImported: UInt64
    TotalBytesToImport: UInt64
    ImportProgress: Double
class PhotoImportSelectionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportSelectionChangedEventArgs
    _classid_ = 'Windows.Media.Import.PhotoImportSelectionChangedEventArgs'
    @winrt_mixinmethod
    def get_IsSelectionEmpty(self: win32more.Windows.Media.Import.IPhotoImportSelectionChangedEventArgs) -> Boolean: ...
    IsSelectionEmpty = property(get_IsSelectionEmpty, None)
class PhotoImportSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportSession
    _classid_ = 'Windows.Media.Import.PhotoImportSession'
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Media.Import.IPhotoImportSession) -> win32more.Windows.Media.Import.PhotoImportSource: ...
    @winrt_mixinmethod
    def get_SessionId(self: win32more.Windows.Media.Import.IPhotoImportSession) -> Guid: ...
    @winrt_mixinmethod
    def put_DestinationFolder(self: win32more.Windows.Media.Import.IPhotoImportSession, value: win32more.Windows.Storage.IStorageFolder) -> Void: ...
    @winrt_mixinmethod
    def get_DestinationFolder(self: win32more.Windows.Media.Import.IPhotoImportSession) -> win32more.Windows.Storage.IStorageFolder: ...
    @winrt_mixinmethod
    def put_AppendSessionDateToDestinationFolder(self: win32more.Windows.Media.Import.IPhotoImportSession, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AppendSessionDateToDestinationFolder(self: win32more.Windows.Media.Import.IPhotoImportSession) -> Boolean: ...
    @winrt_mixinmethod
    def put_SubfolderCreationMode(self: win32more.Windows.Media.Import.IPhotoImportSession, value: win32more.Windows.Media.Import.PhotoImportSubfolderCreationMode) -> Void: ...
    @winrt_mixinmethod
    def get_SubfolderCreationMode(self: win32more.Windows.Media.Import.IPhotoImportSession) -> win32more.Windows.Media.Import.PhotoImportSubfolderCreationMode: ...
    @winrt_mixinmethod
    def put_DestinationFileNamePrefix(self: win32more.Windows.Media.Import.IPhotoImportSession, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DestinationFileNamePrefix(self: win32more.Windows.Media.Import.IPhotoImportSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def FindItemsAsync(self: win32more.Windows.Media.Import.IPhotoImportSession, contentTypeFilter: win32more.Windows.Media.Import.PhotoImportContentTypeFilter, itemSelectionMode: win32more.Windows.Media.Import.PhotoImportItemSelectionMode) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Import.PhotoImportFindItemsResult, UInt32]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def put_SubfolderDateFormat(self: win32more.Windows.Media.Import.IPhotoImportSession2, value: win32more.Windows.Media.Import.PhotoImportSubfolderDateFormat) -> Void: ...
    @winrt_mixinmethod
    def get_SubfolderDateFormat(self: win32more.Windows.Media.Import.IPhotoImportSession2) -> win32more.Windows.Media.Import.PhotoImportSubfolderDateFormat: ...
    @winrt_mixinmethod
    def put_RememberDeselectedItems(self: win32more.Windows.Media.Import.IPhotoImportSession2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RememberDeselectedItems(self: win32more.Windows.Media.Import.IPhotoImportSession2) -> Boolean: ...
    Source = property(get_Source, None)
    SessionId = property(get_SessionId, None)
    DestinationFolder = property(get_DestinationFolder, put_DestinationFolder)
    AppendSessionDateToDestinationFolder = property(get_AppendSessionDateToDestinationFolder, put_AppendSessionDateToDestinationFolder)
    SubfolderCreationMode = property(get_SubfolderCreationMode, put_SubfolderCreationMode)
    DestinationFileNamePrefix = property(get_DestinationFileNamePrefix, put_DestinationFileNamePrefix)
    SubfolderDateFormat = property(get_SubfolderDateFormat, put_SubfolderDateFormat)
    RememberDeselectedItems = property(get_RememberDeselectedItems, put_RememberDeselectedItems)
class PhotoImportSidecar(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportSidecar
    _classid_ = 'Windows.Media.Import.PhotoImportSidecar'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Import.IPhotoImportSidecar) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportSidecar) -> UInt64: ...
    @winrt_mixinmethod
    def get_Date(self: win32more.Windows.Media.Import.IPhotoImportSidecar) -> win32more.Windows.Foundation.DateTime: ...
    Name = property(get_Name, None)
    SizeInBytes = property(get_SizeInBytes, None)
    Date = property(get_Date, None)
class PhotoImportSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportSource
    _classid_ = 'Windows.Media.Import.PhotoImportSource'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Manufacturer(self: win32more.Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Model(self: win32more.Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SerialNumber(self: win32more.Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ConnectionProtocol(self: win32more.Windows.Media.Import.IPhotoImportSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ConnectionTransport(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Media.Import.PhotoImportConnectionTransport: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Media.Import.PhotoImportSourceType: ...
    @winrt_mixinmethod
    def get_PowerSource(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Media.Import.PhotoImportPowerSource: ...
    @winrt_mixinmethod
    def get_BatteryLevelPercent(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_DateTime(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_StorageMedia(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportStorageMedium]: ...
    @winrt_mixinmethod
    def get_IsLocked(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def get_IsMassStorage(self: win32more.Windows.Media.Import.IPhotoImportSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def CreateImportSession(self: win32more.Windows.Media.Import.IPhotoImportSource) -> win32more.Windows.Media.Import.PhotoImportSession: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Media.Import.IPhotoImportSourceStatics, sourceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Import.PhotoImportSource]: ...
    @winrt_classmethod
    def FromFolderAsync(cls: win32more.Windows.Media.Import.IPhotoImportSourceStatics, sourceRootFolder: win32more.Windows.Storage.IStorageFolder) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Import.PhotoImportSource]: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, None)
    Description = property(get_Description, None)
    Manufacturer = property(get_Manufacturer, None)
    Model = property(get_Model, None)
    SerialNumber = property(get_SerialNumber, None)
    ConnectionProtocol = property(get_ConnectionProtocol, None)
    ConnectionTransport = property(get_ConnectionTransport, None)
    Type = property(get_Type, None)
    PowerSource = property(get_PowerSource, None)
    BatteryLevelPercent = property(get_BatteryLevelPercent, None)
    DateTime = property(get_DateTime, None)
    StorageMedia = property(get_StorageMedia, None)
    IsLocked = property(get_IsLocked, None)
    IsMassStorage = property(get_IsMassStorage, None)
    Thumbnail = property(get_Thumbnail, None)
PhotoImportSourceType = Int32
PhotoImportSourceType_Generic: PhotoImportSourceType = 0
PhotoImportSourceType_Camera: PhotoImportSourceType = 1
PhotoImportSourceType_MediaPlayer: PhotoImportSourceType = 2
PhotoImportSourceType_Phone: PhotoImportSourceType = 3
PhotoImportSourceType_Video: PhotoImportSourceType = 4
PhotoImportSourceType_PersonalInfoManager: PhotoImportSourceType = 5
PhotoImportSourceType_AudioRecorder: PhotoImportSourceType = 6
PhotoImportStage = Int32
PhotoImportStage_NotStarted: PhotoImportStage = 0
PhotoImportStage_FindingItems: PhotoImportStage = 1
PhotoImportStage_ImportingItems: PhotoImportStage = 2
PhotoImportStage_DeletingImportedItemsFromSource: PhotoImportStage = 3
class PhotoImportStorageMedium(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportStorageMedium
    _classid_ = 'Windows.Media.Import.PhotoImportStorageMedium'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Import.IPhotoImportStorageMedium) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Media.Import.IPhotoImportStorageMedium) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SerialNumber(self: win32more.Windows.Media.Import.IPhotoImportStorageMedium) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_StorageMediumType(self: win32more.Windows.Media.Import.IPhotoImportStorageMedium) -> win32more.Windows.Media.Import.PhotoImportStorageMediumType: ...
    @winrt_mixinmethod
    def get_SupportedAccessMode(self: win32more.Windows.Media.Import.IPhotoImportStorageMedium) -> win32more.Windows.Media.Import.PhotoImportAccessMode: ...
    @winrt_mixinmethod
    def get_CapacityInBytes(self: win32more.Windows.Media.Import.IPhotoImportStorageMedium) -> UInt64: ...
    @winrt_mixinmethod
    def get_AvailableSpaceInBytes(self: win32more.Windows.Media.Import.IPhotoImportStorageMedium) -> UInt64: ...
    @winrt_mixinmethod
    def Refresh(self: win32more.Windows.Media.Import.IPhotoImportStorageMedium) -> Void: ...
    Name = property(get_Name, None)
    Description = property(get_Description, None)
    SerialNumber = property(get_SerialNumber, None)
    StorageMediumType = property(get_StorageMediumType, None)
    SupportedAccessMode = property(get_SupportedAccessMode, None)
    CapacityInBytes = property(get_CapacityInBytes, None)
    AvailableSpaceInBytes = property(get_AvailableSpaceInBytes, None)
PhotoImportStorageMediumType = Int32
PhotoImportStorageMediumType_Undefined: PhotoImportStorageMediumType = 0
PhotoImportStorageMediumType_Fixed: PhotoImportStorageMediumType = 1
PhotoImportStorageMediumType_Removable: PhotoImportStorageMediumType = 2
PhotoImportSubfolderCreationMode = Int32
PhotoImportSubfolderCreationMode_DoNotCreateSubfolders: PhotoImportSubfolderCreationMode = 0
PhotoImportSubfolderCreationMode_CreateSubfoldersFromFileDate: PhotoImportSubfolderCreationMode = 1
PhotoImportSubfolderCreationMode_CreateSubfoldersFromExifDate: PhotoImportSubfolderCreationMode = 2
PhotoImportSubfolderCreationMode_KeepOriginalFolderStructure: PhotoImportSubfolderCreationMode = 3
PhotoImportSubfolderDateFormat = Int32
PhotoImportSubfolderDateFormat_Year: PhotoImportSubfolderDateFormat = 0
PhotoImportSubfolderDateFormat_YearMonth: PhotoImportSubfolderDateFormat = 1
PhotoImportSubfolderDateFormat_YearMonthDay: PhotoImportSubfolderDateFormat = 2
class PhotoImportVideoSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Import.IPhotoImportVideoSegment
    _classid_ = 'Windows.Media.Import.PhotoImportVideoSegment'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Import.IPhotoImportVideoSegment) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SizeInBytes(self: win32more.Windows.Media.Import.IPhotoImportVideoSegment) -> UInt64: ...
    @winrt_mixinmethod
    def get_Date(self: win32more.Windows.Media.Import.IPhotoImportVideoSegment) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Sibling(self: win32more.Windows.Media.Import.IPhotoImportVideoSegment) -> win32more.Windows.Media.Import.PhotoImportSidecar: ...
    @winrt_mixinmethod
    def get_Sidecars(self: win32more.Windows.Media.Import.IPhotoImportVideoSegment) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Import.PhotoImportSidecar]: ...
    Name = property(get_Name, None)
    SizeInBytes = property(get_SizeInBytes, None)
    Date = property(get_Date, None)
    Sibling = property(get_Sibling, None)
    Sidecars = property(get_Sidecars, None)
make_ready(__name__)
