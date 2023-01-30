import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outages-scaffold",
    version="0.0.2",
    author="Marco Lussetti and the Outages Project",
    author_email="packages@marcolussetti.com",
    description="Generate a standard Outages Project repository.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/outages/scaffold",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    scripts=["bin/outages-scaffold"],
    install_requires=[],
)
