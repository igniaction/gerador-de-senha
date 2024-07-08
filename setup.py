# setup.py
# Direitos autorais © 2024 Richardson Almeida com auxílio do ChatGPT

from setuptools import setup, find_packages

setup(
    name='password_generator',
    version='0.1.0',
    description='A secure password generator system.',
    author='Richardson Almeida',
    author_email='igniaction@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    entry_points={
        'console_scripts': [
            'password_generator=password_generator.app:app.run',
        ],
    },
)
