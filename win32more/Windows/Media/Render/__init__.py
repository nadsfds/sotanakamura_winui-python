from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Media.Render
class AudioRenderCategory(Int32):  # enum
    Other = 0
    ForegroundOnlyMedia = 1
    BackgroundCapableMedia = 2
    Communications = 3
    Alerts = 4
    SoundEffects = 5
    GameEffects = 6
    GameMedia = 7
    GameChat = 8
    Speech = 9
    Movie = 10
    Media = 11


make_ready(__name__)
