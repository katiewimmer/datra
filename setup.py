
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datra", 
    version="0.0.1",
    author="Hannah Agwunobi",
    author_email="ohs.hannaha@gmail.com",
    description="Library to increase transparency of ML data sets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hagwunobi21/datra",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)