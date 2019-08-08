'''
Wrapper around startup tool.
'''
import sys
import os

from performance.logger import setup_loggers
from performance.common import get_artifacts_directory, get_packages_directory
from dotnet import CSharpProject, CSharpProjFile
from logging import getLogger
from util import helixpayload
class StartupWrapper(object):
    '''
    '''
    def __init__(self):
        payload = helixpayload()
        if payload:
            pass
            # run from payload
        else:
            startupProj = os.path.join('..', 
                                       '..', 
                                       'tools', 
                                       'ScenarioMeasurement', 
                                       'Startup',
                                       'Startup.csproj')
            self.startup = CSharpProject(CSharpProjFile(startupProj, 
                                                        sys.path[0]),
                                                        os.path.join(os.path.dirname(startupProj),
                                         os.path.join(get_artifacts_directory(), 'startup')))
            self.startup.restore(get_packages_directory(), True)
            self.startup.build('Release', ['netcoreapp3.0'], True, get_packages_directory())

    def runtests(self, **kwargs):
        print(kwargs['logname'])
    
        for key in ['startupmetric', 'guiapp', 'apppublish']:
            if not kwargs[key]:
                raise Exception('startup tests require %s' % key)
        startup_args = [
            '--', '--app-exe', kwargs['apppublish'],
            '--metric-type', kwargs['startupmetric'], 
            '--scenario-name', kwargs['scenarioname'],
            '--trace-file-name', '%s_startup.etl' % kwargs['logname'],
            '--process-will-exit', 'true', # ???
            '--iterations', '5',
            '--timeout', '20',
            '--log-file-name', '%s_startup.log' % kwargs['logname'],
            '--warmup', 'true',
            '--gui-app', kwargs['guiapp'],
            '--working-dir', sys.path[0],
            '--report-json-path', '%s.json' % kwargs['logname']
        ]
        self.startup.run('Release', ['netcoreapp3.0'], True, *startup_args)