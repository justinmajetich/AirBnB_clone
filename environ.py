#!/usr/bin/python3
'''An abstration for enviromental variables to enable .env files'''

import os


class Environ:
    '''An abstration over environment'''

    environ = {}

    def __init__(self, filename) -> None:
        '''initializes the environment and read ``.env`` file'''

        if os.path.exists(filename):
            with open('.env', 'r') as env:
                for line in env.readlines():
                    line = line.strip(' \n')
                    if not '=' in line:
                        continue
                    k, v = line.split('=', maxsplit=1)
                    self.environ[k] = v

    def get(self, k: str) -> str:
        '''returns an environmental variable'''
        return os.environ.get(k, default=self.environ.get(k, None))

def get_env(k: str, filename='.env') -> str:
    '''returns an environmental variable'''
    return Environ(filename).get(k)
