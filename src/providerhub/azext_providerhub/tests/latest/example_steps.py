# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.cli.testsdk import (live_only)
from azure_devtools.scenario_tests import AllowLargeResponse
from .. import try_manual


# EXAMPLE: /CustomRollouts/put/CustomRollouts_CreateOrUpdate
@try_manual
def step_custom_rollout_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub custom-rollout create '
             '--provider-namespace "{providerNamespace}" '
             '--rollout-name "{customRolloutName}" '
             '--canary regions="BrazilUS" '
             '--canary regions="EastUS2EUAP"',
             checks=[])


# EXAMPLE: /CustomRollouts/get/CustomRollouts_Get
@try_manual
def step_custom_rollout_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub custom-rollout show '
             '--provider-namespace "{providerNamespace}" '
             '--rollout-name "{customRolloutName}"',
             checks=checks)


# EXAMPLE: /CustomRollouts/get/CustomRollouts_ListByProviderRegistration
@AllowLargeResponse()
@try_manual
def step_custom_rollout_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub custom-rollout list '
             '--provider-namespace "{providerNamespace}"',
             checks=checks)


# EXAMPLE: /DefaultRollouts/put/DefaultRollouts_CreateOrUpdate
@AllowLargeResponse()
@live_only()
def step_default_rollout_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub default-rollout create '
             '--provider-namespace "{providerNamespace}" '
             '--rollout-name "{defaultRolloutName}" '
             '--row2-wait-duration "PT2H" '
             '--skip-regions "brazilus, centraluseuap"',
             checks=checks)


# EXAMPLE: /DefaultRollouts/get/DefaultRollouts_Get
@AllowLargeResponse()
@try_manual
def step_default_rollout_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub default-rollout show '
             '--provider-namespace "{providerNamespace}" '
             '--rollout-name "{defaultRolloutName}"',
             checks=checks)


# EXAMPLE: /DefaultRollouts/get/DefaultRollouts_ListByProviderRegistration
@AllowLargeResponse()
@try_manual
def step_default_rollout_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub default-rollout list '
             '--provider-namespace "{providerNamespace}"',
             checks=checks)


# EXAMPLE: /DefaultRollouts/post/DefaultRollouts_Stop
@try_manual
def step_default_rollout_stop(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub default-rollout stop '
             '--provider-namespace "{providerNamespace}" '
             '--rollout-name "{defaultRolloutName}"',
             checks=checks)


# EXAMPLE: /DefaultRollouts/delete/DefaultRollouts_Delete
@try_manual
def step_default_rollout_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub default-rollout delete -y '
             '--provider-namespace "{providerNamespace}" '
             '--rollout-name "{defaultRolloutName}"',
             checks=checks)


# EXAMPLE: /Operations/get/Operations_ListByProviderRegistration
@AllowLargeResponse()
@try_manual
def step_operation_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub operation list '
             '--provider-namespace "{providerNamespace}"',
             checks=checks)


# EXAMPLE: /Operations/delete/Operations_Delete
@try_manual
def step_operation_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub operation delete -y '
             '--provider-namespace "{providerNamespace}"',
             checks=checks)


# EXAMPLE: /providerhub/post/CheckinManifest
@try_manual
def step_manifest_checkin(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub manifest checkin '
             '--environment "Prod" '
             '--arm-manifest-location "EastUS2EUAP" '
             '--provider-namespace "{providerNamespace}"',
             checks=checks)


# EXAMPLE: /providerhub/post/GenerateManifest
@AllowLargeResponse()
@try_manual
def step_manifest_generate(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub manifest generate '
             '--provider-namespace "{providerNamespace}"',
             checks=checks)


