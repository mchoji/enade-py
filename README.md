[![Build Status](https://travis-ci.com/mchoji/enade-py.svg?branch=main)](https://travis-ci.com/mchoji/enade-py)
[![Documentation Status](https://readthedocs.org/projects/enade-py/badge/?version=latest)](https://enade-py.readthedocs.io/en/latest/?badge=latest)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/mchoji/enade-py.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/mchoji/enade-py/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/mchoji/enade-py.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/mchoji/enade-py/context:python)
[![Maintainability](https://api.codeclimate.com/v1/badges/152e1dbef34e563ace98/maintainability)](https://codeclimate.com/github/mchoji/enade-py/maintainability)
[![Requirements Status](https://requires.io/github/mchoji/enade-py/requirements.svg?branch=main)](https://requires.io/github/mchoji/enade-py/requirements/?branch=main)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![GitHub license](https://img.shields.io/github/license/mchoji/enade-py)](https://github.com/mchoji/enade-py/blob/master/LICENSE.txt)
[![PyPI version fury.io](https://badge.fury.io/py/enade-py.svg)](https://pypi.python.org/pypi/enade-py/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/enade-py.svg)](https://pypi.python.org/pypi/enade-py/)
[![PyPI status](https://img.shields.io/pypi/status/enade-py.svg)](https://pypi.python.org/pypi/enade-py/)
[![DOI](https://zenodo.org/badge/303499390.svg)](https://zenodo.org/badge/latestdoi/303499390)

# enade-py

 A library for facilitating data analysis over Enade microdata.


## Description

*enade-py* comprises a set of functions for helping researchers and Educational
Data Mining (EDM) enthusiasts through the data mining process using Enade
microdata.

The Enade microdata datasets are provided by [Inep] and consist of informations from brazilian
undergraduate students and their performance on Enade (a national exam taken at
the end of the course).

Enade datasets contain attributes related to:

* the exam itself;
* the student;
* the institution;
* performance on the exam;
* socioeconomic questions;
* and more.


## Getting Started

### Installing with pip
To install the latest release of *enade-py*, just run

```shell
pip install enade-py
```

### Manual Installation

In order to set up the necessary environment:

0. clone the repository on your machine
   ```
   git clone https://github.com/mchoji/enade-py.git
   ```
1. create an environment `enade-py` with the help of [conda],
   ```
   conda env create -f environment.yaml
   ```
2. activate the new environment with
   ```
   conda activate enade-py
   ```
3. install `enade-py` with:
   ```
   python setup.py install # or `develop`
   ```

Optional and needed only once after `git clone`:

4. install several [pre-commit] git hooks with:
   ```
   pre-commit install
   ```
   and checkout the configuration under `.pre-commit-config.yaml`.
   The `-n, --no-verify` flag of `git commit` can be used to deactivate pre-commit hooks temporarily.

5. install [nbstripout] git hooks to remove the output cells of committed notebooks with:
   ```
   nbstripout --install --attributes notebooks/.gitattributes
   ```
   This is useful to avoid large diffs due to plots in your notebooks.
   A simple `nbstripout --uninstall` will revert these changes.


Then take a look into the `scripts` and `notebooks` folders.

### Dependency Management & Reproducibility

1. Abstract (unpinned) dependencies are kept in `environment.yaml` (for
   development) and in `setup.cfg` (for `pip`)
2. Concrete dependencies are kept in `environment.lock.yaml` for the exact
   reproduction of the development environment with:
   ```
   conda env export -n enade-py -f environment.lock.yaml
   ```
   For multi-OS development, consider using `--no-builds` during the export.
3. Update your current environment with respect to a new `environment.lock.yaml` using:
   ```
   conda env update -f environment.lock.yaml --prune
   ```
4. Data files are tracked with [dvc]. To pull the latest version, run the
   following command after `git clone` or `git pull`:
   ```
   dvc pull
   ```

## Project Organization

```
├── AUTHORS.rst             <- List of developers and maintainers.
├── CHANGELOG.rst           <- Changelog to keep track of new features and fixes.
├── LICENSE.txt             <- License as chosen on the command-line.
├── README.md               <- The top-level README for developers.
├── configs                 <- Directory for configurations of model & application.
├── data
│   ├── external            <- Data from third party sources.
│   ├── interim             <- Intermediate data that has been transformed.
│   ├── preprocessed        <- The final, canonical data sets for modeling.
│   └── raw                 <- The original, immutable data dump.
├── docs                    <- Directory for Sphinx documentation in rst or md.
├── environment.yaml        <- The conda environment file for reproducibility.
├── models                  <- Trained and serialized models, model predictions,
│                              or model summaries.
├── notebooks               <- Jupyter notebooks. Naming convention is a number (for
│                              ordering), the creator's initials and a description,
│                              e.g. `1.0-mc-initial-data-exploration`.
├── references              <- Data dictionaries, manuals, and all other materials.
├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures             <- Generated plots and figures for reports.
├── scripts                 <- Analysis and production scripts which import the
│                              actual PYTHON_PKG, e.g. train_model.
├── setup.cfg               <- Declarative configuration of this project.
├── setup.py                <- Use `python setup.py develop` to install for development or
|                              or create a distribution with `python setup.py bdist_wheel`.
├── src
│   └── enadepy             <- Actual Python package where the main functionality goes.
├── tests                   <- Unit tests which can be run with `py.test`.
├── .coveragerc             <- Configuration for coverage reports of unit tests.
├── .isort.cfg              <- Configuration for git hook that sorts imports.
└── .pre-commit-config.yaml <- Configuration of pre-commit git hooks.
```


## Versioning
Versions defined according to [SemVer](https://semver.org). For the versions
available, see the [tags on this repository](https://github.com/mchoji/enade-py/tags).


## Authors
- M. Choji - [mchoji](https://github.com/mchoji)


## License
*enade-py* is licensed under the MIT License.
See [LICENSE](LICENSE.txt) for more information.


## Note

This project has been set up using PyScaffold 3.2.3 and the [dsproject extension] 0.4.
For details and usage information on PyScaffold see https://pyscaffold.org/.

[Inep]: http://portal.inep.gov.br/microdados
[dvc]: https://dvc.org/
[conda]: https://docs.conda.io/
[pre-commit]: https://pre-commit.com/
[Jupyter]: https://jupyter.org/
[nbstripout]: https://github.com/kynan/nbstripout
[Google style]: http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
[dsproject extension]: https://github.com/pyscaffold/pyscaffoldext-dsproject
