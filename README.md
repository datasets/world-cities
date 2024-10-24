<a href="https://datahub.io/core/world-cities"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25)" alt="badge" /></a>

List of major cities in the world

## Data

The data is extracted from [geonames][geonames], a very exhaustive list of worldwide toponyms.

This [datapackage][datapackage] only list cities above 15,000 inhabitants. Each city is associated with its 
country and subcountry to reduce the number of ambiguities. Subcountry can be the name of a state (eg in 
United Kingdom or the United States of America) or the major administrative section (eg ''region'' in France''). 
See ``admin1`` field on [geonames website][geonames] for further info about subcountry.

Notice that :
* some cities like *Vatican city* or *Singapore* are a whole state so they don't belong to any subcountry. Therefore subcountry is ``N/A``.
* There is no guaranty that a city has a unique name in a country and subcountry (At the time of writing, there are about 60 ambiguities). But for each city, 
the source data primary key ``geonameid`` is provided.

[geonames]: http://www.geonames.org/
[datapackage]: http://dataprotocols.org/data-packages/


## Preparation

## Preparation

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
![.github/workflows/actions.yml](https://github.com/datasets/world-cities/actions/workflows/actions.yml/badge.svg?branch=master)

This repository uses [dataflows](https://github.com/datahq/dataflows) to process and normalize the data.

You first need to install the dependencies:

```
pip install -r scripts/requirements.txt
```

Then run the script

```
python scripts/process.py
```

## License

All data is licensed under the [Creative Common Attribution License][CC] as is the original data from [geonames][geonames]. This means you have to credit [geonames][geonames] when using the data. And while no credit is formally required a link back or credit to [Lexman][lexman] and the [Open Knowledge Foundation][okfn] is much appreciated.

All source code is licensed under the [MIT licence][mit].

[CC]: http://creativecommons.org/licenses/by/3.0/
[mit]: https://opensource.org/licenses/MIT
[geonames]: http://www.geonames.org/
[pddl]: http://opendatacommons.org/licenses/pddl/1.0/
[lexman]: http://github.com/lexman
[okfn]: http://okfn.org/




