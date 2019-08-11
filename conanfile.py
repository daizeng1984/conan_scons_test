from conans import ConanFile, tools
import os


class SconsConan(ConanFile):
    name = 'Main'
    version = '1.0'
    license = 'MIT'
    settings = 'os', 'compiler', 'build_type', 'arch'
    requires = [
        "Poco/1.9.2@pocoproject/stable",
        "glfw/3.3@bincrafters/stable",
        "glad/0.1.29@bincrafters/stable",
        "Assimp/4.1.0@jacmoe/stable",
        "CLI11/1.8.0@cliutils/stable",
        "glm/0.9.9.4@g-truc/stable"
    ]
    description = 'Awesome Project'
    exports_sources = "src/*"
    generators = "scons"

    def build(self):
        debug_opt = '--debug-build' if self.settings.build_type == 'Debug' else ''
        # FIXME: Compiler, version, arch are hardcoded, not parametrized
        with tools.chdir("."):
            self.run('scons -C "{}/src" {}'.format(self.source_folder, debug_opt))
