from pathlib import Path
import re
from setuptools import setup

here = Path(__file__).parent


def find_version(path):
    content = path.read_text(encoding="utf-8")
    match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", content, re.M)
    if match:
        return match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="faat.pikapool",
    version=find_version(here / "faat/pikapool/__init__.py"),
    description="Pools for pikas.",
    long_description=(here / "README.md").read_text("utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/faatca/faat.pikapool",
    author="Aaron Milner",
    author_email="aaron.milner@gmail.com",
    license="BSD",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: BSD License',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["faat.pikapool"],
    install_requires=["pika>=1.1.0"],
    python_requires=">=3.8",
)
