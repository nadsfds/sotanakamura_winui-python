from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation.Metadata
import win32more.Windows.Win32.System.WinRT
class ApiInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.Metadata.ApiInformation'
    @winrt_classmethod
    def IsTypePresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsMethodPresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, methodName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsMethodPresentWithArity(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, methodName: WinRT_String, inputParameterCount: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsEventPresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, eventName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsPropertyPresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, propertyName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsReadOnlyPropertyPresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, propertyName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsWriteablePropertyPresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, propertyName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsEnumNamedValuePresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, enumTypeName: WinRT_String, valueName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsApiContractPresentByMajor(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, contractName: WinRT_String, majorVersion: UInt16) -> Boolean: ...
    @winrt_classmethod
    def IsApiContractPresentByMajorAndMinor(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, contractName: WinRT_String, majorVersion: UInt16, minorVersion: UInt16) -> Boolean: ...
class AttributeTargets(UInt32):  # enum
    All = 4294967295
    Delegate = 1
    Enum = 2
    Event = 4
    Field = 8
    Interface = 16
    Method = 64
    Parameter = 128
    Property = 256
    RuntimeClass = 512
    Struct = 1024
    InterfaceImpl = 2048
    ApiContract = 8192
class CompositionType(Int32):  # enum
    Protected = 1
    Public = 2
class DeprecationType(Int32):  # enum
    Deprecate = 0
    Remove = 1
class FeatureStage(Int32):  # enum
    AlwaysDisabled = 0
    DisabledByDefault = 1
    EnabledByDefault = 2
    AlwaysEnabled = 3
class GCPressureAmount(Int32):  # enum
    Low = 0
    Medium = 1
    High = 2
class IApiInformationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.Metadata.IApiInformationStatics'
    _iid_ = Guid('{997439fe-f681-4a11-b416-c13a47e8ba36}')
    @winrt_commethod(6)
    def IsTypePresent(self, typeName: WinRT_String) -> Boolean: ...
    @winrt_commethod(7)
    def IsMethodPresent(self, typeName: WinRT_String, methodName: WinRT_String) -> Boolean: ...
    @winrt_commethod(8)
    def IsMethodPresentWithArity(self, typeName: WinRT_String, methodName: WinRT_String, inputParameterCount: UInt32) -> Boolean: ...
    @winrt_commethod(9)
    def IsEventPresent(self, typeName: WinRT_String, eventName: WinRT_String) -> Boolean: ...
    @winrt_commethod(10)
    def IsPropertyPresent(self, typeName: WinRT_String, propertyName: WinRT_String) -> Boolean: ...
    @winrt_commethod(11)
    def IsReadOnlyPropertyPresent(self, typeName: WinRT_String, propertyName: WinRT_String) -> Boolean: ...
    @winrt_commethod(12)
    def IsWriteablePropertyPresent(self, typeName: WinRT_String, propertyName: WinRT_String) -> Boolean: ...
    @winrt_commethod(13)
    def IsEnumNamedValuePresent(self, enumTypeName: WinRT_String, valueName: WinRT_String) -> Boolean: ...
    @winrt_commethod(14)
    def IsApiContractPresentByMajor(self, contractName: WinRT_String, majorVersion: UInt16) -> Boolean: ...
    @winrt_commethod(15)
    def IsApiContractPresentByMajorAndMinor(self, contractName: WinRT_String, majorVersion: UInt16, minorVersion: UInt16) -> Boolean: ...
class MarshalingType(Int32):  # enum
    None_ = 1
    Agile = 2
    Standard = 3
    InvalidMarshaling = 0
class Platform(Int32):  # enum
    Windows = 0
    WindowsPhone = 1
class ThreadingModel(Int32):  # enum
    STA = 1
    MTA = 2
    Both = 3
    InvalidThreading = 0


make_ready(__name__)
