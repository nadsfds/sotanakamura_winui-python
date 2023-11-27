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
import win32more.Windows.Globalization.PhoneNumberFormatting
class IPhoneNumberFormatter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter'
    _iid_ = Guid('{1556b49e-bad4-4b4a-900d-4407adb7c981}')
    @winrt_commethod(6)
    def Format(self, number: win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo) -> WinRT_String: ...
    @winrt_commethod(7)
    def FormatWithOutputFormat(self, number: win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo, numberFormat: win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormat) -> WinRT_String: ...
    @winrt_commethod(8)
    def FormatPartialString(self, number: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(9)
    def FormatString(self, number: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(10)
    def FormatStringWithLeftToRightMarkers(self, number: WinRT_String) -> WinRT_String: ...
class IPhoneNumberFormatterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatterStatics'
    _iid_ = Guid('{5ca6f931-84d9-414b-ab4e-a0552c878602}')
    @winrt_commethod(6)
    def TryCreate(self, regionCode: WinRT_String, phoneNumber: POINTER(win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormatter)) -> Void: ...
    @winrt_commethod(7)
    def GetCountryCodeForRegion(self, regionCode: WinRT_String) -> Int32: ...
    @winrt_commethod(8)
    def GetNationalDirectDialingPrefixForRegion(self, regionCode: WinRT_String, stripNonDigit: Boolean) -> WinRT_String: ...
    @winrt_commethod(9)
    def WrapWithLeftToRightMarkers(self, number: WinRT_String) -> WinRT_String: ...
class IPhoneNumberInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo'
    _iid_ = Guid('{1c7ce4dd-c8b4-4ea3-9aef-b342e2c5b417}')
    @winrt_commethod(6)
    def get_CountryCode(self) -> Int32: ...
    @winrt_commethod(7)
    def get_PhoneNumber(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetLengthOfGeographicalAreaCode(self) -> Int32: ...
    @winrt_commethod(9)
    def GetNationalSignificantNumber(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetLengthOfNationalDestinationCode(self) -> Int32: ...
    @winrt_commethod(11)
    def PredictNumberKind(self) -> win32more.Windows.Globalization.PhoneNumberFormatting.PredictedPhoneNumberKind: ...
    @winrt_commethod(12)
    def GetGeographicRegionCode(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def CheckNumberMatch(self, otherNumber: win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberMatchResult: ...
    CountryCode = property(get_CountryCode, None)
    PhoneNumber = property(get_PhoneNumber, None)
class IPhoneNumberInfoFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfoFactory'
    _iid_ = Guid('{8202b964-adaa-4cff-8fcf-17e7516a28ff}')
    @winrt_commethod(6)
    def Create(self, number: WinRT_String) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo: ...
class IPhoneNumberInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfoStatics'
    _iid_ = Guid('{5b3f4f6a-86a9-40e9-8649-6d61161928d4}')
    @winrt_commethod(6)
    def TryParse(self, input: WinRT_String, phoneNumber: POINTER(win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo)) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberParseResult: ...
    @winrt_commethod(7)
    def TryParseWithRegion(self, input: WinRT_String, regionCode: WinRT_String, phoneNumber: POINTER(win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo)) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberParseResult: ...
PhoneNumberFormat = Int32
PhoneNumberFormat_E164: PhoneNumberFormat = 0
PhoneNumberFormat_International: PhoneNumberFormat = 1
PhoneNumberFormat_National: PhoneNumberFormat = 2
PhoneNumberFormat_Rfc3966: PhoneNumberFormat = 3
class PhoneNumberFormatter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter
    _classid_ = 'Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormatter'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormatter: ...
    @winrt_mixinmethod
    def Format(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter, number: win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatWithOutputFormat(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter, number: win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo, numberFormat: win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormat) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatPartialString(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter, number: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatString(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter, number: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def FormatStringWithLeftToRightMarkers(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatter, number: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def TryCreate(cls: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatterStatics, regionCode: WinRT_String, phoneNumber: POINTER(win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormatter)) -> Void: ...
    @winrt_classmethod
    def GetCountryCodeForRegion(cls: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatterStatics, regionCode: WinRT_String) -> Int32: ...
    @winrt_classmethod
    def GetNationalDirectDialingPrefixForRegion(cls: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatterStatics, regionCode: WinRT_String, stripNonDigit: Boolean) -> WinRT_String: ...
    @winrt_classmethod
    def WrapWithLeftToRightMarkers(cls: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberFormatterStatics, number: WinRT_String) -> WinRT_String: ...
class PhoneNumberInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo
    _classid_ = 'Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo'
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfoFactory, number: WinRT_String) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo: ...
    @winrt_mixinmethod
    def get_CountryCode(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_PhoneNumber(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetLengthOfGeographicalAreaCode(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> Int32: ...
    @winrt_mixinmethod
    def GetNationalSignificantNumber(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetLengthOfNationalDestinationCode(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> Int32: ...
    @winrt_mixinmethod
    def PredictNumberKind(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> win32more.Windows.Globalization.PhoneNumberFormatting.PredictedPhoneNumberKind: ...
    @winrt_mixinmethod
    def GetGeographicRegionCode(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def CheckNumberMatch(self: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfo, otherNumber: win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberMatchResult: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    @winrt_classmethod
    def TryParse(cls: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfoStatics, input: WinRT_String, phoneNumber: POINTER(win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo)) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberParseResult: ...
    @winrt_classmethod
    def TryParseWithRegion(cls: win32more.Windows.Globalization.PhoneNumberFormatting.IPhoneNumberInfoStatics, input: WinRT_String, regionCode: WinRT_String, phoneNumber: POINTER(win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberInfo)) -> win32more.Windows.Globalization.PhoneNumberFormatting.PhoneNumberParseResult: ...
    CountryCode = property(get_CountryCode, None)
    PhoneNumber = property(get_PhoneNumber, None)
PhoneNumberMatchResult = Int32
PhoneNumberMatchResult_NoMatch: PhoneNumberMatchResult = 0
PhoneNumberMatchResult_ShortNationalSignificantNumberMatch: PhoneNumberMatchResult = 1
PhoneNumberMatchResult_NationalSignificantNumberMatch: PhoneNumberMatchResult = 2
PhoneNumberMatchResult_ExactMatch: PhoneNumberMatchResult = 3
PhoneNumberParseResult = Int32
PhoneNumberParseResult_Valid: PhoneNumberParseResult = 0
PhoneNumberParseResult_NotANumber: PhoneNumberParseResult = 1
PhoneNumberParseResult_InvalidCountryCode: PhoneNumberParseResult = 2
PhoneNumberParseResult_TooShort: PhoneNumberParseResult = 3
PhoneNumberParseResult_TooLong: PhoneNumberParseResult = 4
PredictedPhoneNumberKind = Int32
PredictedPhoneNumberKind_FixedLine: PredictedPhoneNumberKind = 0
PredictedPhoneNumberKind_Mobile: PredictedPhoneNumberKind = 1
PredictedPhoneNumberKind_FixedLineOrMobile: PredictedPhoneNumberKind = 2
PredictedPhoneNumberKind_TollFree: PredictedPhoneNumberKind = 3
PredictedPhoneNumberKind_PremiumRate: PredictedPhoneNumberKind = 4
PredictedPhoneNumberKind_SharedCost: PredictedPhoneNumberKind = 5
PredictedPhoneNumberKind_Voip: PredictedPhoneNumberKind = 6
PredictedPhoneNumberKind_PersonalNumber: PredictedPhoneNumberKind = 7
PredictedPhoneNumberKind_Pager: PredictedPhoneNumberKind = 8
PredictedPhoneNumberKind_UniversalAccountNumber: PredictedPhoneNumberKind = 9
PredictedPhoneNumberKind_Voicemail: PredictedPhoneNumberKind = 10
PredictedPhoneNumberKind_Unknown: PredictedPhoneNumberKind = 11
make_ready(__name__)
