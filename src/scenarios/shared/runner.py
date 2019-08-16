'''
Module for running scenario tasks
'''

from collections import namedtuple
from shared.startup import StartupWrapper
from performance.logger import setup_loggers


reqfields = ('scenarioname',
             'logname',
             'appbin',
             'framework')
optfields = ('startup', 
             'sdk',
             'guiapp',
             'startupmetric',
             'appargs',
             'apppublish',
             'iterations',
             'timeout',
             'warmup'
             )


TestTraits = namedtuple('TestTraits', reqfields + optfields, defaults=(None,) * len(optfields))

class Runner:
    '''
    Wrapper for running all the things
    '''

    def __init__(self, traits: TestTraits):
        self.traits = traits
        setup_loggers(True)

    def run(self):
        '''
        Runs the specified scenario
        '''
        if self.traits.startup:
            print("startup")
            startup = StartupWrapper()
            startup.runtests(**self.traits._asdict())
