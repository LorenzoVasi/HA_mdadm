import logging # Home Assistant LOG
from homeassistant.helpers.entity import Entity # Home Assistant Entity
import mdstat # MDSTAT for import data from MDADM
import simplejson as json # JSON
from types import SimpleNamespace # Make object


_LOGGER = logging.getLogger(__name__) # Global Variable _ Logger


def setup_platform(hass, config, add_entities, discovery_info=None):
    device = config["device"]
    add_entities([mdadm(device)])
    return True


class mdadm(Entity):

    def __init__(self, device): # setup of entity and self object
        self._device = device
        self._state = None
        self._personality = None
        self._status_disks_not_working = None
        self._status_synced = None
        self._disks_number = None

    @property
    def name(self): # entity name
        name = 'RAID status /dev/'+self._device 
        return name

    @property # entity status
    def state(self):
        return self._state

    @property
    def device_state_attributes(self): # Attribute list
        attributes = {
            "raid-type": self._personality,
            "disks_number": self._disks_number,
            "disks_not_working": self._status_disks_not_working,
            "sync": self._status_synced
        }
        return attributes
        
    def update(self):

        # Loading data from MDADM into x class 
        x = json.loads(json.dumps(mdstat.parse()), object_hook=lambda d: SimpleNamespace(**d))
        device_config = getattr(x.devices, self._device)

        # Status
        if device_config.active == True:
            self._state = 'on'
        else:
            self._state = 'off'

        # Sync attribute
        for tmp in device_config.status.synced:
            if tmp == False:
                self._status_synced = False
                break
            else:
                self._status_synced = True

        # Other attributes
        self._personality = device_config.personality
        self._status_disks_not_working = device_config.status.raid_disks - device_config.status.non_degraded_disks
        self._disks_number = device_config.status.raid_disks