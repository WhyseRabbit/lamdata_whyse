"""
Lambdata-- A project associated with Lambda Schools to create Data Science utility functions.
"""

import setuptools

REQUIRED = [
    "pandas",
    "numpy",
    "sklearn"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="lambdata_whyse",
    version="0.0.2",
    author="WhyseRabbit",
    description="A project associated with Lambda Schools to create Data Science utility functions.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/WhyseRabbit/lamdata_whyse",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
