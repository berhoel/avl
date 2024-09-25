#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Build AVL Cython project."""

import os

from Cython.Build import cythonize
from setuptools import Extension
from setuptools.command.build_ext import build_ext
from setuptools.dist import Distribution

__date__ = "2024/09/25 15:08:30 hoel"
__author__ = "Berthold Höllmann"
__copyright__ = "Copyright © 2021 by Berthold Höllmann"
__credits__ = ["Berthold Höllmann"]
__maintainer__ = "Berthold Höllmann"
__email__ = "berhoel@gmail.com"

# This function will be executed in setup.py:
def build(setup_kwargs):
    # gcc arguments hack: enable optimizations
    os.environ["CFLAGS"] = "-O3"

    # Build
    setup_kwargs.update(
        {
            "libraries": [("avl", {"sources": ["lib/src/avl.c"]})],
            "ext_modules": cythonize(
                [
                    Extension(
                        "avl.ext",
                        ["ext/src/avl_module.pyx"],
                        include_dirs=["lib/src"],
                        extra_compile_args=[
                            "-O3",
                            # "-g"
                        ],
                        # extra_link_args=["-g"],
                    )
                ],
                language_level=3,
                compiler_directives={
                    "embedsignature": True,
                    # "profile": True,
                    "c_string_type": "str",
                    "c_string_encoding": "utf-8",
                    "linetrace": True,
                },
                gdb_debug=True,
            ),
            "cmdclass": {"build_ext": build_ext},
        }
    )


# Local Variables:
# mode: python
# compile-command: "poetry run tox"
# time-stamp-pattern: "30/__date__ = \"%:y/%02m/%02d %02H:%02M:%02S %u\""
# End:
