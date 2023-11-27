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
import win32more.Windows.Phone.StartScreen
import win32more.Windows.UI.Notifications
class DualSimTile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.StartScreen.IDualSimTile
    _classid_ = 'Windows.Phone.StartScreen.DualSimTile'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Phone.StartScreen.DualSimTile: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.Phone.StartScreen.IDualSimTile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Phone.StartScreen.IDualSimTile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsPinnedToStart(self: win32more.Windows.Phone.StartScreen.IDualSimTile) -> Boolean: ...
    @winrt_mixinmethod
    def CreateAsync(self: win32more.Windows.Phone.StartScreen.IDualSimTile) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def UpdateAsync(self: win32more.Windows.Phone.StartScreen.IDualSimTile) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.Phone.StartScreen.IDualSimTile) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetTileForSim2(cls: win32more.Windows.Phone.StartScreen.IDualSimTileStatics) -> win32more.Windows.Phone.StartScreen.DualSimTile: ...
    @winrt_classmethod
    def UpdateDisplayNameForSim1Async(cls: win32more.Windows.Phone.StartScreen.IDualSimTileStatics, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def CreateTileUpdaterForSim1(cls: win32more.Windows.Phone.StartScreen.IDualSimTileStatics) -> win32more.Windows.UI.Notifications.TileUpdater: ...
    @winrt_classmethod
    def CreateTileUpdaterForSim2(cls: win32more.Windows.Phone.StartScreen.IDualSimTileStatics) -> win32more.Windows.UI.Notifications.TileUpdater: ...
    @winrt_classmethod
    def CreateBadgeUpdaterForSim1(cls: win32more.Windows.Phone.StartScreen.IDualSimTileStatics) -> win32more.Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_classmethod
    def CreateBadgeUpdaterForSim2(cls: win32more.Windows.Phone.StartScreen.IDualSimTileStatics) -> win32more.Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_classmethod
    def CreateToastNotifierForSim1(cls: win32more.Windows.Phone.StartScreen.IDualSimTileStatics) -> win32more.Windows.UI.Notifications.ToastNotifier: ...
    @winrt_classmethod
    def CreateToastNotifierForSim2(cls: win32more.Windows.Phone.StartScreen.IDualSimTileStatics) -> win32more.Windows.UI.Notifications.ToastNotifier: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    IsPinnedToStart = property(get_IsPinnedToStart, None)
DualSimTileContract: UInt32 = 65536
class IDualSimTile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.StartScreen.IDualSimTile'
    _iid_ = Guid('{143ab213-d05f-4041-a18c-3e3fcb75b41e}')
    @winrt_commethod(6)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IsPinnedToStart(self) -> Boolean: ...
    @winrt_commethod(9)
    def CreateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(10)
    def UpdateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def DeleteAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    IsPinnedToStart = property(get_IsPinnedToStart, None)
class IDualSimTileStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.StartScreen.IDualSimTileStatics'
    _iid_ = Guid('{50567c9e-c58f-4dc9-b6e8-fa6777eeeb37}')
    @winrt_commethod(6)
    def GetTileForSim2(self) -> win32more.Windows.Phone.StartScreen.DualSimTile: ...
    @winrt_commethod(7)
    def UpdateDisplayNameForSim1Async(self, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def CreateTileUpdaterForSim1(self) -> win32more.Windows.UI.Notifications.TileUpdater: ...
    @winrt_commethod(9)
    def CreateTileUpdaterForSim2(self) -> win32more.Windows.UI.Notifications.TileUpdater: ...
    @winrt_commethod(10)
    def CreateBadgeUpdaterForSim1(self) -> win32more.Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_commethod(11)
    def CreateBadgeUpdaterForSim2(self) -> win32more.Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_commethod(12)
    def CreateToastNotifierForSim1(self) -> win32more.Windows.UI.Notifications.ToastNotifier: ...
    @winrt_commethod(13)
    def CreateToastNotifierForSim2(self) -> win32more.Windows.UI.Notifications.ToastNotifier: ...
class IToastNotificationManagerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.StartScreen.IToastNotificationManagerStatics3'
    _iid_ = Guid('{2717f54b-50df-4455-8e6e-41e0fc8e13ce}')
    @winrt_commethod(6)
    def CreateToastNotifierForSecondaryTile(self, tileId: WinRT_String) -> win32more.Windows.UI.Notifications.ToastNotifier: ...
make_ready(__name__)
