import os
import pkg_resources
from typing import List, Union
import difflib
from setuptools import find_packages, setup

CLASSIFIERS = [
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3 :: Only',
]


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as _in:
        return _in.read()


def check_requirements(fname:str) -> Union[List[str], None]:
    """Returns list of missed packages names, which should be installed. """
    installed_packages = pkg_resources.working_set
    # installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
    #                                   for i in installed_packages])
    installed_packages_list = [(f"{i.key}", f"{i.version}") for i in installed_packages]
    installed_packages_dict = dict(installed_packages_list)

    required_packages = read(fname).splitlines()
    required_packages = list(pkg_resources.parse_requirements(required_packages))
    required_packages_list = [(f"{i.key}", "".join(list(*i.specs))) for i in required_packages]
    required_packages_dict = dict(required_packages_list)

    diff = set(required_packages_dict.keys()).difference(installed_packages_dict.keys())
    pkg_list = [f"{pkg_name}{required_packages_dict[pkg_name]}" for pkg_name in diff]
    return pkg_list if len(pkg_list) != 0 else None


_VERSION = '0.3.1'

setup(version=_VERSION,
      name="civisml-extensions",
      author="Civis Analytics",
      author_email="opensource@civisanalytics.com",
      url="https://www.civisanalytics.com",
      description="scikit-learn-compatible estimators from Civis Analytics",
      packages=find_packages(),
      install_requires=check_requirements('requirements.txt'),
      long_description=read('README.rst'),
      long_description_content_type='text/x-rst',
      include_package_data=True,
      license="BSD-3",
      classifiers=CLASSIFIERS,
      python_requires=">=3.6")
