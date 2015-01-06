# Copyright (C) Sam Parkinson 2014
#
# This file is part of ASLO.
#
# ASLO is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ASLO is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with ASLO.  If not, see <http://www.gnu.org/licenses/>.

import os
from subprocess import call

def compile_bundle():
    call(['rm', '-rf', 'dl/dist'])

    # Common issue
    if not os.path.isdir('dl/po'):
        os.mkdir('dl/po')

    abs_path = os.path.join(os.getcwd(), 'dl')
    call(['docker', 'run', 
          '-v', abs_path + ':/activity', 'samdroid/activity-build'])
    
    if os.path.isdir('dl/dist/') and len(os.listdir('dl/dist/')) == 1:
        f = os.path.join('dl/dist', os.listdir('dl/dist/')[0])
        return open(f, 'rb')
    return None
