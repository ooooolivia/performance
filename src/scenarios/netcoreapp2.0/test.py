import os
from shared.runner import TestTraits, Runner
from shared import const

SCENARIONAME = '.NET Core 2.0 Console Template'
EXENAME = 'NetCoreApp'

def main():
    traits = TestTraits(scenarioname=SCENARIONAME,
                        exename=EXENAME,
                        guiapp='false', 
                        sdk=True,
                        )
    runner = Runner(traits)
    runner.run()


if __name__ == "__main__":
    main()
