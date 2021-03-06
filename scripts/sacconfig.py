import os
import ConfigParser

mu0 = 1.25663706e-6

class SACConfig(object):

    def __init__(self, cfg_file=os.path.dirname(__file__) + '/sac_config.cfg'):
        self.cfg_file = cfg_file

        self.cfg = ConfigParser.SafeConfigParser()
        self.cfg.read(self.cfg_file)

    def _get_value(self, section, option):
        value = self.cfg.get(section, option)
        return value

    def _set_value(self, section, option, value):
        self.cfg.set(section, option, str(value))

    def _to_str(self, value):
        return str(value).replace('.','-')

#==============================================================================
#   SAC Configs
#==============================================================================
    @property
    def compiler(self):
        self._compiler = self._get_value('SAC', 'compiler')
        return self._compiler

    @compiler.setter
    def compiler(self, value):
        self._set_value('SAC', 'compiler', value)

    @property
    def compiler_flags(self):
        return self._get_value('SAC', 'compiler_flags')

    @compiler_flags.setter
    def compiler_flags(self, value):
        self._set_value('SAC', 'compiler_flags', value)

    @property
    def vac_modules(self):
        vm = self._get_value('SAC', 'vac_modules')
        return [x.strip() for x in vm.split(',')]

    @vac_modules.setter
    def vac_modules(self, value):
        self._set_value('SAC', 'vac_modules', value)

    @property
    def runtime(self):
        self._runtime = self._get_value('SAC', 'runtime')
        return self._runtime

    @runtime.setter
    def runtime(self, value):
        self._set_value('SAC', 'runtime', value)

    @property
    def grid_size(self):
        self._grid_size = self._get_value('SAC', 'grid_size')
        return self._grid_size

    @grid_size.setter
    def grid_size(self, value):
        self._set_value('SAC', 'grid_size', value)

    @property
    def mpi_config(self):
        self._mpi_config = self._get_value('SAC', 'mpi_config')
        return self._mpi_config

    @property
    def usr_script(self):
        return self._get_value('SAC', 'usr_script')

    @usr_script.setter
    def usr_script(self, value):
        self._set_value('SAC', 'usr_script', value)

    @mpi_config.setter
    def mpi_config(self, value):
        self._set_value('SAC', 'mpi_config', value)

    @property
    def mpi_size(self):
        r1 = int(self.mpi_config[2:4])
        r2 = int(self.mpi_config[4:6])
        r3 = int(self.mpi_config[6:8])
        return r1*r2*r3

    @property
    def varnames(self):
        self._varnames = self._get_value('SAC', 'varnames').split(' ')
        return self._varnames

    @varnames.setter
    def varnames(self, value):
        if isinstance(str, value):
            self._varnames = value.split(' ')
        elif isinstance(list, value):
            self._varnames = value
        else:
            raise TypeError("Unknown input")

        self._set_value('SAC', 'varnames', self._varnames)

#==============================================================================
#   Driver configs
#==============================================================================
    @property
    def period(self):
        self._period = float(self._get_value('driver', 'period'))
        return self._period

    @period.setter
    def period(self, value):
        self._period = float(value)
        self._set_value('driver', 'period', str(self._period))

    @property
    def str_period(self):
        period = 'p' + str(self.period).replace('.', '-')
        return period

    @property
    def exp_fac(self):
        self._exp_fac = float(self._get_value('driver', 'exp_fac'))
        return self._exp_fac

    @exp_fac.setter
    def exp_fac(self, value):
        self._exp_fac = float(value)
        self._set_value('driver', 'exp_fac', self._exp_fac)

    @property
    def str_exp_fac(self):
        exp_fac = 'B' + str(self.exp_fac).replace('.', '')
        return exp_fac

    @property
    def amp(self):
        self._amp = self._get_value('driver', 'amplitude')
        return self._amp

    @amp.setter
    def amp(self, value):
        self._set_value('driver', 'amplitude', value)

    @property
    def fort_amp(self):
        self._fort_amp = self._get_value('driver', 'fort_amp')
        return self._fort_amp

    @fort_amp.setter
    def fort_amp(self, value):
        self._set_value('driver', 'fort_amp', value)

    @property
    def delta_x(self):
        self._delta_x = self._get_value('driver', 'delta_x')
        return self._delta_x

    @delta_x.setter
    def delta_x(self, value):
        self._set_value('driver', 'delta_x', value)

    @property
    def delta_y(self):
        self._delta_y = self._get_value('driver', 'delta_y')
        return self._delta_y

    @delta_y.setter
    def delta_y(self, value):
        self._set_value('driver', 'delta_y', value)

    @property
    def delta_z(self):
        self._delta_z = self._get_value('driver', 'delta_z')
        return self._delta_z

    @delta_z.setter
    def delta_z(self, value):
        self._set_value('driver', 'delta_z', value)

    @property
    def identifier(self):
        self._identifier = self._get_value('driver', 'identifier').split(',')
        self._identifier = [r.strip() for r in self._identifier]
        return self._identifier

    @identifier.setter
    def identifier(self, value):
        if isinstance(value, str):
            self._identifier = value
        elif isinstance(value, list):
            self._identifier = ', '.join(value)
        else:
            raise TypeError("Unknown input")

        self._set_value('driver', 'identifier', self._identifier)

