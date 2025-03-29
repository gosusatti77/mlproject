from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path):
    """
    This function returns a list of requirements from the given file path.
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.read().splitlines()

        if '-e .' in requirements:
            requirements.remove('-e .')

setup(
    name="mlproject",
    version="0.0.1",
    author="Satti",
    author_email ="gosusatti77@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description="A small ML project",
)