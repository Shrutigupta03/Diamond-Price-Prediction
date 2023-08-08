from setuptools import find_packages, setup
from typing import List

Hypen_e_dot ='-e .'

def get_requirements(file_path:str) -> List[str]:
    with open('requirements.txt', 'r') as f:
        if Hypen_e_dot in f.read():
            return []
        return f.read().splitlines()


setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Shruti-Gupta',
    author_email='shrutig1287@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)