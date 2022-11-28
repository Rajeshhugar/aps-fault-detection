from setuptools import find_packages,setup

from typing import List

HYPEN_E_DOT='-e .'
REQUIREMENT_FILES_NAME ='requirements.txt'


def get_requirements()->List[str]:
    with open(REQUIREMENT_FILES_NAME) as requirement_files:
        requirement_list= requirement_files.readlines()
    requirement_list=[requirement_name.replace("/n","") for requirement_name in requirement_list]

    if HYPEN_E_DOT in requirement_list:
        requirement_list.remove(HYPEN_E_DOT)
    return requirement_list


setup(
    name="sensor",
    version="0.0.1",
    author="ineuron",
    author_email="hugarrajesh@gmail.com",
    packages=find_packages(),
    install_requires =get_requirements()
)

