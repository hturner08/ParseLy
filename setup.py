from setuptools import setup, find_packages

setup(name='ParseLy',
      version='0.1',
      description='Generic Data Parser',
      long_description='Currently only supports meshtal files',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Data Processing',
      ],
      keywords='data, mesh',
      url='http://github.com/hturner08/Parsely',
      author='Hturner08',
      author_email='hmturner@mit.edu',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'markdown',
          'pandas',
          'setuptools',
          'numpy',
      ],
      include_package_data=True,
      zip_safe=False)
