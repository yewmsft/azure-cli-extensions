# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
from __future__ import annotations

import os.path
from typing import TYPE_CHECKING

from argcomplete.completers import FilesCompleter
from azure.cli.core.commands.parameters import (
    file_type,
    get_enum_type,
    get_location_type,
    get_three_state_flag,
    tags_type,
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from knack.arguments import CaseInsensitiveList, CLIArgumentType

from azext_connectedk8s._constants import (
    AHB_Enum_Values,
    Distribution_Enum_Values,
    Feature_Values,
    Infrastructure_Enum_Values,
)

from ._validators import (
    override_client_request_id_header,
    validate_enable_oidc_issuer_updates,
    validate_gateway_updates,
    validate_private_link_properties,
    validate_self_hosted_issuer,
    validate_workload_identity_updates,
)
from .action import (
    AddConfigurationProtectedSettings,
    AddConfigurationSettings,
)

if TYPE_CHECKING:
    from knack.commands import CLICommand

    from azext_connectedk8s import Connectedk8sCommandsLoader


features_types = CLIArgumentType(nargs="+", choices=CaseInsensitiveList(Feature_Values))


def load_arguments(self: Connectedk8sCommandsLoader, _: CLICommand) -> None:
    pls_arm_id_type = CLIArgumentType(
        options_list=["--private-link-scope-resource-id", "--pls-arm-id"],
        arg_group="PrivateLink",
        help="ARM resource id of the private link scope resource to which this connected cluster is associated.",
        is_preview=True,
    )

    with self.argument_context("connectedk8s connect") as c:
        c.argument("tags", tags_type)
        if os.getenv("AZURE_ACCESS_TOKEN"):
            c.argument("location", arg_type=get_location_type(self.cli_ctx))
        else:
            c.argument(
                "location",
                arg_type=get_location_type(self.cli_ctx),
                validator=get_default_location_from_resource_group,
            )
        c.argument(
            "cluster_name",
            options_list=["--name", "-n"],
            help="The name of the connected cluster.",
        )
        c.argument(
            "kube_config",
            options_list=["--kube-config"],
            help="Path to the kube config file.",
        )
        c.argument(
            "kube_context",
            options_list=["--kube-context"],
            help="Kubconfig context from current machine.",
        )
        c.argument(
            "https_proxy",
            options_list=["--proxy-https"],
            arg_group="Proxy",
            help="Https proxy URL to be used.",
        )
        c.argument(
            "http_proxy",
            options_list=["--proxy-http"],
            arg_group="Proxy",
            help="Http proxy URL to be used.",
        )
        c.argument(
            "no_proxy",
            options_list=["--proxy-skip-range"],
            arg_group="Proxy",
            help="List of URLs/CIDRs for which proxy should not to be used.",
        )
        c.argument(
            "proxy_cert",
            options_list=["--proxy-cert", "--custom-ca-cert"],
            arg_group="Proxy",
            type=file_type,
            completer=FilesCompleter(),  # type: ignore[no-untyped-call]
            help="Path to the certificate file for proxy or custom Certificate Authority",
        )
        c.argument(
            "distribution",
            options_list=["--distribution"],
            help="The Kubernetes distribution which will be running on this connected cluster.",
            arg_type=get_enum_type(Distribution_Enum_Values),
        )
        c.argument(
            "distribution_version",
            help="The Kubernetes distribution version of the connected cluster.",
        )
        c.argument(
            "infrastructure",
            options_list=["--infrastructure"],
            help="The infrastructure on which the Kubernetes cluster represented by this connected cluster will be running on.",
            arg_type=get_enum_type(Infrastructure_Enum_Values),
        )
        c.argument(
            "azure_hybrid_benefit",
            help="Flag to enable/disable Azure Hybrid Benefit feature.",
            arg_type=get_enum_type(AHB_Enum_Values),
        )
        c.argument(
            "disable_auto_upgrade",
            options_list=["--disable-auto-upgrade"],
            action="store_true",
            help="Flag to disable auto upgrade of arc agents.",
        )
        c.argument(
            "cl_oid",
            options_list=["--custom-locations-oid"],
            help="OID of 'custom-locations' app",
        )
        c.argument(
            "enable_private_link",
            arg_type=get_three_state_flag(),
            arg_group="PrivateLink",
            help="Flag to enable/disable private link support on a connected cluster resource. Allowed values: false, true.",
            is_preview=True,
            validator=validate_private_link_properties,
        )
        c.argument("private_link_scope_resource_id", pls_arm_id_type)
        c.argument(
            "onboarding_timeout",
            options_list=["--onboarding-timeout"],
            arg_group="Timeout",
            help="Time required (in seconds) for the arc-agent pods to be installed on the kubernetes cluster. Override this value if the hardware/network constraints on your cluster requires more time for installing the arc-agent pods.",
        )
        c.argument(
            "no_wait",
            options_list=["--no-wait"],
            arg_group="Timeout",
            help="Do not wait for the long-running operation to finish.",
        )
        c.argument(
            "correlation_id",
            options_list=["--correlation-id"],
            help="A guid that is used to internally track the source of cluster onboarding. Please do not modify it unless advised",
            validator=override_client_request_id_header,
        )
        c.argument(
            "container_log_path",
            help="Override the default container log path to enable fluent-bit logging",
        )
        c.argument(
            "skip_ssl_verification",
            action="store_true",
            help="Skip SSL verification for any cluster connection.",
        )
        c.argument(
            "yes",
            options_list=["--yes", "-y"],
            help="Do not prompt for confirmation.",
            action="store_true",
        )
        c.argument(
            "enable_oidc_issuer",
            arg_type=get_three_state_flag(),
            options_list=["--enable-oidc-issuer"],
            arg_group="Workload Identity",
            help="Enable creation of OIDC issuer url used for workload identity federation",
            is_preview=True,
        )
        c.argument(
            "self_hosted_issuer",
            options_list=["--self-hosted-issuer"],
            arg_group="Workload Identity",
            help="Self hosted issuer url for public cloud clusters - AKS, GKE, EKS",
            is_preview=True,
            validator=validate_self_hosted_issuer,
        )
        c.argument(
            "enable_workload_identity",
            arg_type=get_three_state_flag(),
            options_list=["--enable-workload-identity", "--enable-wi"],
            arg_group="Workload Identity",
            help="Enable workload identity webhook",
            is_preview=True,
        )
        c.argument(
            "gateway_resource_id",
            options_list=["--gateway-resource-id"],
            arg_group="Gateway",
            help="ArmID of the Arc Gateway resource.",
            is_preview=True,
        )
        c.argument(
            "configuration_settings",
            options_list=["--configuration-settings", "--config"],
            action=AddConfigurationSettings,
            nargs="+",
            help="Configuration Settings as key=value pair.  Repeat parameter for each setting. Do not use this for secrets, as this value is returned in response.",
            is_preview=True,
        )
        c.argument(
            "configuration_protected_settings",
            options_list=["--config-protected-settings", "--config-protected"],
            action=AddConfigurationProtectedSettings,
            nargs="+",
            help="Configuration Protected Settings as key=value pair.  Repeat parameter for each setting.  Only the key is returned in response, the value is not.",
            is_preview=True,
        )

    with self.argument_context("connectedk8s update") as c:
        c.argument("tags", tags_type)
        c.argument(
            "cluster_name",
            options_list=["--name", "-n"],
            id_part="name",
            help="The name of the connected cluster.",
        )
        c.argument(
            "kube_config",
            options_list=["--kube-config"],
            help="Path to the kube config file.",
        )
        c.argument(
            "kube_context",
            options_list=["--kube-context"],
            help="Kubconfig context from current machine.",
        )
        c.argument(
            "https_proxy",
            options_list=["--proxy-https"],
            arg_group="Proxy",
            help="Https proxy URL to be used.",
        )
        c.argument(
            "http_proxy",
            options_list=["--proxy-http"],
            arg_group="Proxy",
            help="Http proxy URL to be used.",
        )
        c.argument(
            "no_proxy",
            options_list=["--proxy-skip-range"],
            arg_group="Proxy",
            help="List of URLs/CIDRs for which proxy should not to be used.",
        )
        c.argument(
            "distribution",
            help="The Kubernetes distribution which will be running on this connected cluster.",
            arg_type=get_enum_type(Distribution_Enum_Values),
        )
        c.argument(
            "distribution_version",
            help="The Kubernetes distribution version of the connected cluster.",
        )
        c.argument(
            "azure_hybrid_benefit",
            help="Flag to enable/disable Azure Hybrid Benefit feature.",
            arg_type=get_enum_type(AHB_Enum_Values),
        )
        c.argument(
            "proxy_cert",
            options_list=["--proxy-cert", "--custom-ca-cert"],
            arg_group="Proxy",
            type=file_type,
            completer=FilesCompleter(),  # type: ignore[no-untyped-call]
            help="Path to the certificate file for proxy or custom Certificate Authority",
        )
        c.argument(
            "disable_proxy",
            options_list=["--disable-proxy"],
            arg_group="Proxy",
            action="store_true",
            help="Disables proxy settings for agents",
        )
        c.argument(
            "auto_upgrade",
            options_list=["--auto-upgrade"],
            help="Flag to enable/disable auto upgrade of arc agents. By default, auto upgrade of agents is enabled.",
            arg_type=get_enum_type(["true", "false"]),
        )
        c.argument(
            "container_log_path",
            help="Override the default container log path to enable fluent-bit logging",
        )
        c.argument(
            "skip_ssl_verification",
            action="store_true",
            help="Skip SSL verification for any cluster connection.",
        )
        c.argument(
            "yes",
            options_list=["--yes", "-y"],
            help="Do not prompt for confirmation.",
            action="store_true",
        )
        c.argument(
            "enable_oidc_issuer",
            arg_type=get_three_state_flag(),
            options_list=["--enable-oidc-issuer"],
            arg_group="Workload Identity",
            help="Enable creation of OIDC issuer url used for workload identity federation",
            is_preview=True,
            validator=validate_enable_oidc_issuer_updates,
        )
        c.argument(
            "self_hosted_issuer",
            options_list=["--self-hosted-issuer"],
            arg_group="Workload Identity",
            help="Self hosted issuer url for public cloud clusters - AKS, GKE, EKS",
            is_preview=True,
            validator=validate_self_hosted_issuer,
        )
        c.argument(
            "enable_workload_identity",
            arg_type=get_three_state_flag(),
            options_list=["--enable-workload-identity", "--enable-wi"],
            arg_group="Workload Identity",
            help="Enable workload identity webhook",
            is_preview=True,
            validator=validate_workload_identity_updates,
        )
        c.argument(
            "disable_workload_identity",
            arg_type=get_three_state_flag(),
            options_list=["--disable-workload-identity", "--disable-wi"],
            arg_group="Workload Identity",
            help="Disable workload identity webhook",
            is_preview=True,
            validator=validate_workload_identity_updates,
        )
        c.argument(
            "gateway_resource_id",
            options_list=["--gateway-resource-id"],
            arg_group="Gateway",
            help="ArmID of the Arc Gateway resource.",
            validator=validate_gateway_updates,
            is_preview=True,
        )
        c.argument(
            "disable_gateway",
            arg_type=get_three_state_flag(),
            options_list=["--disable-gateway"],
            arg_group="Gateway",
            help="Flag to disable Arc Gateway",
            validator=validate_gateway_updates,
            is_preview=True,
        )
        c.argument(
            "configuration_settings",
            options_list=["--configuration-settings", "--config"],
            action=AddConfigurationSettings,
            nargs="+",
            help="Configuration Settings as key=value pair.  Repeat parameter for each setting. Do not use this for secrets, as this value is returned in response.",
            is_preview=True,
        )
        c.argument(
            "configuration_protected_settings",
            options_list=["--config-protected-settings", "--config-protected"],
            action=AddConfigurationProtectedSettings,
            nargs="+",
            help="Configuration Protected Settings as key=value pair.  Repeat parameter for each setting.  Only the key is returned in response, the value is not.",
            is_preview=True,
        )

    with self.argument_context("connectedk8s upgrade") as c:
        c.argument(
            "cluster_name",
            options_list=["--name", "-n"],
            id_part="name",
            help="The name of the connected cluster.",
        )
        c.argument(
            "kube_config",
            options_list=["--kube-config"],
            help="Path to the kube config file.",
        )
        c.argument(
            "kube_context",
            options_list=["--kube-context"],
            help="Kubconfig context from current machine.",
        )
        c.argument(
            "arc_agent_version",
            options_list=["--agent-version"],
            help="Version of agent to update the helm charts to.",
        )
        c.argument(
            "skip_ssl_verification",
            action="store_true",
            help="Skip SSL verification for any cluster connection.",
        )
        c.argument(
            "upgrade_timeout",
            options_list=["--upgrade-timeout"],
            help="Time required (in seconds) for the arc-agent pods to be upgraded on the kubernetes cluster. Override this value if the hardware/network constraints on your cluster requires more time for upgrading the arc-agent pods.",
        )

    with self.argument_context("connectedk8s enable-features") as c:
        c.argument(
            "cluster_name",
            options_list=["--name", "-n"],
            id_part="name",
            help="The name of the connected cluster.",
        )
        c.argument(
            "kube_config",
            options_list=["--kube-config"],
            help="Path to the kube config file.",
        )
        c.argument(
            "kube_context",
            options_list=["--kube-context"],
            help="Kubconfig context from current machine.",
        )
        c.argument(
            "features",
            features_types,
            options_list=["--features"],
            help="Space-separated list of features you want to enable.",
        )
        c.argument(
            "azrbac_client_id",
            options_list=["--app-id"],
            arg_group="Azure RBAC",
            help="Application ID for enabling Azure RBAC.",
            deprecate_info=c.deprecate(hide=True),
        )
        c.argument(
            "azrbac_client_secret",
            options_list=["--app-secret"],
            arg_group="Azure RBAC",
            help="Application secret for enabling Azure RBAC.",
            deprecate_info=c.deprecate(hide=True),
        )
        c.argument(
            "azrbac_skip_authz_check",
            options_list=["--skip-azure-rbac-list"],
            arg_group="Azure RBAC",
            help="Comma separated list of names of usernames/email/oid. Azure RBAC will be skipped for these users. Specify when enabling azure-rbac.",
        )
        c.argument(
            "cl_oid",
            options_list=["--custom-locations-oid"],
            help="OID of 'custom-locations' app",
        )
        c.argument(
            "skip_ssl_verification",
            action="store_true",
            help="Skip SSL verification for any cluster connection.",
        )

    with self.argument_context("connectedk8s disable-features") as c:
        c.argument(
            "cluster_name",
            options_list=["--name", "-n"],
            id_part="name",
            help="The name of the connected cluster.",
        )
        c.argument(
            "kube_config",
            options_list=["--kube-config"],
            help="Path to the kube config file.",
        )
        c.argument(
            "kube_context",
            options_list=["--kube-context"],
            help="Kubconfig context from current machine.",
        )
        c.argument(
            "features",
            features_types,
            options_list=["--features"],
            help="Space-separated list of features you want to disable.",
        )
        c.argument(
            "skip_ssl_verification",
            action="store_true",
            help="Skip SSL verification for any cluster connection.",
        )
        c.argument(
            "yes",
            options_list=["--yes", "-y"],
            help="Do not prompt for confirmation.",
            action="store_true",
        )

    with self.argument_context("connectedk8s list") as c:
        pass

    with self.argument_context("connectedk8s show") as c:
        c.argument(
            "cluster_name",
            options_list=["--name", "-n"],
            id_part="name",
            help="The name of the connected cluster.",
        )

    with self.argument_context("connectedk8s delete") as c:
        c.argument(
            "cluster_name",
            options_list=["--name", "-n"],
            id_part="name",
            help="The name of the connected cluster.",
        )
        c.argument(
            "kube_config",
            options_list=["--kube-config"],
            help="Path to the kube config file.",
        )
        c.argument(
            "kube_context",
            options_list=["--kube-context"],
            help="Kubconfig context from current machine.",
        )
        c.argument(
            "force_delete",
            options_list=["--force"],
            help="Force delete to remove all azure-arc resources from the cluster.",
            action="store_true",
        )
        c.argument(
            "skip_ssl_verification",
            action="store_true",
            help="Skip SSL verification for any cluster connection.",
        )
        c.argument(
            "yes",
            options_list=["--yes", "-y"],
            help="Do not prompt for confirmation.",
            action="store_true",
        )

    with self.argument_context("connectedk8s proxy") as c:
        c.argument(
            "cluster_name",
            options_list=["--name", "-n"],
            id_part="name",
            help="The name of the connected cluster.",
        )
        c.argument(
            "token",
            options_list=["--token"],
            help="Service account token to use to authenticate to the kubernetes cluster.",
        )
        c.argument(
            "context_name",
            options_list=["--kube-context"],
            help="If specified, overwrite the default context name.",
        )
        c.argument(
            "path",
            options_list=["--file", "-f"],
            type=file_type,
            completer=FilesCompleter(),  # type: ignore[no-untyped-call]
            default=os.path.join(os.path.expanduser("~"), ".kube", "config"),
            help="Kubernetes configuration file to update. If not provided, updates the file '~/.kube/config'. Use '-' to print YAML to stdout instead.",
        )
        c.argument(
            "api_server_port",
            options_list=["--port"],
            help="Port used for accessing connected cluster.",
        )

    with self.argument_context("connectedk8s troubleshoot") as c:
        c.argument("tags", tags_type)
        c.argument(
            "cluster_name",
            options_list=["--name", "-n"],
            help="The name of the connected cluster.",
        )
        c.argument(
            "kube_config",
            options_list=["--kube-config"],
            help="Path to the kube config file.",
        )
        c.argument(
            "kube_context",
            options_list=["--kube-context"],
            help="Kubeconfig context from current machine.",
        )
        c.argument(
            "skip_ssl_verification",
            action="store_true",
            help="Skip SSL verification for any cluster connection.",
        )
