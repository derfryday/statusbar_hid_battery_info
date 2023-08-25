from statusbar_hid_battery_info.app import Device
from statusbar_hid_battery_info.util import Util

test_output_mouse_only: str = """
+-o AppleDeviceManagementHIDEventService  <class AppleDeviceManagementHIDEventService, id 0x10000fcc6, registered, matched, active, busy 0 (0 ms), retain 9>

  | {

  |   "IOMatchedAtBoot" = Yes

  |   "PrimaryUsagePage" = 65280

  |   "VersionNumber" = 850

  |   "VendorID" = 1452

  |   "LastCriticalError" = 2

  |   "Built-In" = Yes

  |   "AccelCalFW Version" = 0

  |   "WakeReason" = "Host (0x01)"

  |   "Product" = "Apple Internal Keyboard / Trackpad"

  |   "SerialNumber" = "FM7152301M5NX0RAH+EMN"

  |   "Transport" = "SPI"

  |   "BootLoaderFW Version" = 18

  |   "Manufacturer" = "Apple Inc."

  |   "ActCalFW Version" = 0

  |   "ProductID" = 835

  |   "DeviceUsagePairs" = ({"DeviceUsagePage"=65280,"DeviceUsage"=11})

  |   "IOPersonalityPublisher" = "com.apple.driver.AppleTopCaseDriverV2"

  |   "MTFW Version" = 1332

  |   "MTCalFW Version" = 1

  |   "KeyCalFW Version" = 0

  |   "ForceCalFW Version" = 0

  |   "ReportInterval" = 8000

  |   "VendorIDSource" = 0

  |   "STFW Version" = 850

  |   "HIDEventServiceProperties" = {"HIDMouseKeysOptionToggles"=0,"JitterNoClick"=1,"ActuateDetents"=1,"Dragging"=0,"HIDSlowKeysDelay"=0,"FlipLeftAndRightEdgeGestures"=No,"JitterNoMove"=1,"HIDTrackpadScrollAcceleration"=20$

  |   "CFBundleIdentifier" = "com.apple.driver.AppleTopCaseHIDEventDriver"

  |   "IOProviderClass" = "IOHIDInterface"

  |   "LocationID" = 47

  |   "IOClass" = "AppleDeviceManagementHIDEventService"

  |   "HIDServiceSupport" = Yes

  |   "CFBundleIdentifierKernel" = "com.apple.driver.AppleTopCaseHIDEventDriver"

  |   "ProductIDArray" = (835)

  |   "ColorID" = 1

  |   "CountryCode" = 0

  |   "IOMatchCategory" = "IODefaultMatchCategory"

  |   "PrimaryUsage" = 11

  |   "IOProbeScore" = 7175

  |   "StandardType" = 0

  |   "IOGeneralInterest" = "IOCommand is not serializable"

  | }

  |

  +-o IOHIDEventServiceUserClient  <class IOHIDEventServiceUserClient, id 0x10000fcc9, !registered, !matched, active, busy 0, retain 6>

      {

        "IOUserClientDefaultLockingSetProperties" = Yes

        "IOUserClientDefaultLocking" = Yes

        "IOUserClientCreator" = "pid 587, WindowServer"

        "IOUserClientDefaultLockingSingleThreadExternalMethod" = No

        "IOUserClientEntitlements" = No

        "DebugState" = {"EventQueue"={"NoFullMsg"=0,"tail"=0,"NotificationForce"=0,"NotificationCount"=0,"head"=0}}

      }






+-o AppleDeviceManagementHIDEventService  <class AppleDeviceManagementHIDEventService, id 0x1000210a8, registered, matched, active, busy 0 (2 ms), retain 7>

    {

      "IOMatchedAtBoot" = Yes

      "LowBatteryNotificationPercentage" = 2

      "PrimaryUsagePage" = 65280

      "BatteryFaultNotificationType" = "MOBatteryFault"

      "HasBattery" = Yes

      "VendorID" = 76

      "VersionNumber" = 0

      "Built-In" = No

      "DeviceAddress" = "98-46-0a-b4-c3-ef"

      "WakeReason" = "Button (0x03)"

      "Product" = "Magic Mouse"

      "SerialNumber" = "98-46-0a-b4-c3-ef"

      "Transport" = "Bluetooth"

      "BatteryLowNotificationType" = "MOLowBattery"

      "ProductID" = 617

      "DeviceUsagePairs" = ({"DeviceUsagePage"=65280,"DeviceUsage"=11},{"DeviceUsagePage"=65280,"DeviceUsage"=20})

      "IOPersonalityPublisher" = "com.apple.driver.AppleTopCaseHIDEventDriver"

      "MTFW Version" = 0

      "BD_ADDR" = <98460ab4c3ef>

      "BatteryPercent" = 74

      "BatteryStatusNotificationType" = "BatteryStatusChanged"

      "CriticallyLowBatteryNotificationPercentage" = 1

      "ReportInterval" = 11250

      "RadioFW Version" = 402

      "VendorIDSource" = 1

      "STFW Version" = 2144

      "CFBundleIdentifier" = "com.apple.driver.AppleTopCaseHIDEventDriver"

      "IOProviderClass" = "IOHIDInterface"

      "LocationID" = 179618799

      "BluetoothDevice" = Yes

      "IOClass" = "AppleDeviceManagementHIDEventService"

      "HIDServiceSupport" = No

      "CFBundleIdentifierKernel" = "com.apple.driver.AppleTopCaseHIDEventDriver"

      "ProductIDArray" = (617)

      "BatteryStatusFlags" = 0

      "ColorID" = 0

      "IOMatchCategory" = "IODefaultMatchCategory"

      "CountryCode" = 0

      "IOProbeScore" = 7175

      "PrimaryUsage" = 11

      "IOGeneralInterest" = "IOCommand is not serializable"

      "BTFW Version" = 402

    }
"""

