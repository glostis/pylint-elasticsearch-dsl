import os
from codecs import open

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

package = "pylint_elasticsearch_dsl"

about = {}
with open(os.path.join(here, package, "__about__.py"), "r", "utf-8") as f:
    exec(f.read(), about)


def readme():
    with open(os.path.join(here, "README.md"), "r", "utf-8") as f:
        return f.read()


install_requires = ["astroid"]

extras_require = {
    "dev": ["bump2version", "pre-commit"],
    "test": ["pytest", "pylint", "elasticsearch-dsl"],
}

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme(),
    long_description_content_type="text/markdown",
    url=about["__url__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    packages=[package],
    install_requires=install_requires,
    extras_require=extras_require,
)
