"""
Solfeggio Frequencies
"""
import audiogen

chakras = {'first':'174','second':'285','third':'396','fourth':'417','fifth':'528','sixth':'639','seventh':'741','eigth':'852','nineth':'963'}
for chakra in chakras:
    try:
        audiogen.sampler.play(audiogen.tone(int(chakras.get(chakra,""))))
    except:
        pass