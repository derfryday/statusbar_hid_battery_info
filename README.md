# What is this and why?
#### What is it?: 
This is a daemon that displays the battery level of your bluetooth HID devices and notifies you when the battery level is low.
The level at which you get notified can be configured in the config file.

#### Okay, but why?:
Some of my co-workers complained about MacOS only telling you about the impending lack of battery power when you are already running on fumes.

This wouldn't be an issue with real bluetooth mice, but imagine you have the abomination that is the Magic Mouse which is absolutely useless while it's charging.

So I made this tool to notify you when you want to be notified instead of when it's basically too late. With the added benefit of being able to see the battery level of your devices in the statusbar.

# Installation:
```bash
wget "https://github.com/derfryday/statusbar_hid_battery_info/releases/latest/download/StatusbarHIDBattInfo"

chmod +x StatusbarHIDBattInfo

./StatusbarHIDBattInfo --setup  # this will create the default config file
./StatusbarHIDBattInfo --install  # this will install the launch agent and start it
```

# Uninstallation:
```bash
./StatusbarHIDBattInfo --uninstall  # this will stop and uninstall the launch agent
```
# Building from Source
```bash
make
```

# Configuration:
## Display names:
You can configure the display names of your devices in the config file.

Display Names are entirely optional and only used in the statusbar.

```json
"display_names": {
    "Magic Keyboard with Numeric Keypad": "⌨️",
    "Magic Mouse": "🖱️"
}
```

## Notification settings:
You can configure at which battery level you will get a notification and how often you will get notified.

```json
"notification_settings": {
    "threshold": 20, // battery level threshold in percent
    "notification_interval": 60 // notification interval in minutes
}
```

# Misc:
## Config file location:
```bash
~/.config/statusbar_hid_batt_info.json
```

## Log file location:
```bash
~/Library/Logs/StatusbarHIDBattInfo.log
```

## LaunchAgent file location:
```bash
~/Library/LaunchAgents/dev.derfryday.statusbar-hid-batt-info.plist
```

## Default Config:
```json
{
  "display_names": {
    "Magic Keyboard with Numeric Keypad": "⌨️",
    "Magic Mouse": "🖱️"
  },
  "notification_settings": {
    "threshold": 20,
    "notification_interval": 60
  }
}
```
