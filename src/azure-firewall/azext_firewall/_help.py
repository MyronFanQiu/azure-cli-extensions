# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

# region AzureFirewalls
helps['network firewall'] = """
    type: group
    short-summary: Manage and configure Azure Firewalls.
"""

helps['network firewall create'] = """
    type: command
    short-summary: Create an Azure Firewall.
"""

helps['network firewall delete'] = """
    type: command
    short-summary: Delete an Azure Firewall.
"""

helps['network firewall list'] = """
    type: command
    short-summary: List Azure Firewalls.
"""

helps['network firewall show'] = """
    type: command
    short-summary: Get the details of an Azure Firewall.
"""

helps['network firewall update'] = """
    type: command
    short-summary: Update an Azure Firewall.
"""
# endregion

# region AzureFirewall IP Configurations
helps['network firewall ip-config'] = """
    type: group
    short-summary: Manage and configure Azure Firewall IP configurations.
"""

helps['network firewall ip-config create'] = """
    type: command
    short-summary: Create an Azure Firewall IP configuration.
"""

helps['network firewall ip-config delete'] = """
    type: command
    short-summary: Delete an Azure Firewall IP configuration.
"""

helps['network firewall ip-config list'] = """
    type: command
    short-summary: List Azure Firewall IP configurations.
"""

helps['network firewall ip-config show'] = """
    type: command
    short-summary: Get the details of an Azure Firewall IP configuration.
"""
# endregion

# region AzureFirewall Network Rules
helps['network firewall network-rule'] = """
    type: group
    short-summary: Manage and configure Azure Firewall network rules.
"""

helps['network firewall network-rule create'] = """
    type: command
    short-summary: Create an Azure Firewall network rule.
"""

helps['network firewall network-rule delete'] = """
    type: command
    short-summary: Delete an Azure Firewall network rule.
"""

helps['network firewall network-rule list'] = """
    type: command
    short-summary: List Azure Firewall network rules.
"""

helps['network firewall network-rule show'] = """
    type: command
    short-summary: Get the details of an Azure Firewall network rule.
"""

helps['network firewall network-rule collection'] = """
    type: group
    short-summary: Manage and configure Azure Firewall network rule collections.
    long-summary: Collections are created as part of the `az network firewall network-rule create` command.
"""

helps['network firewall network-rule collection delete'] = """
    type: command
    short-summary: Delete an Azure Firewall network rule collection.
"""

helps['network firewall network-rule collection list'] = """
    type: command
    short-summary: List Azure Firewall network rule collections.
"""

helps['network firewall network-rule collection show'] = """
    type: command
    short-summary: Get the details of an Azure Firewall network rule collection.
"""
# endregion

# region AzureFirewall NAT Rules
helps['network firewall nat-rule'] = """
    type: group
    short-summary: Manage and configure Azure Firewall NAT rules.
"""

helps['network firewall nat-rule create'] = """
    type: command
    short-summary: Create an Azure Firewall NAT rule.
"""

helps['network firewall nat-rule delete'] = """
    type: command
    short-summary: Delete an Azure Firewall NAT rule.
"""

helps['network firewall nat-rule list'] = """
    type: command
    short-summary: List Azure Firewall NAT rules.
"""

helps['network firewall nat-rule show'] = """
    type: command
    short-summary: Get the details of an Azure Firewall NAT rule.
"""

helps['network firewall nat-rule collection'] = """
    type: group
    short-summary: Manage and configure Azure Firewall NAT rules.
    long-summary: Collections are created as part of the `az network firewall nat-rule create` command.
"""

helps['network firewall nat-rule collection delete'] = """
    type: command
    short-summary: Delete an Azure Firewall NAT rule collection.
"""

helps['network firewall nat-rule collection list'] = """
    type: command
    short-summary: List Azure Firewall NAT rule collections.
"""

helps['network firewall nat-rule collection show'] = """
    type: command
    short-summary: Get the details of an Azure Firewall NAT rule collection.
"""
# endregion

# region AzureFirewall Application Rules
helps['network firewall application-rule'] = """
    type: group
    short-summary: Manage and configure Azure Firewall application rules.
"""

helps['network firewall application-rule create'] = """
    type: command
    short-summary: Create an Azure Firewall application rule.
"""

helps['network firewall application-rule delete'] = """
    type: command
    short-summary: Delete an Azure Firewall application rule.
"""

helps['network firewall application-rule list'] = """
    type: command
    short-summary: List Azure Firewall application rules.
"""

helps['network firewall application-rule show'] = """
    type: command
    short-summary: Get the details of an Azure Firewall application rule.
"""

helps['network firewall application-rule collection'] = """
    type: group
    short-summary: Manage and configure Azure Firewall application rule collections.
    long-summary: Collections are created as part of the `az network firewall application-rule create` command.
"""

helps['network firewall application-rule collection delete'] = """
    type: command
    short-summary: Delete an Azure Firewall application rule collection.
"""

helps['network firewall application-rule collection list'] = """
    type: command
    short-summary: List Azure Firewall application rule collections.
"""

helps['network firewall application-rule collection show'] = """
    type: command
    short-summary: Get the details of an Azure Firewall application rule collection.
"""
# endregion

# region AzureFirewall Policy
helps['network firewall application-rule'] = """
    type: group
    short-summary: Manage and configure Azure Firewall application rules.
"""

helps['network firewall application-rule create'] = """
    type: command
    short-summary: Create an Azure Firewall application rule.
"""

helps['network firewall application-rule delete'] = """
    type: command
    short-summary: Delete an Azure Firewall application rule.
"""

