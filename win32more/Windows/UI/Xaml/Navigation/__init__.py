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
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Interop
import win32more.Windows.UI.Xaml.Media.Animation
import win32more.Windows.UI.Xaml.Navigation
class FrameNavigationOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Navigation.IFrameNavigationOptions
    _classid_ = 'Windows.UI.Xaml.Navigation.FrameNavigationOptions'
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Navigation.IFrameNavigationOptionsFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Navigation.FrameNavigationOptions: ...
    @winrt_mixinmethod
    def get_IsNavigationStackEnabled(self: win32more.Windows.UI.Xaml.Navigation.IFrameNavigationOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsNavigationStackEnabled(self: win32more.Windows.UI.Xaml.Navigation.IFrameNavigationOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TransitionInfoOverride(self: win32more.Windows.UI.Xaml.Navigation.IFrameNavigationOptions) -> win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_mixinmethod
    def put_TransitionInfoOverride(self: win32more.Windows.UI.Xaml.Navigation.IFrameNavigationOptions, value: win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> Void: ...
    IsNavigationStackEnabled = property(get_IsNavigationStackEnabled, put_IsNavigationStackEnabled)
    TransitionInfoOverride = property(get_TransitionInfoOverride, put_TransitionInfoOverride)
class IFrameNavigationOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Navigation.IFrameNavigationOptions'
    _iid_ = Guid('{b539ad2a-9fb7-520a-8f41-57a50c59cf92}')
    @winrt_commethod(6)
    def get_IsNavigationStackEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsNavigationStackEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_TransitionInfoOverride(self) -> win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_commethod(9)
    def put_TransitionInfoOverride(self, value: win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> Void: ...
    IsNavigationStackEnabled = property(get_IsNavigationStackEnabled, put_IsNavigationStackEnabled)
    TransitionInfoOverride = property(get_TransitionInfoOverride, put_TransitionInfoOverride)
class IFrameNavigationOptionsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Navigation.IFrameNavigationOptionsFactory'
    _iid_ = Guid('{d4681e41-7e6d-5c7c-aca0-478681cc6fce}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Navigation.FrameNavigationOptions: ...
class INavigatingCancelEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Navigation.INavigatingCancelEventArgs'
    _iid_ = Guid('{fd1d67ae-eafb-4079-be80-6dc92a03aedf}')
    @winrt_commethod(6)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_NavigationMode(self) -> win32more.Windows.UI.Xaml.Navigation.NavigationMode: ...
    @winrt_commethod(9)
    def get_SourcePageType(self) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    Cancel = property(get_Cancel, put_Cancel)
    NavigationMode = property(get_NavigationMode, None)
    SourcePageType = property(get_SourcePageType, None)
class INavigatingCancelEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Navigation.INavigatingCancelEventArgs2'
    _iid_ = Guid('{5407b704-8147-4343-838f-dd1ee908c137}')
    @winrt_commethod(6)
    def get_Parameter(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_NavigationTransitionInfo(self) -> win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    Parameter = property(get_Parameter, None)
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
class INavigationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Navigation.INavigationEventArgs'
    _iid_ = Guid('{b6aa9834-6691-44d1-bdf7-58820c27b0d0}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_Parameter(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(8)
    def get_SourcePageType(self) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_commethod(9)
    def get_NavigationMode(self) -> win32more.Windows.UI.Xaml.Navigation.NavigationMode: ...
    @winrt_commethod(10)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(11)
    def put_Uri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    Content = property(get_Content, None)
    Parameter = property(get_Parameter, None)
    SourcePageType = property(get_SourcePageType, None)
    NavigationMode = property(get_NavigationMode, None)
    Uri = property(get_Uri, put_Uri)
class INavigationEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Navigation.INavigationEventArgs2'
    _iid_ = Guid('{dbff71d9-979a-4b2e-a49b-3bb17fdef574}')
    @winrt_commethod(6)
    def get_NavigationTransitionInfo(self) -> win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
class INavigationFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Navigation.INavigationFailedEventArgs'
    _iid_ = Guid('{11c1dff7-36c2-4102-b2ef-0217a97289b3}')
    @winrt_commethod(6)
    def get_Exception(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_SourcePageType(self) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    Exception = property(get_Exception, None)
    Handled = property(get_Handled, put_Handled)
    SourcePageType = property(get_SourcePageType, None)
class IPageStackEntry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Navigation.IPageStackEntry'
    _iid_ = Guid('{ef8814a6-9388-4aca-8572-405194069080}')
    @winrt_commethod(6)
    def get_SourcePageType(self) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_commethod(7)
    def get_Parameter(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(8)
    def get_NavigationTransitionInfo(self) -> win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    SourcePageType = property(get_SourcePageType, None)
    Parameter = property(get_Parameter, None)
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
class IPageStackEntryFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Navigation.IPageStackEntryFactory'
    _iid_ = Guid('{4454048a-a8b9-4f78-9b84-1f51f58851ff}')
    @winrt_commethod(6)
    def CreateInstance(self, sourcePageType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, navigationTransitionInfo: win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> win32more.Windows.UI.Xaml.Navigation.PageStackEntry: ...
class IPageStackEntryStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Navigation.IPageStackEntryStatics'
    _iid_ = Guid('{aceff8e3-246c-4033-9f01-01cb0da5254e}')
    @winrt_commethod(6)
    def get_SourcePageTypeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    SourcePageTypeProperty = property(get_SourcePageTypeProperty, None)
class LoadCompletedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aebaf785-43fc-4e2c-95c3-97ae84eabc8e}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Navigation.NavigationEventArgs) -> Void: ...
class NavigatedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7bd1cf54-23cf-4cce-b2f5-4ce78d96896e}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Navigation.NavigationEventArgs) -> Void: ...
class NavigatingCancelEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Navigation.INavigatingCancelEventArgs
    _classid_ = 'Windows.UI.Xaml.Navigation.NavigatingCancelEventArgs'
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Windows.UI.Xaml.Navigation.INavigatingCancelEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Windows.UI.Xaml.Navigation.INavigatingCancelEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NavigationMode(self: win32more.Windows.UI.Xaml.Navigation.INavigatingCancelEventArgs) -> win32more.Windows.UI.Xaml.Navigation.NavigationMode: ...
    @winrt_mixinmethod
    def get_SourcePageType(self: win32more.Windows.UI.Xaml.Navigation.INavigatingCancelEventArgs) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_mixinmethod
    def get_Parameter(self: win32more.Windows.UI.Xaml.Navigation.INavigatingCancelEventArgs2) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_NavigationTransitionInfo(self: win32more.Windows.UI.Xaml.Navigation.INavigatingCancelEventArgs2) -> win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    Cancel = property(get_Cancel, put_Cancel)
    NavigationMode = property(get_NavigationMode, None)
    SourcePageType = property(get_SourcePageType, None)
    Parameter = property(get_Parameter, None)
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
class NavigatingCancelEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75d6a78f-a302-4489-9898-24ea49182910}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Navigation.NavigatingCancelEventArgs) -> Void: ...
NavigationCacheMode = Int32
NavigationCacheMode_Disabled: NavigationCacheMode = 0
NavigationCacheMode_Required: NavigationCacheMode = 1
NavigationCacheMode_Enabled: NavigationCacheMode = 2
class NavigationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Navigation.INavigationEventArgs
    _classid_ = 'Windows.UI.Xaml.Navigation.NavigationEventArgs'
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.UI.Xaml.Navigation.INavigationEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Parameter(self: win32more.Windows.UI.Xaml.Navigation.INavigationEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_SourcePageType(self: win32more.Windows.UI.Xaml.Navigation.INavigationEventArgs) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_mixinmethod
    def get_NavigationMode(self: win32more.Windows.UI.Xaml.Navigation.INavigationEventArgs) -> win32more.Windows.UI.Xaml.Navigation.NavigationMode: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.UI.Xaml.Navigation.INavigationEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: win32more.Windows.UI.Xaml.Navigation.INavigationEventArgs, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_NavigationTransitionInfo(self: win32more.Windows.UI.Xaml.Navigation.INavigationEventArgs2) -> win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    Content = property(get_Content, None)
    Parameter = property(get_Parameter, None)
    SourcePageType = property(get_SourcePageType, None)
    NavigationMode = property(get_NavigationMode, None)
    Uri = property(get_Uri, put_Uri)
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
class NavigationFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Navigation.INavigationFailedEventArgs
    _classid_ = 'Windows.UI.Xaml.Navigation.NavigationFailedEventArgs'
    @winrt_mixinmethod
    def get_Exception(self: win32more.Windows.UI.Xaml.Navigation.INavigationFailedEventArgs) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Xaml.Navigation.INavigationFailedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Xaml.Navigation.INavigationFailedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SourcePageType(self: win32more.Windows.UI.Xaml.Navigation.INavigationFailedEventArgs) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    Exception = property(get_Exception, None)
    Handled = property(get_Handled, put_Handled)
    SourcePageType = property(get_SourcePageType, None)
class NavigationFailedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4dab4671-12b2-43c7-b892-9be2dcd3e88d}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Navigation.NavigationFailedEventArgs) -> Void: ...
NavigationMode = Int32
NavigationMode_New: NavigationMode = 0
NavigationMode_Back: NavigationMode = 1
NavigationMode_Forward: NavigationMode = 2
NavigationMode_Refresh: NavigationMode = 3
class NavigationStoppedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f0117ddb-12fa-4d8d-8b26-b383d09c2b3c}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Navigation.NavigationEventArgs) -> Void: ...
class _PageStackEntry_Meta_(ComPtr.__class__):
    pass
class PageStackEntry(ComPtr, metaclass=_PageStackEntry_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Navigation.IPageStackEntry
    _classid_ = 'Windows.UI.Xaml.Navigation.PageStackEntry'
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Navigation.IPageStackEntryFactory, sourcePageType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, navigationTransitionInfo: win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> win32more.Windows.UI.Xaml.Navigation.PageStackEntry: ...
    @winrt_mixinmethod
    def get_SourcePageType(self: win32more.Windows.UI.Xaml.Navigation.IPageStackEntry) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_mixinmethod
    def get_Parameter(self: win32more.Windows.UI.Xaml.Navigation.IPageStackEntry) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_NavigationTransitionInfo(self: win32more.Windows.UI.Xaml.Navigation.IPageStackEntry) -> win32more.Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_classmethod
    def get_SourcePageTypeProperty(cls: win32more.Windows.UI.Xaml.Navigation.IPageStackEntryStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    SourcePageType = property(get_SourcePageType, None)
    Parameter = property(get_Parameter, None)
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
    _PageStackEntry_Meta_.SourcePageTypeProperty = property(get_SourcePageTypeProperty.__wrapped__, None)
make_ready(__name__)
