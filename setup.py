from setuptools import setup, find_packages

__name__ = "kagsa"
__version__ = "1.1.1"
__author__ = "Kagsa Programming Language"
__author_email__ = "kagsa.programming.lang@gmail.com"
__date__ = "2022-9-10"


readme = open("README.md", "r", encoding="utf-8")
long_description =  readme.read()
reqFile=open("requirements.txt", "r")
requirements = reqFile.read().split('\n')

readme.close()
reqFile.close()

setup(
    name=__name__,
    version=__version__,
    description='Programming Language',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://www.kagsa.org/',
    author=__author__,
    author_email=__author_email__,

    project_urls={
      'Source': 'https://github.com/kagsa/kagsa',
      'Report Bugs': 'https://github.com/kagsa/kagsa/issues',
      'Download': 'https://pypi.org/project/kagsa/#files',
      'Documentation': 'https://github.com/kagsa/kagsa/blob/master/README.md',
      'Website' : 'http://kagsa.org/'
    },

    license='MIT',

    keywords=[
        'programming', 'language', 'programming language',
        'kagsa', 'lang', 'kg', 'KG', 'KAGSA'
       ],

    packages=find_packages(),

    include_package_data=True,

    package_data={'' : ['built_modules.py','errors.py','methods.py','parse_id.py','parse_string.py','parser.py']},

    install_requires= requirements,

    entry_points={
        'console_scripts': [
                "kagsa=kagsasrc.__main__:main",
                "kg=kagsasrc.__main__:main"
        ]
	}
)