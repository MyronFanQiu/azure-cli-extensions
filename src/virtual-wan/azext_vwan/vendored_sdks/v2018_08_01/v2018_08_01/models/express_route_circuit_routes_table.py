# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ExpressRouteCircuitRoutesTable(Model):
    """The routes table associated with the ExpressRouteCircuit.

    :param network: IP address of a network entity
    :type network: str
    :param next_hop: NextHop address
    :type next_hop: str
    :param loc_prf: Local preference value as set with the set
     local-preference route-map configuration command
    :type loc_prf: str
    :param weight: Route Weight.
    :type weight: int
    :param path: Autonomous system paths to the destination network.
    :type path: str
    """

    _attribute_map = {
        'network': {'key': 'network', 'type': 'str'},
        'next_hop': {'key': 'nextHop', 'type': 'str'},
        'loc_prf': {'key': 'locPrf', 'type': 'str'},
        'weight': {'key': 'weight', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExpressRouteCircuitRoutesTable, self).__init__(**kwargs)
        self.network = kwargs.get('network', None)
        self.next_hop = kwargs.get('next_hop', None)
        self.loc_prf = kwargs.get('loc_prf', None)
        self.weight = kwargs.get('weight', None)
        self.path = kwargs.get('path', None)
