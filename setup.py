from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="basicpack",
    version="0.0.2",
    author="rim bd",
    author_email="bendhaou.rim@gmail.com",
    description="An example of basic package",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/organizationrim/basicpack",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)