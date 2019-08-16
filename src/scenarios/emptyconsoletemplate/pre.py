'''
pre-command
'''
import sys
# from performance.common import *
from dotnet import CSharpProject
from performance.logger import setup_loggers

setup_loggers(True)

project = CSharpProject.new(template='console',
                            output_dir='build',
                            working_directory=sys.path[0],
                            force=True,
                            verbose=True)

project.publish('Release',
                'publish',
                True,
                [])
