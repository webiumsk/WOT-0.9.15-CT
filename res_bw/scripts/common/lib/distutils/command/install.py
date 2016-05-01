# 2016.05.01 15:29:29 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/distutils/command/install.py
"""distutils.command.install

Implements the Distutils 'install' command."""
from distutils import log
__revision__ = '$Id$'
import sys, os, string
from types import *
from distutils.core import Command
from distutils.debug import DEBUG
from distutils.sysconfig import get_config_vars
from distutils.errors import DistutilsPlatformError
from distutils.file_util import write_file
from distutils.util import convert_path, subst_vars, change_root
from distutils.util import get_platform
from distutils.errors import DistutilsOptionError
from site import USER_BASE
from site import USER_SITE
if sys.version < '2.2':
    WINDOWS_SCHEME = {'purelib': '$base',
     'platlib': '$base',
     'headers': '$base/Include/$dist_name',
     'scripts': '$base/Scripts',
     'data': '$base'}
else:
    WINDOWS_SCHEME = {'purelib': '$base/Lib/site-packages',
     'platlib': '$base/Lib/site-packages',
     'headers': '$base/Include/$dist_name',
     'scripts': '$base/Scripts',
     'data': '$base'}
INSTALL_SCHEMES = {'unix_prefix': {'purelib': '$base/lib/python$py_version_short/site-packages',
                 'platlib': '$platbase/lib/python$py_version_short/site-packages',
                 'headers': '$base/include/python$py_version_short/$dist_name',
                 'scripts': '$base/bin',
                 'data': '$base'},
 'unix_home': {'purelib': '$base/lib/python',
               'platlib': '$base/lib/python',
               'headers': '$base/include/python/$dist_name',
               'scripts': '$base/bin',
               'data': '$base'},
 'unix_user': {'purelib': '$usersite',
               'platlib': '$usersite',
               'headers': '$userbase/include/python$py_version_short/$dist_name',
               'scripts': '$userbase/bin',
               'data': '$userbase'},
 'nt': WINDOWS_SCHEME,
 'nt_user': {'purelib': '$usersite',
             'platlib': '$usersite',
             'headers': '$userbase/Python$py_version_nodot/Include/$dist_name',
             'scripts': '$userbase/Scripts',
             'data': '$userbase'},
 'os2': {'purelib': '$base/Lib/site-packages',
         'platlib': '$base/Lib/site-packages',
         'headers': '$base/Include/$dist_name',
         'scripts': '$base/Scripts',
         'data': '$base'},
 'os2_home': {'purelib': '$usersite',
              'platlib': '$usersite',
              'headers': '$userbase/include/python$py_version_short/$dist_name',
              'scripts': '$userbase/bin',
              'data': '$userbase'}}
SCHEME_KEYS = ('purelib', 'platlib', 'headers', 'scripts', 'data')

