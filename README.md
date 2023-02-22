# SpotPriceWatch

## Kuvaus
SpotPriceWatch on sivu, joka näyttää automaattisesti päivän pörssisähkön hinnan.
##HUOM! 
Toistaiseksi sovellus ei ole tuotannossa
## Ominaisuudet
- Tämän tunnin hinta
- Päivän halvin hinta
- Päivän kallein hinta
- Päivän sähköhinnat siististi taulukossa


## Nykytilanne
- Sovelluksessa toimii yllämainitut ominaisuudet.
- Sovelluksella on maltillinen mutta tyylikäs ja selkeä ulkoasu

## Tulevaisuus
- Sovellukseen tulee paranneltu ulkoasu
- Mahdollisuus katsoa tulevan päivän sähköjen hinnat, mikäli ne ovat jo tulleet NordPoolista
- Muita ominaisuuksia

### Asennus ja käyttäminen

Aloita kloonaamalla repositorio, lisää alla olevat komennot terminaalissa

git clone https://github.com/A00N/SpotPriceWatch

curl -sSL https://install.python-poetry.org/. | POETRY_HOME=$HOME/.local python3 

export PATH="$HOME/.local/bin:$PATH"

poetry update

poetry shell

cd src

flask run
