'''
pre-command
'''
import sys
from dotnet import CSharpProject
from performance.logger import setup_loggers
from shared import const

setup_loggers(True)

CSharpProject.new(template='console',
                  output_dir=const.BINDIR,
                  working_directory=sys.path[0],
                  force=True,
                  verbose=True)