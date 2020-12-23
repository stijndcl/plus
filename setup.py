import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pluspy",
    version="0.0.1",
    author="stijndcl",
    author_email="declercq.stijn@outlook.com",
    description="For all your addition needs, up to numbers of 250.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stijndcl/plus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)