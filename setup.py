from setuptools import find_packages,setup


def get_requirements():
    pass



setup(
    name="sensor",
    version="0.0.1",
    author="ineuron",
    author_email="hugarrajesh@gmail.com"
    packages=find_packages()
    install_requires =get_requirements(),
)