from setuptools import setup, find_packages

VERSION = '0.0.5'
DESCRIPTION = 'A package that helps the process of loading multiple files and plotting the data inside.'
LONG_DESCRIPTION = 'A package that helps the process of loading multiple files and plotting the data inside.'

# Setting up
setup(
    name="quyckplot",
    version=VERSION,
    author="Takanori Akieda",
    author_email="<takanori.codron@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['numpy', 'scipy', 'matplotlib', 'pandas'],
    keywords=['python', 'data analysis', 'scientific'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)