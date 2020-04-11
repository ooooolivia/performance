'''
C# Console app
'''
from shared.runner import TestTraits, Runner

SCENARIONAME = 'Empty C# Console Template'
EXENAME = 'emptycsconsoletemplate'

if __name__ == "__main__":
<<<<<<< Updated upstream
    traits = TestTraits(exename=EXENAME, 
                        #startupmetric='TimeToMain',
                        startup=True,
                        sdk=True,
                        guiapp='false',
                        )
=======
    traits = TestTraits(EXENAME)
    traits.add_traits(startupmetric='TimeToMain',
                      startup=True,
                      sdk=True,
                      guiapp='false',
                      processwillexit='true',
                      iterations='3'
                     )
>>>>>>> Stashed changes
    Runner(traits).run()
