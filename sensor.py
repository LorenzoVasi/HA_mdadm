DOMAIN = "mdadm_state"

def setup(hass, config):
    from homeassistant.helpers.entity import Entity # Importo libreria per creare entita
    import mdstat # Importo libreria MDSTAT installata da manifest.json
    import json # Importo libreria JSON per leggere dati JSON


    return True # Inizializzazione effettuata e completata


def setup_platform(hass, config, add_entities, discovery_info=None):
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

        jsonData = mdstat.parse()
        jsonToPy = json.loads(jsonData)
        

    