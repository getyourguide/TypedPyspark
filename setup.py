# type: ignore

"""
This file is only used for installing mltools for development purposes.
For distribution the source of truth is poetry's pyproject.toml
"""
import setuptools

setuptools.setup(
    name="typed_pyspark",
    version="0.0.5",
    author="Jean Carlo Machado",
    author_email="engineering.data-products@getyourguide.com",
    description="Contains a set of abstractions to type annotate and validate dataframes in pyspark",
    url="https://github.com/getyourguide/TypedPyspark",
    packages=setuptools.find_packages(),
    install_requires=[],
    package_data={},
)
