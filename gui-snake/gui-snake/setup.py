from setuptools import setup, find_packages

setup(
    name='gui-snake',
    version='0.1.0',
    author='Amir Naseredini',
    author_email='amir.naseredini@canonical.com',
    packages=find_packages(),
    install_requires=[
        'pygame',
    ]
)
