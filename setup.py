from setuptools import setup, find_packages
import sys, os


version = '0.1'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
]


setup(name='pydap.responses.citation',
    version=version,
    description='Citation response for Pydap',
    long_description="""This response allows Pydap to serve data citations""",
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='citation opendap dods dap data science climate oceanography',    
    author='Niklas Griessbaum',
    author_email='griessbaum@ucsb.edu',
    url='https://github.com/NiklasPhabian/pydap.responses.citation',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages = ['pydap', 'pydap.responses'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points="""
        [pydap.responses]
        #citation = pydap.responses.citation:CitationResponse
    """,
)
