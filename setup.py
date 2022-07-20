from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='cwmath',
    version='0.0.3',
    author='Cadwork',
    author_email='it@cadwork.ca',
    description='Cadwork Math Utilities',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cwapi3d/cwmath',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3.9, <4',
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    include_package_data=True,
)
