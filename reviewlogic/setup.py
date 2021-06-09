from setuptools import setup, find_packages

setup(
    name="reviewlogic",
    version="0.1.0",
    packages=find_packages(exclude=["tests.*", "tests"]),
)
