from homeassistant.helpers.entity import Entity 
import mdstat 
import simplejson as json 
from types import SimpleNamespace

# Now I'm studing how make it in C++, because I don't know very good Python :)

def setup_platform(hass, config, add_entities, discovery_info=None):
    device = config["device"]

    # Check if the device is a RAID device, and check if it exist, after that make the entity

    add_entities([mdadm()])


class mdadm(Entity):

    def __init__(self):
        self._state = None

    @property
    def name(self):
        return 'MDADM Raid Status'

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return None

    def update(self):

        mdstat_status = mdstat.parse()
        data = json.dumps(mdstat_status)
        x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

        device = 'md0' # Device insert into configuration.yaml (in this case is md0)
        device_config = getattr(x.devices, device)



        self._attribute1 = device_config.read_only

        self._state = device_config.active