class install(Command):
    description = 'install everything from build directory'
    user_options = [('prefix=', None, 'installation prefix'),
     ('exec-prefix=', None, '(Unix only) prefix for platform-specific files'),
     ('home=', None, '(Unix only) home directory to install under'),
     ('user', None, "install in user site-package '%s'" % USER_SITE),
     ('install-base=', None, 'base installation directory (instead of --prefix or --home)'),
     ('install-platbase=', None, 'base installation directory for platform-specific files ' + '(instead of --exec-prefix or --home)'),
     ('root=', None, 'install everything relative to this alternate root directory'),
     ('install-purelib=', None, 'installation directory for pure Python module distributions'),
     ('install-platlib=', None, 'installation directory for non-pure module distributions'),
     ('install-lib=', None, 'installation directory for all module distributions ' + '(overrides --install-purelib and --install-platlib)'),
     ('install-headers=', None, 'installation directory for C/C++ headers'),
     ('install-scripts=', None, 'installation directory for Python scripts'),
     ('install-data=', None, 'installation directory for data files'),
     ('compile', 'c', 'compile .py to .pyc [default]'),
     ('no-compile', None, "don't compile .py files"),
     ('optimize=', 'O', 'also compile with optimization: -O1 for "python -O", -O2 for "python -OO", and -O0 to disable [default: -O0]'),
     ('force', 'f', 'force installation (overwrite any existing files)'),
     ('skip-build', None, 'skip rebuilding everything (for testing/debugging)'),
     ('record=', None, 'filename in which to record list of installed files')]
    boolean_options = ['compile',
     'force',
     'skip-build',
     'user']
    negative_opt = {'no-compile': 'compile'}

    def initialize_options(self):
        self.prefix = None
        self.exec_prefix = None
        self.home = None
        self.user = 0
        self.install_base = None
        self.install_platbase = None
        self.root = None
        self.install_purelib = None
        self.install_platlib = None
        self.install_headers = None
        self.install_lib = None
        self.install_scripts = None
        self.install_data = None
        self.install_userbase = USER_BASE
        self.install_usersite = USER_SITE
        self.compile = None
        self.optimize = None
        self.extra_path = None
        self.install_path_file = 1
        self.force = 0
        self.skip_build = 0
        self.warn_dir = 1
        self.build_base = None
        self.build_lib = None
        self.record = None
        return

    def finalize_options(self):
        if (self.prefix or self.exec_prefix or self.home) and (self.install_base or self.install_platbase):
            raise DistutilsOptionError, 'must supply either prefix/exec-prefix/home or ' + 'install-base/install-platbase -- not both'
        if self.home and (self.prefix or self.exec_prefix):
            raise DistutilsOptionError, 'must supply either home or prefix/exec-prefix -- not both'
        if self.user and (self.prefix or self.exec_prefix or self.home or self.install_base or self.install_platbase):
            raise DistutilsOptionError("can't combine user with prefix, exec_prefix/home, or install_(plat)base")
        if os.name != 'posix':
            if self.exec_prefix:
                self.warn('exec-prefix option ignored on this platform')
                self.exec_prefix = None
        self.dump_dirs('pre-finalize_{unix,other}')
        if os.name == 'posix':
            self.finalize_unix()
        else:
            self.finalize_other()
        self.dump_dirs('post-finalize_{unix,other}()')
        py_version = string.split(sys.version)[0]
        prefix, exec_prefix = get_config_vars('prefix', 'exec_prefix')
        self.config_vars = {'dist_name': self.distribution.get_name(),
         'dist_version': self.distribution.get_version(),
         'dist_fullname': self.distribution.get_fullname(),
         'py_version': py_version,
         'py_version_short': py_version[0:3],
         'py_version_nodot': py_version[0] + py_version[2],
         'sys_prefix': prefix,
         'prefix': prefix,
         'sys_exec_prefix': exec_prefix,
         'exec_prefix': exec_prefix,
         'userbase': self.install_userbase,
         'usersite': self.install_usersite}
        self.expand_basedirs()
        self.dump_dirs('post-expand_basedirs()')
        self.config_vars['base'] = self.install_base
        self.config_vars['platbase'] = self.install_platbase
        if DEBUG:
            from pprint import pprint
            print 'config vars:'
            pprint(self.config_vars)
        self.expand_dirs()
        self.dump_dirs('post-expand_dirs()')
        if self.user:
            self.create_home_path()
        if self.install_lib is None:
            if self.distribution.ext_modules:
                self.install_lib = self.install_platlib
            else:
                self.install_lib = self.install_purelib
        self.convert_paths('lib', 'purelib', 'platlib', 'scripts', 'data', 'headers', 'userbase', 'usersite')
        self.handle_extra_path()
        self.install_libbase = self.install_lib
        self.install_lib = os.path.join(self.install_lib, self.extra_dirs)
        if self.root is not None:
            self.change_roots('libbase', 'lib', 'purelib', 'platlib', 'scripts', 'data', 'headers')
        self.dump_dirs('after prepending root')
        self.set_undefined_options('build', ('build_base', 'build_base'), ('build_lib', 'build_lib'))
        return

    def dump_dirs(self, msg):
        if DEBUG:
            from distutils.fancy_getopt import longopt_xlate
            print msg + ':'
            for opt in self.user_options:
                opt_name = opt[0]
                if opt_name[-1] == '=':
                    opt_name = opt_name[0:-1]
                if opt_name in self.negative_opt:
                    opt_name = string.translate(self.negative_opt[opt_name], longopt_xlate)
                    val = not getattr(self, opt_name)
                else:
                    opt_name = string.translate(opt_name, longopt_xlate)
                    val = getattr(self, opt_name)
                print '  %s: %s' % (opt_name, val)

    def finalize_unix(self):
        if self.install_base is not None or self.install_platbase is not None:
            if self.install_lib is None and self.install_purelib is None and self.install_platlib is None or self.install_headers is None or self.install_scripts is None or self.install_data is None:
                raise DistutilsOptionError, 'install-base or install-platbase supplied, but installation scheme is incomplete'
            return
        else:
            if self.user:
                if self.install_userbase is None:
                    raise DistutilsPlatformError('User base directory is not specified')
                self.install_base = self.install_platbase = self.install_userbase
                self.select_scheme('unix_user')
            elif self.home is not None:
                self.install_base = self.install_platbase = self.home
                self.select_scheme('unix_home')
            else:
                if self.prefix is None:
                    if self.exec_prefix is not None:
                        raise DistutilsOptionError, 'must not supply exec-prefix without prefix'
                    self.prefix = os.path.normpath(sys.prefix)
                    self.exec_prefix = os.path.normpath(sys.exec_prefix)
                elif self.exec_prefix is None:
                    self.exec_prefix = self.prefix
                self.install_base = self.prefix
                self.install_platbase = self.exec_prefix
                self.select_scheme('unix_prefix')
            return

    def finalize_other(self):
        if self.user:
            if self.install_userbase is None:
                raise DistutilsPlatformError('User base directory is not specified')
            self.install_base = self.install_platbase = self.install_userbase
            self.select_scheme(os.name + '_user')
        elif self.home is not None:
            self.install_base = self.install_platbase = self.home
            self.select_scheme('unix_home')
        else:
            if self.prefix is None:
                self.prefix = os.path.normpath(sys.prefix)
            self.install_base = self.install_platbase = self.prefix
            try:
                self.select_scheme(os.name)
            except KeyError:
                raise DistutilsPlatformError, "I don't know how to install stuff on '%s'" % os.name

        return

    def select_scheme(self, name):
        scheme = INSTALL_SCHEMES[name]
        for key in SCHEME_KEYS:
            attrname = 'install_' + key
            if getattr(self, attrname) is None:
                setattr(self, attrname, scheme[key])

        return

    def _expand_attrs(self, attrs):
        for attr in attrs:
            val = getattr(self, attr)
            if val is not None:
                if os.name == 'posix' or os.name == 'nt':
                    val = os.path.expanduser(val)
                val = subst_vars(val, self.config_vars)
                setattr(self, attr, val)

        return

    def expand_basedirs(self):
        self._expand_attrs(['install_base', 'install_platbase', 'root'])

    def expand_dirs(self):
        self._expand_attrs(['install_purelib',
         'install_platlib',
         'install_lib',
         'install_headers',
         'install_scripts',
         'install_data'])

    def convert_paths(self, *names):
        for name in names:
            attr = 'install_' + name
            setattr(self, attr, convert_path(getattr(self, attr)))

    def handle_extra_path(self):
        if self.extra_path is None:
            self.extra_path = self.distribution.extra_path
        if self.extra_path is not None:
            if type(self.extra_path) is StringType:
                self.extra_path = string.split(self.extra_path, ',')
            if len(self.extra_path) == 1:
                path_file = extra_dirs = self.extra_path[0]
            elif len(self.extra_path) == 2:
                path_file, extra_dirs = self.extra_path
            else:
                raise DistutilsOptionError, "'extra_path' option must be a list, tuple, or comma-separated string with 1 or 2 elements"
            extra_dirs = convert_path(extra_dirs)
        else:
            path_file = None
            extra_dirs = ''
        self.path_file = path_file
        self.extra_dirs = extra_dirs
        return

    def change_roots(self, *names):
        for name in names:
            attr = 'install_' + name
            setattr(self, attr, change_root(self.root, getattr(self, attr)))

    def create_home_path(self):
        """Create directories under ~
        """
        if not self.user:
            return
        home = convert_path(os.path.expanduser('~'))
        for name, path in self.config_vars.iteritems():
            if path.startswith(home) and not os.path.isdir(path):
                self.debug_print("os.makedirs('%s', 0700)" % path)
                os.makedirs(path, 448)

    def run(self):
        if not self.skip_build:
            self.run_command('build')
            build_plat = self.distribution.get_command_obj('build').plat_name
            if self.warn_dir and build_plat != get_platform():
                raise DistutilsPlatformError("Can't install when cross-compiling")
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)

        if self.path_file:
            self.create_path_file()
        if self.record:
            outputs = self.get_outputs()
            if self.root:
                root_len = len(self.root)
                for counter in xrange(len(outputs)):
                    outputs[counter] = outputs[counter][root_len:]

            self.execute(write_file, (self.record, outputs), "writing list of installed files to '%s'" % self.record)
        sys_path = map(os.path.normpath, sys.path)
        sys_path = map(os.path.normcase, sys_path)
        install_lib = os.path.normcase(os.path.normpath(self.install_lib))
        if self.warn_dir and not (self.path_file and self.install_path_file) and install_lib not in sys_path:
            log.debug("modules installed to '%s', which is not in Python's module search path (sys.path) -- you'll have to change the search path yourself", self.install_lib)

    def create_path_file(self):
        filename = os.path.join(self.install_libbase, self.path_file + '.pth')
        if self.install_path_file:
            self.execute(write_file, (filename, [self.extra_dirs]), 'creating %s' % filename)
        else:
            self.warn("path file '%s' not created" % filename)

    def get_outputs(self):
        outputs = []
        for cmd_name in self.get_sub_commands():
            cmd = self.get_finalized_command(cmd_name)
            for filename in cmd.get_outputs():
                if filename not in outputs:
                    outputs.append(filename)

        if self.path_file and self.install_path_file:
            outputs.append(os.path.join(self.install_libbase, self.path_file + '.pth'))
        return outputs

    def get_inputs(self):
        inputs = []
        for cmd_name in self.get_sub_commands():
            cmd = self.get_finalized_command(cmd_name)
            inputs.extend(cmd.get_inputs())

        return inputs

    def has_lib(self):
        """Return true if the current distribution has any Python
        modules to install."""
        return self.distribution.has_pure_modules() or self.distribution.has_ext_modules()

    def has_headers(self):
        return self.distribution.has_headers()

    def has_scripts(self):
        return self.distribution.has_scripts()

    def has_data(self):
        return self.distribution.has_data_files()

    sub_commands = [('install_lib', has_lib),
     ('install_headers', has_headers),
     ('install_scripts', has_scripts),
     ('install_data', has_data),
     ('install_egg_info', lambda self: True)]
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\distutils\command\install.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.05.01 15:29:29 St�edn� Evropa (letn� �as)
