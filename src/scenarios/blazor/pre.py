'''
pre-command
'''
import sys, os
from performance.logger import setup_loggers
from shared import const
from shared.precommands import PreCommands
from test import EXENAME

setup_loggers(True)
precommands = PreCommands()
precommands.new(template='blazorwasm',
                output_dir=const.APPDIR,
                bin_dir=const.BINDIR,
                exename=EXENAME,
                working_directory=sys.path[0])
# For blazor3.2 the linker argument '--dump-dependencies' should be added statically to enable linker dump
# For blazor5.0 the linker argument can be added to the command line as an msbuild property
precommands.add_static_msbuild_property(projectfile=os.path.join(const.APPDIR, f'{EXENAME}.csproj'), 
                                        propertyname='AdditionalMonoLinkerOptions', 
                                        propertyvalue=r'$(AdditionalMonoLinkerOptions) --dump-dependencies')
precommands.execute()
