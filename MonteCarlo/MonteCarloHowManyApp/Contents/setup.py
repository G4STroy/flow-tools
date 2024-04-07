from setuptools import setup

setup(
    name='MCHowManyApp',
    version='1.0',
    py_modules=['MonteCarloApp'],
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'openpyxl',
        'Pillow'
    ],
    entry_points={
        'console_scripts': [
            'MCHowManyApp=MonteCarloApp:main',
        ],
    },
    package_data={
        'MonteCarloApp': ['Resources/*.jpeg', 'Resources/*.xlsx', 'Resources/*.docx']
    },
)
