# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2016 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
Cookiecutter Topology Node module
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

# Topology already includes a base class for nodes that includes certain
# capabilities commonly used. This can be changed or removed if necessary.
from topology.node import CommonNode

# Same for the base shell imported here, this class incorporates common shell
# utilities and can be changed or removed if necessary too.
from topology.shell import PexpectBashShell


class {{ cookiecutter.class_name }}(CommonNode):
    """
    {{ cookiecutter.node_name }} for the {{ cookiecutter.platform_engine }} platform engine.

    See :class:`topology.base.CommonNode` for more information.
    """

    # Change this method as needed
    def __init__(self, identifier, **kwargs):

        super({{ cookiecutter.class_name }}, self).__init__(identifier, **kwargs)

        # Set your shells as needed
        self._shells['bash'] = PexpectBashShell()


__all__ = ['{{ cookiecutter.class_name }}']
