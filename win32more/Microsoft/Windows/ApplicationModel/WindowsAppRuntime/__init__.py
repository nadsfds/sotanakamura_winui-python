from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.WinRT
DeploymentContract: UInt32 = 262144
class DeploymentInitializeOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentInitializeOptions
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentInitializeOptions'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentInitializeOptions.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentInitializeOptions: ...
    @winrt_mixinmethod
    def get_ForceDeployment(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentInitializeOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_ForceDeployment(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentInitializeOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OnErrorShowUI(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentInitializeOptions2) -> Boolean: ...
    @winrt_mixinmethod
    def put_OnErrorShowUI(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentInitializeOptions2, value: Boolean) -> Void: ...
    ForceDeployment = property(get_ForceDeployment, put_ForceDeployment)
    OnErrorShowUI = property(get_OnErrorShowUI, put_OnErrorShowUI)
class DeploymentManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentManager'
    @winrt_overload
    @winrt_classmethod
    def Initialize(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentManagerStatics2, deploymentInitializeOptions: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentInitializeOptions) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
    @winrt_classmethod
    def GetStatus(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentManagerStatics) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
    @Initialize.register
    @winrt_classmethod
    def Initialize(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentManagerStatics) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
class DeploymentResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResult
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 2:
            return win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResultFactory, status: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentStatus, extendedError: win32more.Windows.Foundation.HResult) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResult) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResult) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class DeploymentStatus(Int32):  # enum
    Unknown = 0
    Ok = 1
    PackageInstallRequired = 2
    PackageInstallFailed = 3
class IDeploymentInitializeOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentInitializeOptions'
    _iid_ = Guid('{578a5fd4-9d7f-5e01-97b8-d8ea61db4027}')
    @winrt_commethod(6)
    def get_ForceDeployment(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_ForceDeployment(self, value: Boolean) -> Void: ...
    ForceDeployment = property(get_ForceDeployment, put_ForceDeployment)
class IDeploymentInitializeOptions2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentInitializeOptions2'
    _iid_ = Guid('{ad902820-149f-5e16-a566-9b2363997de2}')
    @winrt_commethod(6)
    def get_OnErrorShowUI(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_OnErrorShowUI(self, value: Boolean) -> Void: ...
    OnErrorShowUI = property(get_OnErrorShowUI, put_OnErrorShowUI)
class IDeploymentManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentManagerStatics'
    _iid_ = Guid('{6782a9d0-bfd0-50ea-81b0-32e9ed37cdf0}')
    @winrt_commethod(6)
    def GetStatus(self) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
    @winrt_commethod(7)
    def Initialize(self) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
class IDeploymentManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentManagerStatics2'
    _iid_ = Guid('{f49c16ee-6ebc-5f15-bebb-2ba49f8c0b30}')
    @winrt_commethod(6)
    def Initialize(self, deploymentInitializeOptions: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentInitializeOptions) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...
class IDeploymentResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResult'
    _iid_ = Guid('{27203f62-463d-587a-8eb7-870098901078}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class IDeploymentResultFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.WindowsAppRuntime.IDeploymentResultFactory'
    _iid_ = Guid('{acd7bdae-4ae6-5cac-8205-1e8c305f953b}')
    @winrt_commethod(6)
    def CreateInstance(self, status: win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentStatus, extendedError: win32more.Windows.Foundation.HResult) -> win32more.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentResult: ...


make_ready(__name__)
