from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'LazyBugged'
LONG_DESCRIPTION = 'Python package'

setup(
        name="lazybugged", 
        version=VERSION,
        author="Max Base and Tarunav.BA",
        author_email="tarunavba@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
