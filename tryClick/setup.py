from setuptools import setup

setup(
    name="myClick",
    version='0.1',
    py_modules=['testClick'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        myClick=testClick:cli
    ''',
)