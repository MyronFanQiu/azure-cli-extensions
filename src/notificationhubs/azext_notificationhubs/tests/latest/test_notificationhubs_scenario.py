# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import time
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class NotificationHubsScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_notificationhubs')
    def test_notificationhubs(self, resource_group):

        self.kwargs.update({
            'namespace': 'mycli-not-namespace-test2',
            'hub': 'mycli-not-hub-test2'
        })

        self.cmd('az notificationhubs namespace check_availability '
                 '--name {namespace}',
                 checks=[])

        self.cmd('az notificationhubs namespace create '
                 '--resource-group {rg} '
                 '--namespace-name {namespace} '
                 '--location "South Central US" '
                 '--sku-name "Standard" '
                 '--sku-tier "Standard"',
                 checks=[])

        if self.is_live:
            time.sleep(20)

        self.cmd('az notificationhubs hub create '
                 '--resource-group {rg} '
                 '--namespace-name {namespace} '
                 '--notification-hub-name {hub} '
                 '--sku-name "Standard"',
                 checks=[])
