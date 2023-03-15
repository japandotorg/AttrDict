"""
To install AttrDict:

    python setup.py install
"""
from setuptools import setup


DESCRIPTION = "A dict with attribute-style access"

try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    LONG_DESCRIPTION = DESCRIPTION


setup(
    name="attrdict",
    version="2.0.1",
    author="Brendan Curran-Johnson",
    author_email="brendan@bcjbcj.ca",
    packages=["attrdict",],
    url="https://github.com/bcj/AttrDict",
    license="MIT License",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: 7 - Active",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy3",
    ],
    install_requires=(
        'six',
    ),
    tests_require=(
        'nose>=1.0',
        'coverage',
    ),
    zip_safe=True,
)
