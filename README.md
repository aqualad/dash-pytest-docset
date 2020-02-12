Dash Docset for pytest 3.10.1
=============================

# Steps to generate
1. Clone https://github.com/pytest-dev/pytest and checkout the version you want to build docs for
1. Modify the pytest doc config file using `dashify_pytest.patch` as a guide
1. Create a pipenv using python 3.7.3 `pipenv shell --python 3.7.3`
1. Install deps for pytest
	* `python setup.py install`
	* `pip install "sphinx<2.0"` (had issues with older docset above 2)
	* `pip install doc2dash`
1. In pytest/doc/en: `make html`
1. Copy \_build dir to a root directory in this project like pytest-3.10.1
1. Run the doc2dash command
	* `doc2dash -A -n pytest --online-redirect-url https://docs.pytest.org/en/3.10.1/contents.html -i ../../icon@2x.png html/ -f`
