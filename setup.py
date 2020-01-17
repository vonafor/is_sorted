from setuptools import setup

import is_sorted

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="is_sorted",
    version=is_sorted.__version__,
    author="Yan Mitrofanov",
    author_email="mmxlviii@mail.ru",
    description="tool to check sorting",
    long_description=long_description,
    url="https://github.com/vonafor/is_sorted",
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=["is_sorted"],
    python_requires=">=3.5",
    extras_require={
        "tests": ["pytest>=5.3.2"],
    },
)
