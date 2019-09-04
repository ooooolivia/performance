'''
MVC App
'''
import sys
import os
from shared.runner import TestTraits, Runner


SCENARIONAME = 'MVC App Template'
EXENAME = 'mvcapptemplate'

if __name__ == "__main__":
    traits = TestTraits(scenarioname=SCENARIONAME,
                        exename=EXENAME,
                        startupmetric='PROCESSTIME',
                        guiapp='false',
                        )
    Runner(traits).run()