#==============================================================================
#   Analysis Configs
#==============================================================================
    @property
    def tube_radii(self):
        self._radii = self._get_value('analysis', 'tube_radii').split(',')
        self._radii = [r.strip() for r in self._radii]
        return self._radii

    @tube_radii.setter
    def tube_radii(self, value):
        if isinstance(value, str):
            self._radii = value
        elif isinstance(value, list):
            self._radii = ', '.join(value)
        else:
            raise TypeError("Unknown input")

        self._set_value('analysis', 'tube_radii', self._radii)

#==============================================================================
#   data configs
#==============================================================================
    @property
    def out_dir(self):
        self._out_dir = os.path.realpath(self._get_value('data', 'out_dir'))
        return self._out_dir

    @out_dir.setter
    def out_dir(self, value):
        self._out_dir = self._set_value('data', 'out_dir', value)
        return self._out_dir

    @property
    def data_dir(self):
        data_dir = os.path.realpath(self._get_value('data', 'data_dir'))
        return os.path.join(data_dir, self.get_identifier())

    @data_dir.setter
    def data_dir(self, value):
        self._set_value('data', 'data_dir', value)

    @property
    def gdf_dir(self):
        gdf_dir = os.path.realpath(self._get_value('data', 'gdf_dir'))
        return os.path.join(gdf_dir, self.get_identifier())

    @gdf_dir.setter
    def gdf_dir(self, value):
        self._set_value('data', 'gdf_dir', value)

    @property
    def fig_dir(self):
        return os.path.realpath(self._get_value('data', 'fig_dir'))

    @fig_dir.setter
    def fig_dir(self, value):
        self._set_value('data', 'fig_dir', value)

    @property
    def ini_dir(self):
        return os.path.realpath(self._get_value('data', 'ini_dir'))

    @ini_dir.setter
    def ini_dir(self, value):
        self._set_value('data', 'ini_dir', value)

    @property
    def ini_filename(self):
        return self._get_value('data', 'ini_filename')

    @ini_filename.setter
    def ini_filename(self, value):
        self._set_value('data', 'ini_filename', value)

#==============================================================================
#   Utils
#==============================================================================
    def get_identifier(self):
        id = ""
        for tag in self.identifier:
            x = getattr(self, tag)
            id += "{0}_".format(self._to_str(x))
        return id[:-1]  # Last _ is not wanted

    def save_cfg(self):
        with open(self.cfg_file, 'wb') as configfile:
            self.cfg.write(configfile)

    def print_config(self, section='all'):
        SAC = driver = analysis = data = False
        if section == 'all':
            SAC = True
            driver = True
            analysis = True
            data = True
        elif section == 'SAC':
            SAC = True
        elif section == 'driver':
            driver = True
        elif section == 'analysis':
            analysis = True
        elif section == 'data':
            data = True
        else:
            raise ValueError("Invalid section id")

        print "Current Config is:"
        if SAC:
            print "-"*79
            print "SAC:"
            print "-"*79
            print "compiler:", self.compiler
            print "compiler_flags:", self.compiler_flags
            print "vacmodules:", self.vac_modules
            print "usr_script:", self.usr_script
            print "runtime:", self.runtime
            print "mpi_config:", self.mpi_config
            print "grid_size:", self.grid_size
            print "varnames:", self.varnames
        if driver:
            print "-"*79
            print "Driver:"
            print "-"*79
            print "period:", self.period
            print "exp_fac:", self.exp_fac
            print "amp:", self.amp
            print "fort_amp:", self.fort_amp
            print "delta_x:", self.delta_x, "Mm"
            print "delta_y:", self.delta_y, "Mm"
            print "delta_z:", self.delta_z, "Mm"
            print "identifier:", self.identifier
        if analysis:
            print "-"*79
            print "analysis:"
            print "-"*79
            print "tube_radii:", self.tube_radii
        if data:
            print "-"*79
            print "data:"
            print "-"*79
            print "ini_dir:", self.ini_dir
            print "ini_filename:", self.ini_filename
            print "out_dir:", self.out_dir
            print "data_dir:", self.data_dir
            print "gdf_dir:", self.gdf_dir
            print "fig_dir:", self.fig_dir
