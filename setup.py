from setuptools import setup, find_packages

setup(
    name="MyProject",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["flask>=3.0.0"],
    python_requires=">=3.10",
)