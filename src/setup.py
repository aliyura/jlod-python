from setuptools import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jlod_db",
    version="0.0.1",
    author="Rabiu Aliyu [ Rabs ]",
    author_email="Net.RabiuAliyu@Gmail.com",
    description="A small local database package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rabs-developer/jlod_db",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MTN Approved :: TT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pymongo'
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'jlod=jlod_cli:main',
        ],
    },
)
