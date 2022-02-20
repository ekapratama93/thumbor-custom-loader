import os
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = \
        'Thumbor custom HTTP loader to replace hosts to a single host'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="thumbor_custom_loader",
    version="0.1.0",
    author="ekapratama93",
    description=(
        "Thumbor custom HTTP loader to replace hosts to a single host"),
    license="MIT",
    keywords="thumbor loader hostname",
    url="https://github.com/ekapratama93/thumbor-custom-loader",
    packages=find_packages(include=[
        'thumbor_custom_loader.loaders.single_loader',
    ]),
    long_description=long_description,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Multimedia :: Graphics :: Presentation",
    ],
    install_requires=[
        'thumbor>=7.0.0,<8.0.0',
    ]
)
