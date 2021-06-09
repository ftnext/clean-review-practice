from setuptools import find_packages, setup

setup(
    name="reviewlogic",
    version="0.1.0",
    packages=find_packages(exclude=["tests.*", "tests"]),
)
