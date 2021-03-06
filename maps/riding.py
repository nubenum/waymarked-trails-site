# This file is part of the Waymarked Trails Map Project
# Copyright (C) 2015 Sarah Hoffmann
#
# This is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
""" Configuration for the Horse riding map.
"""

from db.configs import *
from os.path import join as os_join
from config.defaults import MEDIA_ROOT

MAPTYPE = 'routes'

ROUTEDB = RouteDBConfig()
ROUTEDB.schema = 'riding'
ROUTEDB.relation_subset = """
    tags ? 'route' and tags->'type' IN ('route', 'superroute')
    AND 'horse' = any(regexp_split_to_array(tags->'route', ';'))
    AND NOT (tags ? 'state' AND tags->'state' = 'proposed')"""

ROUTES = RouteTableConfig()
ROUTES.network_map = { 'nhn': 10, 'rhn': 20, 'lhn': 30,
                       'nwn': 10, 'rwn': 20, 'lwn': 30, 'nwn:kct' : 10,
                       'ncn': 10, 'rcn': 20, 'lcn': 30,
                     }
ROUTES.symbols = ( 'OSMCSymbol',
                   'TextSymbol',
                   'ColorBox')

DEFSTYLE = RouteStyleTableConfig()

GUIDEPOSTS = GuidePostConfig()
GUIDEPOSTS.subtype = 'horse'
GUIDEPOSTS.require_subtype = True

NETWORKNODES = NetworkNodeConfig()
NETWORKNODES.node_tag = 'rhn_ref'

SYMBOLS = ShieldConfiguration()
SYMBOLS.symbol_outdir = os_join(MEDIA_ROOT, 'symbols/riding')
