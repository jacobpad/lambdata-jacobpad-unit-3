

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-jacobpad-unit-3", # Replace with your own (repo name) username
    version="0.0.1",
    author="Jacob Padgett",
    author_email="jacobpad@gmail.com",
    description="Unit 3 Sprint 1 Module 1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jacobpad/lambdata-jacobpad-unit-3",
    packages=setuptools.find_packages(),  # or maybe it's just `find_packages()`
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
    # python_requires='>=3.6',
)
