from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI.Composition
import win32more.Microsoft.UI.Xaml.Controls
import win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals
import win32more.Windows.Foundation.Collections
import win32more.Windows.UI
import win32more.Windows.Win32.System.WinRT
class AnimatedAcceptVisualSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource
    _classid_ = 'Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedAcceptVisualSource'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedAcceptVisualSource.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedAcceptVisualSource: ...
    @winrt_mixinmethod
    def TryCreateAnimatedVisual(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource, compositor: win32more.Microsoft.UI.Composition.Compositor, diagnostics: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisual: ...
    @winrt_mixinmethod
    def get_Markers(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource2) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, Double]: ...
    @winrt_mixinmethod
    def SetColorProperty(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource2, propertyName: WinRT_String, value: win32more.Windows.UI.Color) -> Void: ...
    Markers = property(get_Markers, None)
class AnimatedBackVisualSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource
    _classid_ = 'Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedBackVisualSource'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedBackVisualSource.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedBackVisualSource: ...
    @winrt_mixinmethod
    def TryCreateAnimatedVisual(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource, compositor: win32more.Microsoft.UI.Composition.Compositor, diagnostics: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisual: ...
    @winrt_mixinmethod
    def get_Markers(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource2) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, Double]: ...
    @winrt_mixinmethod
    def SetColorProperty(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource2, propertyName: WinRT_String, value: win32more.Windows.UI.Color) -> Void: ...
    Markers = property(get_Markers, None)
class AnimatedChevronDownSmallVisualSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource
    _classid_ = 'Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedChevronDownSmallVisualSource'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedChevronDownSmallVisualSource.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedChevronDownSmallVisualSource: ...
    @winrt_mixinmethod
    def TryCreateAnimatedVisual(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource, compositor: win32more.Microsoft.UI.Composition.Compositor, diagnostics: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisual: ...
    @winrt_mixinmethod
    def get_Markers(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource2) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, Double]: ...
    @winrt_mixinmethod
    def SetColorProperty(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource2, propertyName: WinRT_String, value: win32more.Windows.UI.Color) -> Void: ...
    Markers = property(get_Markers, None)
class AnimatedChevronRightDownSmallVisualSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource
    _classid_ = 'Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedChevronRightDownSmallVisualSource'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedChevronRightDownSmallVisualSource.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedChevronRightDownSmallVisualSource: ...
    @winrt_mixinmethod
    def TryCreateAnimatedVisual(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource, compositor: win32more.Microsoft.UI.Composition.Compositor, diagnostics: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisual: ...
    @winrt_mixinmethod
    def get_Markers(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource2) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, Double]: ...
    @winrt_mixinmethod
    def SetColorProperty(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource2, propertyName: WinRT_String, value: win32more.Windows.UI.Color) -> Void: ...
    Markers = property(get_Markers, None)
class AnimatedChevronUpDownSmallVisualSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource
    _classid_ = 'Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedChevronUpDownSmallVisualSource'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedChevronUpDownSmallVisualSource.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedChevronUpDownSmallVisualSource: ...
    @winrt_mixinmethod
    def TryCreateAnimatedVisual(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource, compositor: win32more.Microsoft.UI.Composition.Compositor, diagnostics: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisual: ...
    @winrt_mixinmethod
    def get_Markers(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource2) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, Double]: ...
    @winrt_mixinmethod
    def SetColorProperty(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource2, propertyName: WinRT_String, value: win32more.Windows.UI.Color) -> Void: ...
    Markers = property(get_Markers, None)
class AnimatedFindVisualSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource
    _classid_ = 'Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedFindVisualSource'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedFindVisualSource.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedFindVisualSource: ...
    @winrt_mixinmethod
    def TryCreateAnimatedVisual(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource, compositor: win32more.Microsoft.UI.Composition.Compositor, diagnostics: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisual: ...
    @winrt_mixinmethod
    def get_Markers(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource2) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, Double]: ...
    @winrt_mixinmethod
    def SetColorProperty(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource2, propertyName: WinRT_String, value: win32more.Windows.UI.Color) -> Void: ...
    Markers = property(get_Markers, None)
class AnimatedGlobalNavigationButtonVisualSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource
    _classid_ = 'Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedGlobalNavigationButtonVisualSource'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedGlobalNavigationButtonVisualSource.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedGlobalNavigationButtonVisualSource: ...
    @winrt_mixinmethod
    def TryCreateAnimatedVisual(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource, compositor: win32more.Microsoft.UI.Composition.Compositor, diagnostics: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisual: ...
    @winrt_mixinmethod
    def get_Markers(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource2) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, Double]: ...
    @winrt_mixinmethod
    def SetColorProperty(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource2, propertyName: WinRT_String, value: win32more.Windows.UI.Color) -> Void: ...
    Markers = property(get_Markers, None)
class AnimatedSettingsVisualSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource
    _classid_ = 'Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedSettingsVisualSource'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedSettingsVisualSource.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Controls.AnimatedVisuals.AnimatedSettingsVisualSource: ...
    @winrt_mixinmethod
    def TryCreateAnimatedVisual(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource, compositor: win32more.Microsoft.UI.Composition.Compositor, diagnostics: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisual: ...
    @winrt_mixinmethod
    def get_Markers(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource2) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, Double]: ...
    @winrt_mixinmethod
    def SetColorProperty(self: win32more.Microsoft.UI.Xaml.Controls.IAnimatedVisualSource2, propertyName: WinRT_String, value: win32more.Windows.UI.Color) -> Void: ...
    Markers = property(get_Markers, None)


make_ready(__name__)
