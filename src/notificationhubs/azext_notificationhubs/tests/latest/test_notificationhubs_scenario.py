# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest
import time

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer, JMESPathCheck)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class NotificationHubsScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_notificationhubs')
    def test_notificationhubs(self, resource_group):

        self.kwargs.update({
            'name': 'mycli-hub-ns-test3',
            'hubname': 'mycli-hub-test3',
            'rg': resource_group
        })

        self.cmd('az notificationhubs check-availability --name {name} -o json', checks=[
            self.check('isAvailiable', True),
            self.check('name', '{name}')
        ])
        self.cmd('az notificationhubs create --namespace-name {name} -g {rg} --location "japaneast" -o json', checks=[
            self.check('name', '{name}')
        ])
        if self.is_live:
            time.sleep(20)
        self.cmd('az notificationhubs show --namespace-name {name} -g {rg} -o json', checks=[
            self.check('name', '{name}')
        ])
        self.cmd('az notificationhubs list -g {rg} -o json', checks=[])
        self.cmd('az notificationhubs notification-hub check-notification-hub-availability -g {rg} --namespace-name {name} --name {hubname} -o json', checks=[
            self.check('isAvailiable', True)
        ])
        if self.is_live:
            time.sleep(20)
        self.cmd('az notificationhubs notification-hub create --namespace-name {name} --notification-hub-name {hubname} --location "japaneast" -g {rg} -o json', checks=[
            self.check('name', '{hubname}')
        ])
        if self.is_live:
            time.sleep(20)
        self.cmd('az notificationhubs notification-hub show --namespace-name {name} --notification-hub-name {hubname} -g {rg}', checks=[])
        self.cmd('az notificationhubs notification-hub delete --namespace-name {name} --notification-hub-name {hubname} -g {rg}', checks=[])