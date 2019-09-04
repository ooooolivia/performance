'''
MVC App
'''
import os
from shared.runner import TestTraits, Runner
from shared import const

SCENARIO_NAME = 'MVC App Template'
DIRECTORY_NAME = 'mvcapptemplate'
EXENAME = DIRECTORY_NAME
PROJECT_FILE = os.path.join(const.APPDIR, DIRECTORY_NAME+'.csproj')

if __name__ == "__main__":
    traits = TestTraits(scenarioname=SCENARIO_NAME,
                        exename=const.DOTNET,
                        appargs="build %s" % PROJECT_FILE,
                        startupmetric='ProcessTime',
                        guiapp='false',
                        iterations='1',
                        sdk=True,
                        startup=True
                        )
    runner = Runner(traits)
    runner.parseargs()
    runner.run()
