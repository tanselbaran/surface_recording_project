import numpy as np
from utils.experiment_classes import *
class sixtyfour_ch_single_penetrating(Probe):
    def __init__(self,):
        self.nr_of_groups = 64
        self.type = 'linear'
        self.nr_of_electrodes_per_group = 1
        self.nr_of_electrodes = 64

    def get_channel_mapping(self, amplifier):
        if amplifier == 'rhd':
            id = {
            0:[51], 1:[53], 2:[48], 3:[37], 4:[61], 5:[59], 6:[36], 7:[44], 
            8:[63], 9:[58], 10:[55], 11:[50], 12:[47], 13:[42], 14:[39], 15:[34], 
            16:[62], 17:[57], 18:[54], 19:[49], 20:[46], 21:[41], 22:[38], 23:[33], 
            24:[52], 25:[60], 26:[40], 27:[35], 28:[56], 29:[43], 30:[45], 31:[32], 
            32:[3], 33:[4], 34:[5], 35:[16], 36:[13], 37:[0], 38:[24], 39:[19], 
            40:[30], 41:[25], 42:[22], 43:[17], 44:[14], 45:[9], 46:[6], 47:[2],  
            48:[31], 49:[26], 50:[23], 51:[18], 52:[15], 53:[10], 54:[8], 55:[1], 
            56:[7], 57:[11], 58:[21], 59:[20], 60:[12], 61:[27], 62:[29], 63:[28]
            }
        self.id = id

    def get_channel_coords(self):
        self.coords = [[[0, 0]], [[0, 80]], [[0, 160]], [[0, 240]], [[0, 320]], [[0, 400]], [[0, 480]], [[0, 560]],
        [[0, 640]], [[0, 720]], [[0, 800]], [[0, 880]], [[0, 960]], [[0, 1040]], [[0, 1120]], [[0, 1200]], 
        [[0, 1280]], [[0, 1360]], [[0, 1440]], [[0, 1520]], [[0, 1600]], [[0, 1680]], [[0, 1760]], [[0, 1840]],
        [[0, 1920]], [[0, 2000]], [[0, 2080]], [[0, 2160]], [[0, 2240]], [[0, 2320]], [[0, 2400]], [[0, 2480]],
        [[0, 2560]], [[0, 2640]], [[0, 2720]], [[0, 2800]], [[0, 2880]], [[0, 2960]], [[0, 3040]], [[0, 3120]],
        [[0, 3200]], [[0, 3280]], [[0, 3360]], [[0, 3440]], [[0, 3520]], [[0, 3600]], [[0, 3680]], [[0, 3760]],
        [[0, 3840]], [[0, 3920]], [[0, 4000]], [[0, 4080]], [[0, 4160]], [[0, 4240]], [[0, 4320]], [[0, 4400]], 
        [[0, 4480]], [[0, 4560]], [[0, 4640]], [[0, 4720]], [[0, 4800]], [[0, 4880]], [[0, 4960]], [[0, 5040]]]
        
