'''
Module for running scenario tasks
'''

from os import environ
from collections import namedtuple
from startup import StartupWrapper

reqfields = ('scenarioname',
             'logname',
             'appbin')
optfields = ('startup', 
             'sdk',
             'guiapp',
             'startupmetric',
             'appargs',
             'apppublish',
             'iterations',
             'timeout',
             )


TestTraits = namedtuple('TestTraits', reqfields + optfields, defaults=(None,) * len(optfields))

class Runner:
    '''
    Wrapper for running all the things
    '''
    
    def __init__(self, traits: TestTraits):
        self.traits = traits
    
    def run(self):
        '''
        Runs the specified scenario
        '''
        if self.traits.startup:
            print("startup")
            startup = StartupWrapper()
            startup.runtests(**self.traits._asdict())
