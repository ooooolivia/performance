'''
pre-command
'''

import paths
# from performance.common import *
from dotnet import CSharpProject, CSharpProjFile
# from logging import getLogger
import sys

project = CSharpProject.new(template='console',
                            output_dir='build',
                            working_directory=sys.path[0],
                            force=True,
                            verbose=True)

project.publish('Release',
                'publish',
                True,
                [])
