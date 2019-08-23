'''
pre-command
'''
import sys
import os
from shared.runner import TestTraits, Runner




traits = TestTraits(scenarioname='C# Console Template', 
                    logname='emptycsconsoletemplate', 
                    framework='netcoreapp3.0',
                    startupmetric='TimeToMain',
                    guiapp='false', # string passed through to tool
                    )
Runner(traits).run()
