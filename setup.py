from setuptools import setup, find_packages

setup(
    name="pyroject",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pyroject=pyroject.cli:main"
        ]
    },
    python_requires=">=3.7",
    description="A lightweight Python project manager inspired by npm",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/FowluhhDev/pyroject",
    author="Mason Fowler",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
