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
import win32more.Windows.Media.Render
AudioRenderCategory = Int32
AudioRenderCategory_Other: AudioRenderCategory = 0
AudioRenderCategory_ForegroundOnlyMedia: AudioRenderCategory = 1
AudioRenderCategory_BackgroundCapableMedia: AudioRenderCategory = 2
AudioRenderCategory_Communications: AudioRenderCategory = 3
AudioRenderCategory_Alerts: AudioRenderCategory = 4
AudioRenderCategory_SoundEffects: AudioRenderCategory = 5
AudioRenderCategory_GameEffects: AudioRenderCategory = 6
AudioRenderCategory_GameMedia: AudioRenderCategory = 7
AudioRenderCategory_GameChat: AudioRenderCategory = 8
AudioRenderCategory_Speech: AudioRenderCategory = 9
AudioRenderCategory_Movie: AudioRenderCategory = 10
AudioRenderCategory_Media: AudioRenderCategory = 11
make_ready(__name__)