test_output_mouse_and_keyboard: str = """
+-o AppleDeviceManagementHIDEventService  <class AppleDeviceManagementHIDEventService, id 0x10000fcc6, registered, matched, active, busy 0 (0 ms), retain 9>

  | {

  |   "IOMatchedAtBoot" = Yes

  |   "PrimaryUsagePage" = 65280

  |   "VersionNumber" = 850

  |   "VendorID" = 1452

  |   "LastCriticalError" = 2

  |   "Built-In" = Yes

  |   "AccelCalFW Version" = 0

  |   "WakeReason" = "Host (0x01)"

  |   "Product" = "Apple Internal Keyboard / Trackpad"

  |   "SerialNumber" = "FM7152301M5NX0RAH+EMN"

  |   "Transport" = "SPI"

  |   "BootLoaderFW Version" = 18

  |   "Manufacturer" = "Apple Inc."

  |   "ActCalFW Version" = 0

  |   "ProductID" = 835

  |   "DeviceUsagePairs" = ({"DeviceUsagePage"=65280,"DeviceUsage"=11})

  |   "IOPersonalityPublisher" = "com.apple.driver.AppleTopCaseDriverV2"

  |   "MTFW Version" = 1332

  |   "MTCalFW Version" = 1

  |   "KeyCalFW Version" = 0

  |   "ForceCalFW Version" = 0

  |   "ReportInterval" = 8000

  |   "VendorIDSource" = 0

  |   "STFW Version" = 850

  |   "HIDEventServiceProperties" = {"HIDMouseKeysOptionToggles"=0,"JitterNoClick"=1,"ActuateDetents"=1,"Dragging"=0,"HIDSlowKeysDelay"=0,"FlipLeftAndRightEdgeGestures"=No,"JitterNoMove"=1,"HIDTrackpadScrollAcceleration"=20480,"HIDInitia$

  |   "CFBundleIdentifier" = "com.apple.driver.AppleTopCaseHIDEventDriver"

  |   "IOProviderClass" = "IOHIDInterface"

  |   "LocationID" = 47

  |   "IOClass" = "AppleDeviceManagementHIDEventService"

  |   "HIDServiceSupport" = Yes

  |   "CFBundleIdentifierKernel" = "com.apple.driver.AppleTopCaseHIDEventDriver"

  |   "ProductIDArray" = (835)

  |   "ColorID" = 1

  |   "CountryCode" = 0

  |   "IOMatchCategory" = "IODefaultMatchCategory"

  |   "PrimaryUsage" = 11

  |   "IOProbeScore" = 7175

  |   "StandardType" = 0

  |   "IOGeneralInterest" = "IOCommand is not serializable"

  | }

  |

  +-o IOHIDEventServiceUserClient  <class IOHIDEventServiceUserClient, id 0x10000fcc9, !registered, !matched, active, busy 0, retain 6>

      {

        "IOUserClientDefaultLockingSetProperties" = Yes

        "IOUserClientDefaultLocking" = Yes

        "IOUserClientCreator" = "pid 587, WindowServer"

        "IOUserClientDefaultLockingSingleThreadExternalMethod" = No

        "IOUserClientEntitlements" = No

        "DebugState" = {"EventQueue"={"NoFullMsg"=0,"tail"=0,"NotificationForce"=0,"NotificationCount"=0,"head"=0}}

      }

      




+-o AppleDeviceManagementHIDEventService  <class AppleDeviceManagementHIDEventService, id 0x10002240d, registered, matched, active, busy 0 (0 ms), retain 7>

    {

      "IOMatchedAtBoot" = Yes

      "LowBatteryNotificationPercentage" = 2

      "PrimaryUsagePage" = 65280

      "BatteryFaultNotificationType" = "KBBatteryFault"

      "HasBattery" = Yes

      "VendorID" = 76

      "VersionNumber" = 0

      "Built-In" = No

      "DeviceAddress" = "c4-14-11-0c-ec-d0"

      "WakeReason" = "Host (0x01)"

      "Product" = "Magic Keyboard with Numeric Keypad"

      "SerialNumber" = "c4-14-11-0c-ec-d0"

      "Transport" = "Bluetooth"

      "BatteryLowNotificationType" = "ExKBLowBattery"

      "ProductID" = 620

      "DeviceUsagePairs" = ({"DeviceUsagePage"=65280,"DeviceUsage"=11},{"DeviceUsagePage"=65280,"DeviceUsage"=20})

      "IOPersonalityPublisher" = "com.apple.driver.AppleTopCaseHIDEventDriver"

      "BatteryPercent" = 68

      "BD_ADDR" = <c414110cecd0>

      "BatteryStatusNotificationType" = "BatteryStatusChanged"

      "CriticallyLowBatteryNotificationPercentage" = 1

      "ReportInterval" = 11250

      "RadioFW Version" = 352

      "VendorIDSource" = 1

      "STFW Version" = 2130

      "CFBundleIdentifier" = "com.apple.driver.AppleTopCaseHIDEventDriver"

      "IOProviderClass" = "IOHIDInterface"

      "LocationID" = 286059728

      "BluetoothDevice" = Yes

      "IOClass" = "AppleDeviceManagementHIDEventService"

      "HIDServiceSupport" = No

      "CFBundleIdentifierKernel" = "com.apple.driver.AppleTopCaseHIDEventDriver"

      "ProductIDArray" = (620)

      "BatteryStatusFlags" = 0

      "ColorID" = 0

      "IOMatchCategory" = "IODefaultMatchCategory"

      "CountryCode" = 0

      "IOProbeScore" = 7175

      "PrimaryUsage" = 11

      "IOGeneralInterest" = "IOCommand is not serializable"

      "BTFW Version" = 352

    }

    




+-o AppleDeviceManagementHIDEventService  <class AppleDeviceManagementHIDEventService, id 0x10002243d, registered, matched, active, busy 0 (1 ms), retain 7>

    {

      "IOMatchedAtBoot" = Yes

      "LowBatteryNotificationPercentage" = 2

      "PrimaryUsagePage" = 65280

      "BatteryFaultNotificationType" = "MOBatteryFault"

      "HasBattery" = Yes

      "VendorID" = 76

      "VersionNumber" = 0

      "Built-In" = No

      "DeviceAddress" = "98-46-0a-b4-c3-ef"

      "WakeReason" = "Button (0x03)"

      "Product" = "Magic Mouse"

      "SerialNumber" = "98-46-0a-b4-c3-ef"

      "Transport" = "Bluetooth"

      "BatteryLowNotificationType" = "MOLowBattery"

      "ProductID" = 617

      "DeviceUsagePairs" = ({"DeviceUsagePage"=65280,"DeviceUsage"=11},{"DeviceUsagePage"=65280,"DeviceUsage"=20})

      "IOPersonalityPublisher" = "com.apple.driver.AppleTopCaseHIDEventDriver"

      "MTFW Version" = 0

      "BD_ADDR" = <98460ab4c3ef>

      "BatteryPercent" = 75

      "BatteryStatusNotificationType" = "BatteryStatusChanged"

      "CriticallyLowBatteryNotificationPercentage" = 1

      "ReportInterval" = 11250

      "RadioFW Version" = 402

      "VendorIDSource" = 1

      "STFW Version" = 2144

      "CFBundleIdentifier" = "com.apple.driver.AppleTopCaseHIDEventDriver"

      "IOProviderClass" = "IOHIDInterface"

      "LocationID" = 179618799

      "BluetoothDevice" = Yes

      "IOClass" = "AppleDeviceManagementHIDEventService"

      "HIDServiceSupport" = No

      "CFBundleIdentifierKernel" = "com.apple.driver.AppleTopCaseHIDEventDriver"

      "ProductIDArray" = (617)

      "BatteryStatusFlags" = 0

      "ColorID" = 0

      "IOMatchCategory" = "IODefaultMatchCategory"

      "CountryCode" = 0

      "IOProbeScore" = 7175

      "PrimaryUsage" = 11

      "IOGeneralInterest" = "IOCommand is not serializable"

      "BTFW Version" = 402

    }
"""


