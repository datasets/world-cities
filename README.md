List of major cities in the world

## Data

The data is extracted from geonames [geonames], a very exhaustive list of worldwide toponymes.

This datapackage [datapackage] only list cities above 15,000 inhabitants. Each city is associated with the 
country and the subcountry to reduce the number of ambiguities. Subcountry can be the name of a state (eg in 
the United States of America or United Kingdom) or the major administrative section (eg ''region'' in France''). 
More info about subcountry is available on the [geonames website][geonames] on ''admin1'' field.

Notice that :
* some cities like ''Vatican city'' or ''Singapore'' are a state themselves so they don't belong to any subcountry. Therefore subcountry is ''N/A''.
* There is no guaranty that a city has a uniq name in a country and a subcountry. See [ambiguities] for a list of duplicate. For each city, 
the source data primary key ''geonameid'' is provided.

[geonames]: http://www.geonames.com/
[datapackage] : http://www.okfn.org/datapackage
[ambiguities] : http://sisyphus.lexman.org/workspaces/world-cities/scripts/ambiguities.csv

## Preparation

You can run the script yourself to update the data and publish them to github : see [scripts README](scripts/README.md)

## License

All source code is licenced under the [MIT licence][mit].

The original data licence is Creative Common ???, and I, the maintainer,
explicitly license this file under the [Open Data Commons Public Domain Dedication and
License][pddl].

Note that while no credit is formally required a link back or credit to [geonames][geonames], [Lexman][lexman] and 
the [Open Knowledge Foundation][okfn] is much appreciated.

[mit]: http://???/
[geonames]: http://www.geonames.com/
[pddl]: http://opendatacommons.org/licenses/pddl/1.0/
[lexman]: http://github.com/lexman
[okfn]: http://okfn.org/




