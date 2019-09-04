'''
pre-command
'''
import sys
from performance.logger import setup_loggers
from shared import const
from shared.precommands import PreCommands
from test import EXENAME

setup_loggers(True)
precommands = PreCommands()
precommands.new(template='mvc',
                output_dir=const.APPDIR,
                bin_dir=const.BINDIR,
                exename=EXENAME,   # not needed if there's just 'dotnet new'
                working_directory=sys.path[0])
precommands.backup(const.APPDIR)
