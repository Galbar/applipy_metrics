from setuptools import setup, find_packages
from distutils.util import convert_path

ns = {}
ver_path = convert_path('applipy_metrics/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), ns)
version = ns['__version__']

setup(
    name="applipy_metrics",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
    ],
    description="Performance metrics, based on Coda Hale's Yammer metrics",
    license="Apache 2.0",
    author="Alessio Linares",
    author_email="mail@alessio.cc",
    version=version,
    packages=find_packages(exclude=['doc', 'tests']),
    data_files=[],
    python_requires='>=3.6',
    install_requires=[],
    scripts=[],
)
