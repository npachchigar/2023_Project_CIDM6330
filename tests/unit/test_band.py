from allocation.domain.model import Band

def test_create_band():
    band = Band(name="Arijit Singh", genre="Bollywood")
    assert band.name == "Arijit Singh"
    assert band.genre == "Bollywood"

def test_band_str():
    band = Band(name="Arijit Singh", genre="Bollywood")
    assert str(band) == "Arijit Singh (Bollywood)"

def test_band_repr():
    band = Band(name="Arijit Singh", genre="Bollywood")
    assert repr(band) == f"Band(name='Arijit Singh', genre='Bollywood')"