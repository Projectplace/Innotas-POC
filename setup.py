from setuptools import setup

setup(name='innotas-POC',
      description='innotas selenium POC',
      long_description='',
      author='Jim Brannlund',
      author_email='jbrannlund@planview.com',
      url='https://github.com/Projectplace/innotas-POC',
      packages=['test_automation', 'test_automation.page_objects', 'test_automation.tests'],
      install_requires=[
          'pytest>=2.7.3',
          'pytest-base-url',
          'pytest-html>=1.14.0',
          'pytest-variables>=1.5.0',
          'pytest-selenium',
          'selenium==3.3.3',
          'requests',
          'basepage',
          'assertpy'],
      license='Mozilla Public License 2.0 (MPL 2.0)',
      keywords='innotas selenium',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7'])
