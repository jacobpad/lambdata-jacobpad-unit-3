

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # Replace with your own (repo name) username
    name="lambdata-jacobpad-unit-3",
    version="0.0.2",
    author="Jacob Padgett",
    author_email="jacobpad@gmail.com",
    description="Unit 3 Sprint 1 Module 1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jacobpad/lambdata-jacobpad-unit-3",
    packages=setuptools.find_packages(),  # or maybe it's just `find_packages()`
)
