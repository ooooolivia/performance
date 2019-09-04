'''
Commands and utilities for pre.py scripts
'''

import sys
from argparse import ArgumentParser
from dotnet import CSharpProject, CSharpProjFile
from shared import const
from performance.common import get_packages_directory
from shutil import copytree
import os

BUILD = 'build'
PUBLISH = 'publish'
RESTORE = 'restore'

OPERATIONS = (BUILD,
              RESTORE,
              PUBLISH)


class PreCommands:
    '''
    Handles building and publishing
    '''

    def __init__(self):
        self.project = None
        self.projectfile = None
        parser = ArgumentParser()
        parser.add_argument('operation', choices=OPERATIONS)
        parser.add_argument('-c', '--configuration', dest='configuration', choices=['Debug', 'Release'], required=True)
        args = parser.parse_args()
        self.configuration = args.configuration
        self.operation = args.operation

    def new(self, template: str, output_dir: str, bin_dir: str, exename: str, working_directory: str):
        'makes a new app with the given template'
        self.project = CSharpProject.new(template=template,
                                         output_dir=output_dir,
                                         bin_dir=bin_dir,
                                         exename=exename,
                                         working_directory=working_directory,
                                         force=True,
                                         verbose=True)
        return self

    def existing(self, projectfile: str):
        'create a project from existing project file'
        csproj = CSharpProjFile(projectfile, sys.path[0])
        self.project = CSharpProject(csproj, const.BINDIR)
        return self

    def execute(self):
        'Parses args and runs precommands'
        if self.operation == BUILD:
            self._restore()
            self._build(self.configuration)
        if self.operation == RESTORE:
            self._restore()
        if self.operation == PUBLISH:
            self._restore()
            self._publish(self.configuration)

    def backup(self, folder):
        'make a temp copy of the asset'
        copytree(folder, os.path.join(const.TMPDIR, folder))

    def _publish(self, configuration: str):
        self.project.publish(configuration=configuration,
                             output_dir=const.PUBDIR,
                             verbose=True,
                             packages_path=get_packages_directory()
                             )

    def _restore(self):
        self.project.restore(packages_path=get_packages_directory(), verbose=True)

    def _build(self, configuration: str):
        self.project.build(configuration=configuration,
                           verbose=True,
                           packages_path=get_packages_directory(),
                           target_framework_monikers=None)
