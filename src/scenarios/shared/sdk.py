from collections import namedtuple
from performance.logger import setup_loggers
from shared.startup import StartupWrapper

fields = (
    'scenarioname',
    'apppublish',
    'appargs',
    'logname',
    'startupmetric',
    'iterations',
    'timeout',
    'warmup',
    'guiapp',
    'iterationsetup',
    'setupargs'
)

TestTraits = namedtuple('TestTraits', fields, defaults=(None,)*len(fields))


class SDKRunner(object):
    '''
    Module for running sdk tests
    '''

    def __init__(self, scenario_name: str, project_file: str):
        self.scenario_name = scenario_name
        self.project_file = project_file
        self.startup = StartupWrapper()
        setup_loggers(True)

    def build_clean(self, iterations=3, timeout=20):
        traits = TestTraits(
            scenarioname='%s (Clean)' % self.scenario_name,
            apppublish='dotnet.exe',
            appargs='build %s' % self.project_file,
            logname='%s_clean' % self.scenario_name.lower().replace(' ', '_'),
            startupmetric='ProcessTime', # could be a parameter
            iterations=str(iterations),
            timeout=str(timeout),
            warmup='false',
            guiapp='false',
            iterationsetup='dotnet.exe',
            setupargs='clean %s' % self.project_file
        )
        print("scenario: %s" % traits.scenarioname)
        self.startup.runtests(**traits._asdict())

    def build_no_changes(self, iterations=3, timeout=20):
        traits = TestTraits(
            scenarioname='%s (No Changes)' % self.scenario_name,
            apppublish='dotnet.exe',
            appargs='build %s' % self.project_file,
            logname='%s_no_changes' % self.scenario_name.lower().replace(' ', '_'),
            startupmetric='ProcessTime',
            iterations=str(iterations),
            timeout=str(timeout),
            warmup='true',
            guiapp='false'
        )
        print("scenario: %s" % traits.scenarioname)
        self.startup.runtests(**traits._asdict())

