'''
Wrapper around startup tool.
'''
import sys
import os

from performance.logger import setup_loggers
from performance.common import get_artifacts_directory, get_packages_directory, RunCommand
from dotnet import CSharpProject, CSharpProjFile
from shared.util import helixpayload
class StartupWrapper(object):
    '''
    Wraps startup.exe, building it if necessary.
    '''
    def __init__(self):
        payload = helixpayload()
        if payload:
            self.setstartuppath(payload)
        else:
            startupproj = os.path.join('..',
                                       '..',
                                       'tools',
                                       'ScenarioMeasurement',
                                       'Startup',
                                       'Startup.csproj')
            startup = CSharpProject(CSharpProjFile(startupproj,
                                                   sys.path[0]),
                                                   os.path.join(os.path.dirname(startupproj),
                                    os.path.join(get_artifacts_directory(), 'startup')))
            startup.restore(get_packages_directory(), True)
            startup.build('Release', ['netcoreapp3.0'], True, get_packages_directory())
            self.setstartuppath(startup.bin_path)

    
    def setstartuppath(self, path: str):
        self.startupexe = os.path.join(path, 'Startup.exe')

    def runtests(self, **kwargs):
        '''
        Runs tests through startup
        '''
        for key in ['startupmetric', 'guiapp', 'apppublish']:
            if not kwargs[key]:
                raise Exception('startup tests require %s' % key)

        startup_args = [
            self.startupexe,
            '--app-exe', kwargs['apppublish'],
            '--app-args', kwargs['appargs'],
            '--metric-type', kwargs['startupmetric'], 
            '--scenario-name', kwargs['scenarioname'],
            '--trace-file-name', '%s_startup.etl' % kwargs['logname'],
            '--process-will-exit', 'true', # ???
            '--iterations', '%s' % (kwargs['iterations'] or '5'),
            '--timeout', '%s' % (kwargs['timeout'] or '20'),
            '--log-file-name', '%s_startup.log' % kwargs['logname'],
            '--warmup', '%s' % (kwargs['warmup'] or 'true'),
            '--gui-app', kwargs['guiapp'],
            '--working-dir', sys.path[0],
            '--report-json-path', '%s.json' % kwargs['logname'],
        ]

        # optional arguments
        if kwargs['iterationsetup']:
            startup_args.extend(['--iteration-setup', kwargs['iterationsetup']])
        if kwargs['setupargs']:
            startup_args.extend(['--setup-args', kwargs['setupargs']])

        RunCommand(startup_args, verbose=True).run()
