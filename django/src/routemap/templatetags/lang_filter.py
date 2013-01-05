# This file is part of the Waymarked Trails Map Project
# Copyright (C) 2011-2012 Sarah Hoffmann
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

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def localeurl(context, lang_code):
    """Return the path of the current page localized in
       the given language.
    """
    url = context['request'].path
    curlocale = context['LANGUAGE_CODE']
    outurl = url.replace('/%s/' % curlocale, '/%s/' % lang_code)
    return outurl