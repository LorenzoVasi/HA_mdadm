from homeassistant.helpers.entity import Entity 
import mdstat 
import simplejson as json 
from types import SimpleNamespace

def setup_platform(hass, config, add_entities, discovery_info=None):

    # device = config["device"] // This is the next step, load from configuration.yaml
    add_entities([mdadm()])


class mdadm(Entity):

    def __init__(self): # __init__
        self._state = None
        self._read_only = None
        self._resync = None

    @property
    def name(self): # Name of Entity 
        return 'MDADM Raid Status'

    @property # This is the function of state (return as state)
    def state(self):
        return self._state

    @property
    def device_class(self): # This is the device class of the device
        return 'connectivity'

    @property
    def unit_of_measurement(self): # Unit of measurament (in this case it isn't needed)
        return None

    @property
    def device_state_attributes(self): # This is the list of attributes
        attributes = {
            "read_only": self._read_only,
            "resync": self._resync
        }
        return attributes

    def update(self):

        # Take data from mdstat and load it on an object called x 
        mdstat_status = mdstat.parse()
        data = json.dumps(mdstat_status)
        x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))


        device = 'md0' # This is a debug device, not loaded by configuration.yaml


        device_config = getattr(x.devices, device) # Take devices that I want to view (conf.yaml)

        # This is the status of RAID Device
        if device_config.active == True:
            tmp = 'on'
        else:
            tmp = 'off'
        self._state = tmp


        # There are other things loaded by mdstat and insert into the entity as attributes
        self._read_only = device_config.read_only
        self._resync = device_config.resync