helps['network firewall application-rule list'] = """
    type: command
    short-summary: List Azure Firewall application rules.
"""

helps['network firewall application-rule show'] = """
    type: command
    short-summary: Get the details of an Azure Firewall application rule.
"""

helps['network firewall application-rule collection'] = """
    type: group
    short-summary: Manage and configure Azure Firewall application rule collections.
    long-summary: Collections are created as part of the `az network firewall application-rule create` command.
"""

helps['network firewall application-rule collection delete'] = """
    type: command
    short-summary: Delete an Azure Firewall application rule collection.
"""

helps['network firewall application-rule collection list'] = """
    type: command
    short-summary: List Azure Firewall application rule collections.
"""

helps['network firewall application-rule collection show'] = """
    type: command
    short-summary: Get the details of an Azure Firewall application rule collection.
"""
# endregion

# region AzureFirewall Policy
helps['network firewall policy'] = """
    type: group
    short-summary: Manage and configure Azure Firewall policy.
"""

helps['network firewall policy create'] = """
    type: command
    short-summary: Create an Azure Firewall policy.
"""

helps['network firewall policy update'] = """
    type: command
    short-summary: Update an Azure Firewall policy.
"""

helps['network firewall policy delete'] = """
    type: command
    short-summary: Delete an Azure Firewall policy.
"""

helps['network firewall policy show'] = """
    type: command
    short-summary: Show an Azure Firewall policy.
"""

helps['network firewall policy list'] = """
    type: command
    short-summary: List all Azure Firewall policies.
"""

helps['network firewall policy rule-group'] = """
    type: group
    short-summary: Manage and configure Azure Firewall policy rule group.
"""

helps['network firewall policy rule-group create'] = """
    type: command
    short-summary: Create an Azure Firewall policy rule group.
"""

helps['network firewall policy rule-group update'] = """
    type: command
    short-summary: Update an Azure Firewall policy rule group.
"""

helps['network firewall policy rule-group list'] = """
    type: command
    short-summary: List all Azure Firewall policy rule groups.
"""

helps['network firewall policy rule-group show'] = """
    type: command
    short-summary: Show an Azure Firewall policy rule group.
"""

helps['network firewall policy rule-group delete'] = """
    type: command
    short-summary: Delete an Azure Firewall policy rule group.
"""

helps['network firewall policy rule-group rule'] = """
    type: group
    short-summary: Manage and configure Azure Firewall policy rules in the rule group.
    long-summary: |
        Currently, Azure Firewall policy support two kinds of rules which are Filter Rule and NAT Rule. There are also two kinds of conditions which are application condition and network condition.
        NAT rule can only use one network condition. Filter rule support including a list of condition in it. But all of conditions should be the same type.
"""

helps['network firewall policy rule-group rule add-filter-rule'] = """
    type: command
    short-summary: Add a filter rule into an Azure Firewall policy rule group.
    long-summary: |
        Common Condition Arguments are used for both Network condition and Application condition. If you want to add more conditions into filter rule, please use "az network policy rule-group rule condition add/remove"
    examples:
        - name: Add a filter rule with Network condition into the rule group
          text: az network firewall policy rule-group rule add-filter-rule -g {rg} --policy-name {policy} --rule-group-name {rulegroup}
                --action Allow --condition-name network_condition --condition-type NetworkRuleCondition
                --description "test" --destination-addresses "202.120.36.15" --source-addresses "202.120.36.13" "202.120.36.14" --destination-ports 12003 12004
                --ip-protocols TCP UDP --rule-priority 11002 --name filter_rule
        - name: Add a filter rule with Application condition into the rule group
          text: az network firewall policy rule-group rule add-filter-rule -g {rg} --policy-name {policy} --rule-group-name {rulegroup}
                --action Allow --condition-name application_condition --condition-type ApplicationRuleCondition --description "test"
                --destination-addresses "202.120.36.15" "202.120.36.16" --source-addresses "202.120.36.13" "202.120.36.14" --protocols Http=12800 Https=12801
                --fqdn-tags AzureBackup HDInsight --rule-priority 11100 --name filter_rule
"""

helps['network firewall policy rule-group rule add-nat-rule'] = """
    type: command
    short-summary: Add a NAT rule into an Azure Firewall policy rule group.
    examples:
        - name: Add a nat rule into the rule group
          text: az network firewall policy rule-group rule add-nat-rule -n nat_rule --rule-priority 10003
                --policy-name {policy} -g {rg} --rule-group-name {rulegroup} --action DNAT
                --condition-name network_condition --description "test" --destination-addresses "202.120.36.15"
                --source-addresses "202.120.36.13" "202.120.36.14" --translated-address 128.1.1.1
                --translated-port 1234 --destination-ports 12000 12001 --ip-protocols TCP UDP
"""

helps['network firewall policy rule-group rule list'] = """
    type: command
    short-summary: List all rules of an Azure Firewall policy rule group.
"""

helps['network firewall policy rule-group rule remove'] = """
    type: command
    short-summary: Remove a rule from an Azure Firewall policy rule group.
"""

helps['network firewall policy rule-group rule condition'] = """
    type: group
    short-summary: Manage and configure the condition of a filter rule in the rule group of Azure Firewall policy.
"""

helps['network firewall policy rule-group rule condition add'] = """
    type: command
    short-summary: Add a condition into an Azure Firewall policy rule.
"""

helps['network firewall policy rule-group rule condition remove'] = """
    type: command
    short-summary: Remove a condition from an Azure Firewall policy rule.
"""
# endregion