# EXAMPLE: /ProviderRegistrations/put/ProviderRegistrations_CreateOrUpdate
@AllowLargeResponse()
@try_manual
def step_provider_registration_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub provider-registration create '
             '--providerhub-metadata-provider-authorizations '
             'application-id="3d834152-5efa-46f7-85a4-a18c2b5d46f9" '
             'role-definition-id="760505bf-dcfa-4311-b890-18da392a00b2" '
             '--providerhub-metadata-rp-authentication allowed-audiences="https://management.core.windows.net/" '
             '--service-tree-infos service-id="6f53185c-ea09-4fc3-9075-318dec805303" '
             'component-id="6f53185c-ea09-4fc3-9075-318dec805303" '
             '--capabilities effect="Allow" quota-id="CSP_2015-05-01" '
             '--capabilities effect="Allow" quota-id="CSP_MG_2017-12-01" '
             '--manifest-owners "SPARTA-PlatformServiceAdministrator" '
             '--incident-contact-email "helpme@contoso.com" '
             '--incident-routing-service "Contoso Resource Provider" '
             '--incident-routing-team "Contoso Triage" '
             '--provider-type "Internal" '
             '--provider-version "2.0" '
             '--provider-namespace "{providerNamespace}"',
             checks=checks)


# EXAMPLE: /ProviderRegistrations/get/ProviderRegistrations_Get
@AllowLargeResponse()
@try_manual
def step_provider_registration_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub provider-registration show '
             '--provider-namespace "{providerNamespace}"',
             checks=checks)


# EXAMPLE: /ProviderRegistrations/get/ProviderRegistrations_List
@AllowLargeResponse()
@try_manual
def step_provider_registration_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub provider-registration list',
             checks=checks)


# EXAMPLE: /ProviderRegistrations/post/ProviderRegistrations_GenerateOperations
@AllowLargeResponse()
@try_manual
def step_provider_registration_generate_operation(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub provider-registration generate-operation '
             '--provider-namespace "{providerNamespace}"',
             checks=checks)


# EXAMPLE: /ProviderRegistrations/delete/ProviderRegistrations_Delete
@try_manual
def step_provider_registration_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub provider-registration delete -y '
             '--provider-namespace "{providerNamespace}" ',
             checks=checks)


# EXAMPLE: /ResourceTypeRegistration/put/ResourceTypeRegistration_CreateOrUpdate
@AllowLargeResponse()
@try_manual
def step_resource_type_registration_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub resource-type-registration create '
             '--endpoints api-versions="2018-11-01-preview,2020-01-01-preview,2019-01-01" '
             'locations="West US, West Central US,West Europe,Southeast Asia, West US 2,'
             'East US 2 EUAP, North Europe, East US, East Asia" '
             'required-features="Microsoft.Contoso/RPaaSSampleApp" '
             '--regionality "Regional" '
             '--routing-type "Default" '
             '--swagger-specifications api-versions="2018-11-01-preview,'
             '2020-01-01-preview,2019-01-01" swagger-spec-folder-uri="https://github.com/'
             'Azure/azure-rest-api-specs-pr/blob/RPSaaSMaster/specification/rpsaas/'
             'resource-manager/Microsoft.Contoso/" '
             '--provider-namespace "{providerNamespace}" '
             '--enable-async-operation true '
             '--resource-move-policy validation-required=false '
             'cross-resource-group-move-enabled=true cross-subscription-move-enabled=true '
             '--resource-type "{resourceType}"',
             checks=checks)


# EXAMPLE: /ResourceTypeRegistration/delete/ResourceTypeRegistration_Delete
@try_manual
def step_resource_type_registration_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub resource-type-registration delete -y '
             '--provider-namespace "{providerNamespace}" '
             '--resource-type "{resourceType}"',
             checks=checks)


# EXAMPLE: /ResourceTypeRegistrations/get/ResourceTypeRegistrations_Get
@AllowLargeResponse()
@try_manual
def step_resource_type_registration_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub resource-type-registration show '
             '--provider-namespace "{providerNamespace}" '
             '--resource-type "{resourceType}"',
             checks=checks)


# EXAMPLE: /ResourceTypeRegistrations/get/ResourceTypeRegistrations_ListByProviderRegistration
@AllowLargeResponse()
@try_manual
def step_resource_type_registration_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az providerhub resource-type-registration list '
             '--provider-namespace "{providerNamespace}"',
             checks=checks)