from setuptools import setup

setup(name='instagram-python-lib',
      version='0.1',
      description='API wrapper for Instagram written in Python',
      url='https://github.com/GearPlug/instagram-python',
      author='Miguel Ferrer',
      author_email='ingferrermiguel@gmail.com',
      license='GPL',
      packages=['instagram'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
