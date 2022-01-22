from setuptools import setup

setup(
    name="ipxacttree",
    version="0.1",
    packages=["ipxacttree"],
    entry_points={"console_scripts": ["ipxacttree = ipxacttree.main:main",]},
)
