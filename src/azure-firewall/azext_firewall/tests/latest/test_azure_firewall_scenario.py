# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer, StorageAccountPreparer, JMESPathCheck, NoneCheck,
                               api_version_constraint)
from azure.cli.core.profiles import ResourceType
from azext_firewall.profiles import CUSTOM_FIREWALL


class AzureFirewallScenario(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_azure_firewall')
    def test_azure_firewall(self, resource_group):

        self.kwargs.update({
            'af': 'af1',
            'coll': 'rc1',
            'rule1': 'rule1',
            'rule2': 'rule2'
        })
        self.cmd('network firewall create -g {rg} -n {af}')
        self.cmd('network firewall show -g {rg} -n {af}')
        self.cmd('network firewall list -g {rg}')
        self.cmd('network firewall delete -g {rg} -n {af}')

    @ResourceGroupPreparer(name_prefix='cli_test_azure_firewall_rules')
    def test_azure_firewall_rules(self, resource_group):

        self.kwargs.update({
            'af': 'af1',
            'coll': 'rc1',
            'coll2': 'rc2',
            'network_rule1': 'network-rule1',
            'nat_rule1': 'nat-rule1'
        })
        self.cmd('network firewall create -g {rg} -n {af}')
        self.cmd('network firewall network-rule create -g {rg} -n {network_rule1} -c {coll} --priority 10000 --action Allow -f {af} --source-addresses 10.0.0.0 111.1.0.0/24 --protocols UDP TCP ICMP --destination-fqdns www.bing.com --destination-ports 80')
        self.cmd('network firewall nat-rule create -g {rg} -n {network_rule1} -c {coll2} --priority 10001 --action Dnat -f {af} --source-addresses 10.0.0.0 111.1.0.0/24 --protocols UDP TCP --translated-fqdn server1.internal.com --destination-ports 96 --destination-addresses 12.36.22.14 --translated-port 95')
        self.cmd('network firewall delete -g {rg} -n {af}')

    @ResourceGroupPreparer(name_prefix='cli_test_azure_firewall_zones', location='eastus')
    def test_azure_firewall_zones(self, resource_group):

        self.kwargs.update({
            'af': 'af1',
            'coll': 'rc1',
        })
        self.cmd('network firewall create -g {rg} -n {af} --zones 1 3')
        self.cmd('network firewall update -g {rg} -n {af} --zones 1')

    @ResourceGroupPreparer(name_prefix='cli_test_azure_firewall_policy', location='westcentralus')
    def test_azure_firewall_policy(self, resource_group, resource_group_location):
        self.kwargs.update({
            'rulegroup': 'myrulegroup',
            'policy': 'mypolicy',
            'rg': resource_group,
            'location': resource_group_location
        })
        self.cmd('network firewall policy create -g {rg} -n {policy} -l {location}')
        self.cmd('network firewall policy rule-group create -g {rg} --priority 10000 --policy-name {policy} -n {rulegroup}')

        self.cmd('az network firewall policy rule-group rule add-nat-rule -n nat_rule_3 --rule-priority 10005 \
                 --policy-name {policy} -g {rg} --rule-group-name {rulegroup} --action DNAT \
                 --condition-name network_condition --description "test" --destination-addresses "202.120.36.15" \
                 --source-addresses "202.120.36.13" "202.120.36.14" --translated-address 128.1.1.1 \
                 --translated-port 1234 --destination-ports 12000 12001 --ip-protocols TCP UDP --defer')

        self.cmd('az network firewall policy rule-group rule add-nat-rule -n nat_rule_2 --rule-priority 10004 \
                 --policy-name {policy} -g {rg} --rule-group-name {rulegroup} --action DNAT \
                 --condition-name network_condition --description "test" --destination-addresses "202.120.36.15" \
                 --source-addresses "202.120.36.13" "202.120.36.14" --translated-address 128.1.1.1 \
                 --translated-port 1234 --destination-ports 12000 12001 --ip-protocols TCP UDP --defer')


        self.cmd('az network firewall policy rule-group rule add-nat-rule -n nat_rule_1 --rule-priority 10003 \
                 --policy-name {policy} -g {rg} --rule-group-name {rulegroup} --action DNAT \
                 --condition-name network_condition --description "test" --destination-addresses "202.120.36.15" \
                 --source-addresses "202.120.36.13" "202.120.36.14" --translated-address 128.1.1.1 \
                 --translated-port 1234 --destination-ports 12000 12001 --ip-protocols TCP UDP')

        self.cmd('az network firewall policy rule-group rule remove --policy-name {policy} -g {rg} --rule-group-name {rulegroup} --name nat_rule_1 --defer')
        self.cmd('az network firewall policy rule-group rule remove --policy-name {policy} -g {rg} --rule-group-name {rulegroup} --name nat_rule_2 --defer')
        self.cmd('az network firewall policy rule-group rule remove --policy-name {policy} -g {rg} --rule-group-name {rulegroup} --name nat_rule_3')

        self.cmd('network firewall policy rule-group rule add-filter-rule -g {rg} --policy-name {policy} --rule-group-name {rulegroup} \
                 --action Allow --condition-name network_condition --condition-type NetworkRuleCondition \
                 --description "test" --destination-addresses "202.120.36.15" --source-addresses "202.120.36.13" "202.120.36.14" --destination-ports 12003 12004 \
                 --ip-protocols TCP UDP --rule-priority 11000 --name filter_rule_2 --defer')

        self.cmd('network firewall policy rule-group rule add-filter-rule -g {rg} --policy-name {policy} --rule-group-name {rulegroup} \
                 --action Allow --condition-name network_condition --condition-type NetworkRuleCondition \
                 --description "test" --destination-addresses "202.120.36.15" --source-addresses "202.120.36.13" "202.120.36.14" --destination-ports 12003 12004 \
                 --ip-protocols TCP UDP --rule-priority 11001 --name filter_rule_3 --defer')

        self.cmd('network firewall policy rule-group rule add-filter-rule -g {rg} --policy-name {policy} --rule-group-name {rulegroup} \
                 --action Allow --condition-name network_condition --condition-type NetworkRuleCondition \
                 --description "test" --destination-addresses "202.120.36.15" --source-addresses "202.120.36.13" "202.120.36.14" --destination-ports 12003 12004 \
                 --ip-protocols TCP UDP --rule-priority 11002 --name filter_rule_1')

        self.cmd('az network firewall policy rule-group rule add-filter-rule -g {rg} --policy-name {policy} --rule-group-name {rulegroup} \
                 --action Allow --condition-name network_condition --condition-type ApplicationRuleCondition --description "test" \
                 --destination-addresses "202.120.36.15" "202.120.36.16" --source-addresses "202.120.36.13" "202.120.36.14" --protocols Http=12800 Https=12801 \
                 --fqdn-tags AzureBackup HDInsight --rule-priority 11100 --name filter_rule_5 --defer')

        self.cmd('az network firewall policy rule-group rule condition add -g {rg} --policy-name {policy} --rule-group-name {rulegroup} \
                 --condition-name network_condition_2 --condition-type ApplicationRuleCondition --description "test" --destination-addresses "202.120.36.15" "202.120.36.16" \
                 --source-addresses "202.120.36.13" "202.120.36.14" --protocols Http=12800 Https=12801 --fqdn-tags AzureBackup HDInsight --name filter_rule_5 --defer')

        self.cmd('az network firewall policy rule-group rule condition add -g {rg} --policy-name {policy} --rule-group-name {rulegroup} \
                 --condition-name network_condition_3 --condition-type ApplicationRuleCondition \
                 --description "test" --destination-addresses "202.120.36.15" "202.120.36.16" --source-addresses "202.120.36.13" "202.120.36.14" \
                 --protocols Http=12800 Https=12801 --target-fqdns "natRuleTest1.net" "natRuleTest2.net" --name filter_rule')

        self.cmd('az network firewall policy rule-group rule condition remove -g {rg} --policy-name {policy} --rule-group-name {rulegroup} -n network_condition_3 --rule-name filter_rule_5 --defer')
        self.cmd('az network firewall policy rule-group rule condition remove -g {rg} --policy-name {policy} --rule-group-name {rulegroup} -n network_condition_2 --rule-name filter_rule_5')
