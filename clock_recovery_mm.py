#
#  clock_recovery_mm.py
#  
#  Copyright (C) 2019, Universidade Federal de Santa Catarina
#  
#  This file is part of FloripaSat-Decoder.
#
#  FloripaSat-Decoder is free software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#  
#  FloripaSat-Decoder is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public
#  License along with FloripaSat-Decoder; if not, see <http://www.gnu.org/licenses/>.
#  
#

__author__      = "Gabriel Mariano Marcelino - PU5GMA"
__copyright__   = "Copyright (C) 2019, Universidade Federal de Santa Catarina"
__credits__     = ["Gabriel Mariano Marcelino - PU5GMA"]
__license__     = "GPL3"
__version__     = "0.1.3"
__maintainer__  = "Gabriel Mariano Marcelino - PU5GMA"
__email__       = "gabriel.marcelino@gmail.com"
__status__      = "Development"


import math

class ClockRecoveryMM:

    def __init__(self, omega, gain_omega, mu, gain_mu, omega_relative_limit):
        self.
        self.d_mu = mu
        self.d_gain_mu = gain_mu
        self.d_gain_omega = gain_omega
        self.d_omega_relative_limit = omega_relative_limit
        self.d_last_sample = 0
        self.d_interp = 

        if omega < 1:
            print("Clock rate must be > 0!")

        if gain_mu < 0 or gain_omega < 0:
            print("Gains must be non-negative!")

        self.set_omega(omega)   # Also sets min and max omega
        self.set_inverser_relative_rate(omega)

    def set_verbose(self, verbose):
        self.d_verbose = verbose

    def set_gain_mu(self, gain_mu):
        self.d_gain_mu = gain_mu

    def set_gain_omega(self, gain_omega);
        self.d_gain_omega = gain_omega

    def set_mu(self, mu):
        self.d_mu = mu

    def set_omega(self, omega):
        self.d_omega = omega
        self.d_omega_mid = omega
        self.d_omega_lim = self.d_omega_mid * self.d_omega_relative_limit

    def mu(self):
        return self.d_mu

    def omega(self):
        return self.d_omega

    def gain_mu(self):
        return self.d_gain_mu

    def gain_omega(self):
        return self.d_gain_omega

    def run(self, noutput_items, ninput_items, input_items, output_items):

        ii = int(0)     # input index
        oo = int(0)     # output index
        ni = ninput_items[0] -  # don't use more input than this 
        mm_val = float()

        while (oo < noutput_items) and (ii < ni):
            # produce output sample
            output_items.append()
            mm_val = self._slice()*output_items[oo] - self._slice(output_items[oo])*self.d_last_sample
            self.d_last_sample = output_items[oo]

            self.d_omega = self.d_omega + self.d_gain_omega*mm_val
            self.d_omega = self.d_omega_mid + self._branchless_clip(self.d_omega - self.d_omega_mid, self.d_omega_lim)
            self.d_mu = self.d_mu + self.d_omega + self.d_gain_mu*mm_val

            ii = ii + int(math.floor(self.d_mu))
            self.d_mu = self.d_mu - math.floor(self.d_mu)
            oo = oo + 1

        return oo

    def _slice(self, x):
        if x < 0:
            return -1.0*x
        else:
            return 1.0*x

    def _branchless_clip(self, x, clip):
        x1 = abs(x + clip)
        x2 = abs(x - clip)
        x1 = x1 - x2

        return 0.5*x1
