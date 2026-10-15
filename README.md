<a className="gh-badge" href="https://datahub.io/core/world-cities"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

# Major cities of the world

A list of the major cities of the world, with the country and the first-level region each city is in. The data comes from GeoNames.

Column definitions and types are in `datapackage.json`.

## Data

`data/world-cities.csv` has one row per city. It lists cities with more than 15,000 inhabitants, plus capitals and seats of government, which can be smaller (for example Hamilton, the capital of Bermuda).

| Column | Meaning |
|---|---|
| `name` | Name of the city (the GeoNames name, in UTF-8, so it can contain accents and non-Latin letters), for example `Düsseldorf` |
| `country` | Country name. These are the ISO 3166-1 official short names, for example `Russian Federation`, `Viet Nam`, `Bolivia, Plurinational State of`. `Kosovo` is added by the script |
| `subcountry` | Name of the first-level region of the country, in ASCII, for example `North Rhine-Westphalia`. This is a state in the United States, and the major administrative area in other countries. See `admin1` on the [GeoNames website][geonames] |
| `geonameid` | GeoNames id of the city. This is the primary key |

### Known limitations

* `subcountry` is empty for cities that have no first-level region in GeoNames. This includes cities that are a whole state, such as Singapore and Vatican City. It is empty, not `N/A`. By default pandas reads an empty cell as missing (`NaN`). To keep empty strings instead: `pd.read_csv("data/world-cities.csv", keep_default_na=False)`.
* The name of a city is not unique within a country and subcountry. Some combinations of `country`, `subcountry` and `name` appear more than once. Use `geonameid` to identify a city.
* `country` uses the ISO names, which are not always the everyday names. For example Vatican City is `Holy See (Vatican City State)`.

## Data sources

* [GeoNames][geonames]: a list of worldwide place names. This repository uses two of its files, [cities15000.zip][cities] (the cities) and [admin1CodesASCII.txt][admin1] (the names of the first-level regions). Licence: [Creative Commons Attribution 4.0 International][cc-by] (see [License](#license)).
* [pycountry][pycountry]: a Python package that gives the ISO 3166-1 country names. It includes the data of the Debian [iso-codes][isocodes] project. Licence: LGPL-2.1 (see [License](#license)).

Changes made to the source data: from `cities15000.txt` the script keeps only the name, the GeoNames id, the country and the first-level region. The country code is replaced by the country name from pycountry. The first-level region code is replaced by the region's ASCII name from `admin1CodesASCII.txt`. All other columns (coordinates, population, alternate names, time zone and so on) are removed. The name `Kosovo` is added by the script for the GeoNames code `XK`, which pycountry does not know.

Not endorsed by, or affiliated with, GeoNames, pycountry or the iso-codes project.

[geonames]: https://www.geonames.org/
[cities]: https://download.geonames.org/export/dump/cities15000.zip
[admin1]: https://download.geonames.org/export/dump/admin1CodesASCII.txt
[cc-by]: https://creativecommons.org/licenses/by/4.0/
[pycountry]: https://github.com/pycountry/pycountry
[isocodes]: https://salsa.debian.org/iso-codes-team/iso-codes

## Preparation

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
![.github/workflows/actions.yml](https://github.com/datasets/world-cities/actions/workflows/actions.yml/badge.svg?branch=main)

The script needs Python 3.12 and the packages in `scripts/requirements.txt` (requests, pycountry, pandas and frictionless). Install them and run the script from the repository root:

```
pip install -r scripts/requirements.txt
python scripts/process.py
```

The script downloads the two GeoNames files and writes `data/world-cities.csv`.

A GitHub workflow rebuilds the data on the 1st of every month (at 00:00 UTC) and on every push to `main`. It validates `datapackage.json` with [Frictionless](https://framework.frictionlessdata.io/) and commits `data/world-cities.csv` if it changed.

## License

The city data comes from GeoNames and is licensed under the [Creative Commons Attribution 4.0 International License][cc-by]. If you use it, credit GeoNames with a link, say which licence applies, and say that the data was changed (see the changes listed under Data sources). GeoNames provides the data "as is" without warranty or any representation of accuracy, timeliness or completeness. A link back or credit to [Lexman][lexman] and the [Open Knowledge Foundation][okfn] is also appreciated. See also [ATTRIBUTION.txt](ATTRIBUTION.txt).

The country names come from pycountry, which is licensed under the LGPL-2.1 and includes iso-codes data (LGPL-2.1-or-later). ISO says its publications are protected by copyright. We could not establish whether this affects short country names, and the LGPL is a software licence. We found nothing that puts LGPL terms on this CSV, so we think the risk is low, but the position is unclear.

All source code is licensed under the [MIT licence](LICENSE).

[lexman]: https://github.com/lexman
[okfn]: https://okfn.org/
