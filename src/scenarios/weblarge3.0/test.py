import os
from shared.runner import TestTraits, Runner
from shared import const

SCENARIONAME = 'Web Large 3.0'
EXENAME = 'weblarge30'

def main():
    traits = TestTraits(scenarioname=SCENARIONAME,
                        exename=EXENAME,
                        guiapp='false',
                        workingdir='mvc',
                        timeout= f'{const.MINUTE*30}',   # increase timeout for the large project
                        sdk=True,
                        )
    runner = Runner(traits)
    runner.run()


if __name__ == "__main__":
    main()
