### Airtest
多台设备
```
from airtest.core.api import auto_setup
from airtest.core.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
auto_setup(__file__)
 
device_1 = Android('设备编号')
device_2 = Android('设备编号')
device_3 = Android('设备编号')
 
poco_1 = AndroidUiautomationPoco(device_1, use_airtest_input=True, screenshot_each_action=False)
poco_2 = AndroidUiautomationPoco(device_2, use_airtest_input=True, screenshot_each_action=False)
poco_3 = AndroidUiautomationPoco(device_3, use_airtest_input=True, screenshot_each_action=False)
```