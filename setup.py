import setuptools
import re, io

with open("README.md", "r") as fh:
    long_description = fh.read()

# get version from package's __version__
__version__ = re.search(
        r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
        io.open('miney_toolbox/__init__.py', encoding='utf_8_sig').read()
    ).group(1)

setuptools.setup(
    name="miney_toolbox",
    version=__version__,
    author="Andreas Knüpfer",
    author_email="knue@posteo.de",
    description="Higher level functionalities for programming MineTest landscapes on top of Miney",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/knuedd/miney_toolbox",
    project_urls={
        "Documentation": "https://github.com/knuedd/miney_toolbox"
    },
    packages=["miney_toolbox"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment"
    ],
    python_requires='>=3.6',
)
