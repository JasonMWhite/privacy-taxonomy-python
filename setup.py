from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Privacy Taxonomy'
LONG_DESCRIPTION = "Python interface to Ethyca's Privacy Taxonomy"

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="privacy_taxonmy", 
        version=VERSION,
        author="Jason White",
        author_email="actinolite.jw@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'privacy'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
        ]
)
