import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='instagram-python-lib',
      version='0.1.2',
      description='API wrapper for Instagram written in Python',
      long_description=read('README.md'),
      url='https://github.com/GearPlug/instagram-python',
      author='Miguel Ferrer',
      author_email='ingferrermiguel@gmail.com',
      license='GPL',
      packages=['instagram'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
