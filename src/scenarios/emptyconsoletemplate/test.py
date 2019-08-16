'''
pre-command
'''
import sys
import os
from shared.runner import TestTraits, Runner


exe_extension = ''
if sys.platform == 'win32':
    exe_extension = '.exe'

traits = TestTraits(scenarioname='C# Console Template', 
                    logname='emptycsconsoletemplate', 
                    appbin=os.path.join('build', 'build%s' % exe_extension),
                    apppublish=os.path.join('publish', 'build%s' % exe_extension),
                    framework='netcoreapp3.0',
                    startupmetric='TimeToMain',
                    guiapp='false', # string passed through to tool
                    startup=True)
runner = Runner(traits)
runner.run()