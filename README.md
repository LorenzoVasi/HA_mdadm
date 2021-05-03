# Home Assistant MDADM Status RAID
Hi, this is my first project for Home Assistant. I want make a custom component for check my RAID Status in my Server.

## Requirements
`mdadm` installed in the base machine  

## How to install
1. Download the repository
2. Copy 'mdadm_state' folder into custom_components folder (if it doesn't exist, make it) 
3. Edit `configuration.yaml`:

### YAML Configuration
```yaml
# Example configuration.yaml entry
binary_sensor:
  - platform: mdadm_state
    device: # NOT currently available 
```

## Contributions
`mdstat` (Python library)
https://pypi.org/project/mdstat/
