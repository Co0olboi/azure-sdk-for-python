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


class VaultProperties(Model):
    """Properties of the vault.

    All required parameters must be populated in order to send to Azure.

    :param tenant_id: Required. The Azure Active Directory tenant ID that
     should be used for authenticating requests to the key vault.
    :type tenant_id: str
    :param sku: Required. SKU details
    :type sku: ~azure.mgmt.keyvault.models.Sku
    :param access_policies: An array of 0 to 16 identities that have access to
     the key vault. All identities in the array must use the same tenant ID as
     the key vault's tenant ID.
    :type access_policies: list[~azure.mgmt.keyvault.models.AccessPolicyEntry]
    :param vault_uri: The URI of the vault for performing operations on keys
     and secrets.
    :type vault_uri: str
    :param enabled_for_deployment: Property to specify whether Azure Virtual
     Machines are permitted to retrieve certificates stored as secrets from the
     key vault.
    :type enabled_for_deployment: bool
    :param enabled_for_disk_encryption: Property to specify whether Azure Disk
     Encryption is permitted to retrieve secrets from the vault and unwrap
     keys.
    :type enabled_for_disk_encryption: bool
    :param enabled_for_template_deployment: Property to specify whether Azure
     Resource Manager is permitted to retrieve secrets from the key vault.
    :type enabled_for_template_deployment: bool
    :param enable_soft_delete: Property to specify whether the 'soft delete'
     functionality is enabled for this key vault. It does not accept false
     value.
    :type enable_soft_delete: bool
    :param create_mode: The vault's create mode to indicate whether the vault
     need to be recovered or not. Possible values include: 'recover', 'default'
    :type create_mode: str or ~azure.mgmt.keyvault.models.CreateMode
    :param enable_purge_protection: Property specifying whether protection
     against purge is enabled for this vault. Setting this property to true
     activates protection against purge for this vault and its content - only
     the Key Vault service may initiate a hard, irrecoverable deletion. The
     setting is effective only if soft delete is also enabled. Enabling this
     functionality is irreversible - that is, the property does not accept
     false as its value.
    :type enable_purge_protection: bool
    :param network_acls: A collection of rules governing the accessibility of
     the vault from specific network locations.
    :type network_acls: ~azure.mgmt.keyvault.models.NetworkRuleSet
    """

    _validation = {
        'tenant_id': {'required': True},
        'sku': {'required': True},
    }

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'access_policies': {'key': 'accessPolicies', 'type': '[AccessPolicyEntry]'},
        'vault_uri': {'key': 'vaultUri', 'type': 'str'},
        'enabled_for_deployment': {'key': 'enabledForDeployment', 'type': 'bool'},
        'enabled_for_disk_encryption': {'key': 'enabledForDiskEncryption', 'type': 'bool'},
        'enabled_for_template_deployment': {'key': 'enabledForTemplateDeployment', 'type': 'bool'},
        'enable_soft_delete': {'key': 'enableSoftDelete', 'type': 'bool'},
        'create_mode': {'key': 'createMode', 'type': 'CreateMode'},
        'enable_purge_protection': {'key': 'enablePurgeProtection', 'type': 'bool'},
        'network_acls': {'key': 'networkAcls', 'type': 'NetworkRuleSet'},
    }

    def __init__(self, **kwargs):
        super(VaultProperties, self).__init__(**kwargs)
        self.tenant_id = kwargs.get('tenant_id', None)
        self.sku = kwargs.get('sku', None)
        self.access_policies = kwargs.get('access_policies', None)
        self.vault_uri = kwargs.get('vault_uri', None)
        self.enabled_for_deployment = kwargs.get('enabled_for_deployment', None)
        self.enabled_for_disk_encryption = kwargs.get('enabled_for_disk_encryption', None)
        self.enabled_for_template_deployment = kwargs.get('enabled_for_template_deployment', None)
        self.enable_soft_delete = kwargs.get('enable_soft_delete', None)
        self.create_mode = kwargs.get('create_mode', None)
        self.enable_purge_protection = kwargs.get('enable_purge_protection', None)
        self.network_acls = kwargs.get('network_acls', None)
