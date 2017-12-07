from setuptools import setup

setup(
    name='hash_lha_slave',
    version='0.1',
    description='Testing setup.py and LHA module import',
    url='http://dummy.com',
    author='Oliver Ainger',
    author_email='oainger@gmail.com',
    license='BSD',
    packages=['slave_lha', 'slave_lha.parse_lha'],
    install_requires=['lhafile'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['hash_lha_slave=slave_lha.command_line:main'],
    },
    zip_safe=False)
