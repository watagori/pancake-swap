from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


setup(
    name="pancakeswap",
    version="0.1.0",
    description="Create caaj from PancakeSwap",
    author="watagori",
    url="https://github.com/watagori/pancake-swap",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"]
)
