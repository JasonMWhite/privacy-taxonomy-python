from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Privacy Taxonomy'
LONG_DESCRIPTION = "Python interface to Ethyca's Privacy Taxonomy"

setup(
        name="privacy_taxonmy", 
        version=VERSION,
        author="Jason White",
        author_email="actinolite.jw@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            'owlready2'
        ],        
        keywords=['python', 'privacy'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
        ]
)
