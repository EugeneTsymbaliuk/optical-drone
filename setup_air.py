from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Air app',
    ext_modules=cythonize("fly_by_ip_air.pyx"),
)
