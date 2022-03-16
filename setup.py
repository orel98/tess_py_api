from setuptools import find_packages, setup

with open("./README.md") as f:
    long_description = f.read()

setup(
    name="tess_py_api",
    version="0.0.11",
    author="Orel Kalaf",
    author_email="orelron98@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/orel98/tess_py_api/tree/main",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)
