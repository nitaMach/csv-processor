from setuptools import setup, find_packages

setup(
    name="csv_processor",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'csv-processor=csv_processor.main:main'
        ],
    },
    extras_require={
        'test': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
        ],
    },
)
