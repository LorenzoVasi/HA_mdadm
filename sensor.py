DOMAIN = "mdadm_state"

def setup(hass, config):
    from homeassistant.helpers.entity import Entity # Importo libreria per creare entita
    import mdstat # Importo libreria MDSTAT installata da manifest.json
    import json # Importo libreria JSON per leggere dati JSON
    from types import SimpleNamespace # Da vedere se disponibile su Home Assistant Core, altrimenti da importare 

    return True # Inizializzazione effettuata e completata


def setup_platform(hass, config, add_entities, discovery_info=None):

    device = config[CONF_DEVICE]    
    
    add_entities([mdadm_state()]) # Creo nuova entita chiamata sensor.mdadm_state


class mdadm_state(Entity):
    def __init__(self):
        self._state = None # Inizializzazione del sensore

    @property
    def name(self):
        return 'MDADM Raid Status' # Ritorna il nome del sensore 
    
    @property
    def state(self):
        return self._state # Ritorna lo stato del sensore

    @property
    def update(self):
        # Qui devo eseguire il codice da decifrare in JSON

        data = json.dumps(mdstat.parse()) # Prendo il codice ricevuto da mdstat e lo trasformo in vero json
        x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d)) # Trasformo il risultato JSON in una classe
        
        
        self._state = x.devices.md0.active

    