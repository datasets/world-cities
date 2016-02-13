These scripts retrieve data from geoname's website and computes a the ``data/world-cities.csv`` file.


## Install the dependencies
The preparation process work under Linux and Windows (under a git bash session).

The scripts consist of some shell and python 2.7 code that are glued together with [tuttle](http://github.com/lexman/tuttle), a *make for data*. 
Therefore, you'll need to install [git](https://git-scm.com/downloads), [Python](https://www.python.org/) and [tuttle](https://github.com/lexman/tuttle/releases).

	
## Run the scripts

After you have checked out the code, go into the script directory and run the processing :

    cd scripts
	tuttle run
	