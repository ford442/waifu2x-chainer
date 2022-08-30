import os
from distutils.extension import Extension;
import pkg_resources
from setuptools import setup, find_packages
extensions = [Extension('waifu',['waifu2x.py'])];
from Cython.Build import cythonize

setup(
    name="waifu",
    py_modules=["waifu"],
    version="1.0",
    description="Image Super-Resolution for Anime-Style Art",
    author="nagadomi",
    include_package_data=True,
    extras_require={'dev': ['pytest']},
    ext_modules = cythonize(extensions,nthreads=4,compiler_directives={'infer_types':True}),
)
