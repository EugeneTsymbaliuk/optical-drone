from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Gnd app',
    ext_modules=cythonize("fly_by_ip_gnd.pyx"),
)
