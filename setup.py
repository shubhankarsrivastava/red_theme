from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in red_theme/__init__.py
from red_theme import __version__ as version

setup(
	name="red_theme",
	version=version,
	description="Custom Red Theme",
	author="Shubhankar Srivastava",
	author_email="shubhankarsrivastava005@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
