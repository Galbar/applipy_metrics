from setuptools import setup, find_packages
from applipy_metrics import Version

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
    version=Version.RELEASE,
    packages=['applipy_metrics'],
    data_files=[],
    python_requires='>=3.6',
    install_requires=[],
    scripts=[],
)
