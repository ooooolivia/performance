'''
C# Console app
'''
from shared.runner import TestTraits, Runner

SCENARIONAME = 'Empty C# Console Template'
EXENAME = 'emptycsconsoletemplate'

if __name__ == "__main__":
    traits = TestTraits(EXENAME) # required fields which should be initalized with the object
    traits.add_traits(startupmetric='TimeToMain',  # optional fields defined in test.py have higher priority that traits in runner.py
                      startup=True,
                      sdk=True,
                      guiapp='false',
                      processwillexit='true',
                      iterations='3'
                     )
    Runner(traits).run()
