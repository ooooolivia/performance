'''
Wrapper around startup tool.
'''
import sys
import os

from performance.logger import setup_loggers
from performance.common import get_artifacts_directory, get_packages_directory, RunCommand
from dotnet import CSharpProject, CSharpProjFile
from shared.util import helixpayload, builtexe, publishedexe
from shared.const import *
class StartupWrapper(object):
    '''
    Wraps startup.exe, building it if necessary.
    '''
    def __init__(self):
        payload = helixpayload()
        if payload:
            self._setstartuppath(os.path.join('tools', 'startup', payload))
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
            self._setstartuppath(startup.bin_path)

    
    def _setstartuppath(self, path: str):
        self.startupexe = os.path.join(path, 'Startup.exe')

    def runtests(self, apptorun: str, **kwargs):
        '''
        Runs tests through startup
        '''
        for key in ['startupmetric', 'guiapp']:
            if not kwargs[key]:
                raise Exception('startup tests require %s' % key)

        startup_args = [
            self.startupexe,
            '--app-exe', apptorun,
            '--metric-type', kwargs['startupmetric'], 
            '--scenario-name', "%s - %s" % (kwargs['scenarioname'], kwargs['scenariotypename']),
            '--trace-file-name', '%s_startup.etl' % kwargs['exename'],
            '--process-will-exit', 'true', # ???
            '--iterations', '%s' % (kwargs['iterations'] or '5'),
            '--timeout', '%s' % (kwargs['timeout'] or '20'),
            '--log-file-name', '%s_startup.log' % kwargs['exename'],
            '--warmup', '%s' % (kwargs['warmup'] or 'true'),
            '--gui-app', kwargs['guiapp'],
            '--working-dir', sys.path[0],
            '--report-json-path', '%s.json' % kwargs['exename']
        ]
        RunCommand(startup_args, verbose=True).run()
