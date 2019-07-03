from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "VERSION"), encoding="utf-8") as f:
    VERSION = f.read().strip()

setup(author="Andrew Michaud",
      author_email="dev@drew.life",

      entry_points={
          "console_scripts": ["dirtyunix_bot = dirtyunix_bot.__main__:main"]
      },

      install_requires=["botskeleton>=3.3.4"],
      python_requires=">=3.6",

      license="BSD3",

      name="dirtyunix_bot",

      packages=find_packages(),

      url="https://github.com/alixnovosi/dirtyunix_bot",

      version=VERSION)
