# DevicePilot SDK for Python

[![image](https://img.shields.io/pypi/v/devicepilot.svg)](https://pypi.org/project/requdevicepilotests/)
[![image](https://img.shields.io/pypi/l/devicepilot.svg)](https://pypi.org/project/devicepilot/)
[![image](https://img.shields.io/pypi/pyversions/devicepilot.svg)](https://pypi.org/project/devicepilot/)

www.devicepilot.com

DevicePilot is a universal cloud-based software service allowing you to easily locate, monitor and manage your connected devices at scale, with proactive management of the entire device lifecycle.

This library helps you quickly get started posting your device telemetry so you can begin exploring your IoT data in DevicePilot.

### Getting Started

* Sign up for a DevicePilot account if you haven't already!

> [You can book at demo at devicepilot.com](https://www.devicepilot.com/contact)

* Get your API key

> [Find your API Key in Settings > My User](https://app.devicepilot.com/#/settings/my-user)

* Add the DevicePilot library to your python project:

```
pip install devicepilot
```

* Start posting your device telemetry:

```python
    import devicepilot

    # api key should be explicitly provided, or stored in the environmental variable DP_API_KEY
    apikey = "your-devicepilot-api-key"

    record = {
        "$id": "unique-device-id", # this is used to identify your device
        # any valid json body will be converted into key:value telemetry:
        "ledColour": 'blue',
        "switchedOn": True,
        "temperature": 20,
    }
    # an array of record objects can also be provided

    devicepilot.post(record, apikey)
```

### Documentation

For more information about using DevicePilot, check out: https://help.devicepilot.com/
