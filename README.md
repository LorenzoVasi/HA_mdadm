# RAID Status - Custom Component - Home Assistant

This is a custom component that can be used to monitor the status of a RAID device created with `mdadm`

 ## Requirements

- `mdadm` installed into local server

## How to install

HACS:

1. Go to HACS -> 3dots -> Custom Repositories -> Copy repository link and set "Integration" as Category
2. Search "RAID Status - MDADM" on HACS Integrations 

Without HACS: 

1. Download the repository
2. Copy the 'custom_components/mdadm_state' folder into the configuration folder


## Setup YAML Configuration

```yaml
# Example configuration.yaml entry
binary_sensor:
  - platform: mdadm_state
    device: devicename
```

### Configuration Variables

`device` [**REQUIRED**] : name of device. Example `device: md0` if the path of device is `/dev/md0`

## Contributions

`mdstat` library: https://pypi.org/project/mdstat/

`simplejson` library: https://pypi.org/project/simplejson/



