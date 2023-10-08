from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dev_doc_hub/__init__.py
from dev_doc_hub import __version__ as version

setup(
	name="dev_doc_hub",
	version=version,
	description="Development Documentation Hub for frappe",
	author="Mohamed Abdulsalam Alqadasi",
	author_email="moha2016it@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
