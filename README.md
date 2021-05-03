# Home Assistant MDADM Status RAID
Hi, this is my first project for Home Assistant. I want make a custom component for check my RAID Status in my Server.

## Requirements
`mdadm` installed in the base machine  

## YAML Configuration
```yaml
# Example configuration.yaml entry
binary_sensor:
  - platform: mdadm_state
    device: # NOT currently available 
```

## Contributions
`mdstat` (Python library)
https://pypi.org/project/mdstat/