class TestUtil:
    def test_extract_battery_info(self):
        mouse_bat = Util.extract_battery_info(test_output_mouse_and_keyboard, "Magic Mouse")
        kb_bat = Util.extract_battery_info(test_output_mouse_and_keyboard, "Magic Keyboard with Numeric Keypad")

        assert mouse_bat == 75
        assert kb_bat == 68

    def test_detect_devices(self):
        devices = Util.detect_devices(test_output_mouse_and_keyboard)
        assert devices == [
            Device(**{'is_bluetooth': False, 'vendor_id': 1452, 'product_id': 835,
             'product_name': 'Apple Internal Keyboard / Trackpad', 'has_battery': False, 'device_address': None}),
            Device(**{'is_bluetooth': True, 'vendor_id': 76, 'product_id': 620,
             'product_name': 'Magic Keyboard with Numeric Keypad', 'has_battery': True,
             'device_address': 'c4-14-11-0c-ec-d0'}),
            Device(**{'is_bluetooth': True, 'vendor_id': 76, 'product_id': 617, 'product_name': 'Magic Mouse',
             'has_battery': True, 'device_address': '98-46-0a-b4-c3-ef'})
        ]

        devices = Util.detect_devices(test_output_mouse_only)
        assert devices == [
            Device(**{'is_bluetooth': False, 'vendor_id': 1452, 'product_id': 835,
                      'product_name': 'Apple Internal Keyboard / Trackpad', 'has_battery': False,
                      'device_address': None}),
            Device(**{'is_bluetooth': True, 'vendor_id': 76, 'product_id': 617, 'product_name': 'Magic Mouse',
                      'has_battery': True, 'device_address': '98-46-0a-b4-c3-ef'})
        ]
