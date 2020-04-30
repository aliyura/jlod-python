from setuptools import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jlod",
    version="0.0.1",
    author="JLOD.ORG",
    author_email="contact@jload.org",
    description="Self Contained Document Oriented Database",
    long_description="JLOD stands for JSON Local Document Database, it is a serverless in-process library that implements a self-contained document-oriented database use for storing small application data within an application without an internet connection. The database is like MongoDB, it uses Collection, Documents, and JSON objects.  The JLOD is a version of SQLite in object-oriented format, the JLOD collections can be exported to Remote MongoDB collection as well as remote MongoDB collection can also be imported to the JLOD database. JLOD is an embedded document-oriented database library. Unlike MongoDB.  JLOD does not have a separate server process. JLOD reads and writes the data to ordinary disk files.  The complete JLOD database along with the collections and the documents are contained in a disk file. The folder is a database in JLOD while the file is a collection, and each line in the file is a document.",
    long_description_content_type="text/markdown",
    url="https://github.com/rabs-developer/jlod_db",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
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
