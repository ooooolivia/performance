import os
from shared.runner import TestTraits, Runner
from shared import const

SCENARIO_NAME = 'WPF Large'
EXE_NAME = 'wpflarge'

def main():
    traits = TestTraits(scenarioname=SCENARIO_NAME,
                        exename=EXE_NAME,
                        guiapp='false', 
                        sdk=True,
                        )
    runner = Runner(traits)
    runner.run()


if __name__ == "__main__":
    main()
