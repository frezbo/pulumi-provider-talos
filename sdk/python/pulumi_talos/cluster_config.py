# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ClusterConfigArgs', 'ClusterConfig']

@pulumi.input_type
class ClusterConfigArgs:
    def __init__(__self__, *,
                 cluster_endpoint: pulumi.Input[str],
                 cluster_name: pulumi.Input[str],
                 secrets: pulumi.Input['SecretsBundleArgs'],
                 additional_sans: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cluster_discovery: Optional[pulumi.Input[bool]] = None,
                 config_patches: Optional[pulumi.Input['ConfigPatchesArgs']] = None,
                 config_patches_control_plane: Optional[pulumi.Input['ConfigPatchesArgs']] = None,
                 config_patches_worker: Optional[pulumi.Input['ConfigPatchesArgs']] = None,
                 config_version: Optional[pulumi.Input['TalosMachineConfigVersionOutputArgs']] = None,
                 dns_domain: Optional[pulumi.Input[str]] = None,
                 docs: Optional[pulumi.Input[bool]] = None,
                 examples: Optional[pulumi.Input[bool]] = None,
                 install_disk: Optional[pulumi.Input[str]] = None,
                 install_image: Optional[pulumi.Input[str]] = None,
                 kubernetes_version: Optional[pulumi.Input[str]] = None,
                 kubespan: Optional[pulumi.Input[bool]] = None,
                 persist: Optional[pulumi.Input[bool]] = None,
                 registry_mirrors: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 talos_version: Optional[pulumi.Input['TalosVersionOutputArgs']] = None):
        """
        The set of arguments for constructing a ClusterConfig resource.
        :param pulumi.Input[str] cluster_endpoint: The cluster endpoint is the URL for the Kubernetes API. If you decide to use
               a control plane node, common in a single node control plane setup, use port 6443 as
               this is the port that the API server binds to on every control plane node. For an HA
               setup, usually involving a load balancer, use the IP and port of the load balancer.
        :param pulumi.Input[str] cluster_name: cluster name
        :param pulumi.Input['SecretsBundleArgs'] secrets: Talos Secrets Bundle
        :param pulumi.Input[Sequence[pulumi.Input[str]]] additional_sans: additional Subject-Alt-Names for the APIServer certificate
        :param pulumi.Input[bool] cluster_discovery: enable cluster discovery feature (default true)
        :param pulumi.Input['ConfigPatchesArgs'] config_patches: patch generated machineconfigs (applied to all node types)
        :param pulumi.Input['ConfigPatchesArgs'] config_patches_control_plane: patch generated machineconfigs (applied to 'controlplane' types)
        :param pulumi.Input['ConfigPatchesArgs'] config_patches_worker: patch generated machineconfigs (applied to 'worker' type)
        :param pulumi.Input['TalosMachineConfigVersionOutputArgs'] config_version: the desired machine config version to refer to
        :param pulumi.Input[str] dns_domain: the dns domain to use for cluster (default "cluster.local")
        :param pulumi.Input[bool] docs: renders all machine configs adding the documentation for each field (default true)
        :param pulumi.Input[bool] examples: renders all machine configs with the commented examples (default true)
        :param pulumi.Input[str] install_disk: the disk to install to (default "/dev/sda")
        :param pulumi.Input[str] install_image: the image used to perform an installation (default "ghcr.io/talos-systems/installer:v0.14.2")
        :param pulumi.Input[str] kubernetes_version: desired kubernetes version to run (default "1.23.4")
        :param pulumi.Input[bool] kubespan: enable kubespan feature
        :param pulumi.Input[bool] persist: the desired persist value for configs (default true)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] registry_mirrors: list of registry mirrors to use in format: <registry host>=<mirror URL>
        :param pulumi.Input['TalosVersionOutputArgs'] talos_version: the desired Talos version to refer to
        """
        pulumi.set(__self__, "cluster_endpoint", cluster_endpoint)
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "secrets", secrets)
        if additional_sans is not None:
            pulumi.set(__self__, "additional_sans", additional_sans)
        if cluster_discovery is None:
            cluster_discovery = True
        if cluster_discovery is not None:
            pulumi.set(__self__, "cluster_discovery", cluster_discovery)
        if config_patches is not None:
            pulumi.set(__self__, "config_patches", config_patches)
        if config_patches_control_plane is not None:
            pulumi.set(__self__, "config_patches_control_plane", config_patches_control_plane)
        if config_patches_worker is not None:
            pulumi.set(__self__, "config_patches_worker", config_patches_worker)
        if config_version is not None:
            pulumi.set(__self__, "config_version", config_version)
        if dns_domain is None:
            dns_domain = 'cluster.local'
        if dns_domain is not None:
            pulumi.set(__self__, "dns_domain", dns_domain)
        if docs is None:
            docs = True
        if docs is not None:
            pulumi.set(__self__, "docs", docs)
        if examples is None:
            examples = True
        if examples is not None:
            pulumi.set(__self__, "examples", examples)
        if install_disk is None:
            install_disk = '/dev/sda'
        if install_disk is not None:
            pulumi.set(__self__, "install_disk", install_disk)
        if install_image is None:
            install_image = 'ghcr.io/talos-systems/installer:v0.14.2'
        if install_image is not None:
            pulumi.set(__self__, "install_image", install_image)
        if kubernetes_version is None:
            kubernetes_version = '1.23.4'
        if kubernetes_version is not None:
            pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        if kubespan is not None:
            pulumi.set(__self__, "kubespan", kubespan)
        if persist is None:
            persist = True
        if persist is not None:
            pulumi.set(__self__, "persist", persist)
        if registry_mirrors is not None:
            pulumi.set(__self__, "registry_mirrors", registry_mirrors)
        if talos_version is not None:
            pulumi.set(__self__, "talos_version", talos_version)

    @property
    @pulumi.getter(name="clusterEndpoint")
    def cluster_endpoint(self) -> pulumi.Input[str]:
        """
        The cluster endpoint is the URL for the Kubernetes API. If you decide to use
        a control plane node, common in a single node control plane setup, use port 6443 as
        this is the port that the API server binds to on every control plane node. For an HA
        setup, usually involving a load balancer, use the IP and port of the load balancer.
        """
        return pulumi.get(self, "cluster_endpoint")

    @cluster_endpoint.setter
    def cluster_endpoint(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_endpoint", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        cluster name
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter
    def secrets(self) -> pulumi.Input['SecretsBundleArgs']:
        """
        Talos Secrets Bundle
        """
        return pulumi.get(self, "secrets")

    @secrets.setter
    def secrets(self, value: pulumi.Input['SecretsBundleArgs']):
        pulumi.set(self, "secrets", value)

    @property
    @pulumi.getter(name="additionalSans")
    def additional_sans(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        additional Subject-Alt-Names for the APIServer certificate
        """
        return pulumi.get(self, "additional_sans")

    @additional_sans.setter
    def additional_sans(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "additional_sans", value)

    @property
    @pulumi.getter(name="clusterDiscovery")
    def cluster_discovery(self) -> Optional[pulumi.Input[bool]]:
        """
        enable cluster discovery feature (default true)
        """
        return pulumi.get(self, "cluster_discovery")

    @cluster_discovery.setter
    def cluster_discovery(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cluster_discovery", value)

    @property
    @pulumi.getter(name="configPatches")
    def config_patches(self) -> Optional[pulumi.Input['ConfigPatchesArgs']]:
        """
        patch generated machineconfigs (applied to all node types)
        """
        return pulumi.get(self, "config_patches")

    @config_patches.setter
    def config_patches(self, value: Optional[pulumi.Input['ConfigPatchesArgs']]):
        pulumi.set(self, "config_patches", value)

    @property
    @pulumi.getter(name="configPatchesControlPlane")
    def config_patches_control_plane(self) -> Optional[pulumi.Input['ConfigPatchesArgs']]:
        """
        patch generated machineconfigs (applied to 'controlplane' types)
        """
        return pulumi.get(self, "config_patches_control_plane")

    @config_patches_control_plane.setter
    def config_patches_control_plane(self, value: Optional[pulumi.Input['ConfigPatchesArgs']]):
        pulumi.set(self, "config_patches_control_plane", value)

    @property
    @pulumi.getter(name="configPatchesWorker")
    def config_patches_worker(self) -> Optional[pulumi.Input['ConfigPatchesArgs']]:
        """
        patch generated machineconfigs (applied to 'worker' type)
        """
        return pulumi.get(self, "config_patches_worker")

    @config_patches_worker.setter
    def config_patches_worker(self, value: Optional[pulumi.Input['ConfigPatchesArgs']]):
        pulumi.set(self, "config_patches_worker", value)

    @property
    @pulumi.getter(name="configVersion")
    def config_version(self) -> Optional[pulumi.Input['TalosMachineConfigVersionOutputArgs']]:
        """
        the desired machine config version to refer to
        """
        return pulumi.get(self, "config_version")

    @config_version.setter
    def config_version(self, value: Optional[pulumi.Input['TalosMachineConfigVersionOutputArgs']]):
        pulumi.set(self, "config_version", value)

    @property
    @pulumi.getter(name="dnsDomain")
    def dns_domain(self) -> Optional[pulumi.Input[str]]:
        """
        the dns domain to use for cluster (default "cluster.local")
        """
        return pulumi.get(self, "dns_domain")

    @dns_domain.setter
    def dns_domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_domain", value)

    @property
    @pulumi.getter
    def docs(self) -> Optional[pulumi.Input[bool]]:
        """
        renders all machine configs adding the documentation for each field (default true)
        """
        return pulumi.get(self, "docs")

    @docs.setter
    def docs(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "docs", value)

    @property
    @pulumi.getter
    def examples(self) -> Optional[pulumi.Input[bool]]:
        """
        renders all machine configs with the commented examples (default true)
        """
        return pulumi.get(self, "examples")

    @examples.setter
    def examples(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "examples", value)

    @property
    @pulumi.getter(name="installDisk")
    def install_disk(self) -> Optional[pulumi.Input[str]]:
        """
        the disk to install to (default "/dev/sda")
        """
        return pulumi.get(self, "install_disk")

    @install_disk.setter
    def install_disk(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "install_disk", value)

    @property
    @pulumi.getter(name="installImage")
    def install_image(self) -> Optional[pulumi.Input[str]]:
        """
        the image used to perform an installation (default "ghcr.io/talos-systems/installer:v0.14.2")
        """
        return pulumi.get(self, "install_image")

    @install_image.setter
    def install_image(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "install_image", value)

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> Optional[pulumi.Input[str]]:
        """
        desired kubernetes version to run (default "1.23.4")
        """
        return pulumi.get(self, "kubernetes_version")

    @kubernetes_version.setter
    def kubernetes_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubernetes_version", value)

    @property
    @pulumi.getter
    def kubespan(self) -> Optional[pulumi.Input[bool]]:
        """
        enable kubespan feature
        """
        return pulumi.get(self, "kubespan")

    @kubespan.setter
    def kubespan(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "kubespan", value)

    @property
    @pulumi.getter
    def persist(self) -> Optional[pulumi.Input[bool]]:
        """
        the desired persist value for configs (default true)
        """
        return pulumi.get(self, "persist")

    @persist.setter
    def persist(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "persist", value)

    @property
    @pulumi.getter(name="registryMirrors")
    def registry_mirrors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        list of registry mirrors to use in format: <registry host>=<mirror URL>
        """
        return pulumi.get(self, "registry_mirrors")

    @registry_mirrors.setter
    def registry_mirrors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "registry_mirrors", value)

    @property
    @pulumi.getter(name="talosVersion")
    def talos_version(self) -> Optional[pulumi.Input['TalosVersionOutputArgs']]:
        """
        the desired Talos version to refer to
        """
        return pulumi.get(self, "talos_version")

    @talos_version.setter
    def talos_version(self, value: Optional[pulumi.Input['TalosVersionOutputArgs']]):
        pulumi.set(self, "talos_version", value)


class ClusterConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_sans: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cluster_discovery: Optional[pulumi.Input[bool]] = None,
                 cluster_endpoint: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 config_patches: Optional[pulumi.Input[pulumi.InputType['ConfigPatchesArgs']]] = None,
                 config_patches_control_plane: Optional[pulumi.Input[pulumi.InputType['ConfigPatchesArgs']]] = None,
                 config_patches_worker: Optional[pulumi.Input[pulumi.InputType['ConfigPatchesArgs']]] = None,
                 config_version: Optional[pulumi.Input[pulumi.InputType['TalosMachineConfigVersionOutputArgs']]] = None,
                 dns_domain: Optional[pulumi.Input[str]] = None,
                 docs: Optional[pulumi.Input[bool]] = None,
                 examples: Optional[pulumi.Input[bool]] = None,
                 install_disk: Optional[pulumi.Input[str]] = None,
                 install_image: Optional[pulumi.Input[str]] = None,
                 kubernetes_version: Optional[pulumi.Input[str]] = None,
                 kubespan: Optional[pulumi.Input[bool]] = None,
                 persist: Optional[pulumi.Input[bool]] = None,
                 registry_mirrors: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secrets: Optional[pulumi.Input[pulumi.InputType['SecretsBundleArgs']]] = None,
                 talos_version: Optional[pulumi.Input[pulumi.InputType['TalosVersionOutputArgs']]] = None,
                 __props__=None):
        """
        Talos cluster config resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] additional_sans: additional Subject-Alt-Names for the APIServer certificate
        :param pulumi.Input[bool] cluster_discovery: enable cluster discovery feature (default true)
        :param pulumi.Input[str] cluster_endpoint: The cluster endpoint is the URL for the Kubernetes API. If you decide to use
               a control plane node, common in a single node control plane setup, use port 6443 as
               this is the port that the API server binds to on every control plane node. For an HA
               setup, usually involving a load balancer, use the IP and port of the load balancer.
        :param pulumi.Input[str] cluster_name: cluster name
        :param pulumi.Input[pulumi.InputType['ConfigPatchesArgs']] config_patches: patch generated machineconfigs (applied to all node types)
        :param pulumi.Input[pulumi.InputType['ConfigPatchesArgs']] config_patches_control_plane: patch generated machineconfigs (applied to 'controlplane' types)
        :param pulumi.Input[pulumi.InputType['ConfigPatchesArgs']] config_patches_worker: patch generated machineconfigs (applied to 'worker' type)
        :param pulumi.Input[pulumi.InputType['TalosMachineConfigVersionOutputArgs']] config_version: the desired machine config version to refer to
        :param pulumi.Input[str] dns_domain: the dns domain to use for cluster (default "cluster.local")
        :param pulumi.Input[bool] docs: renders all machine configs adding the documentation for each field (default true)
        :param pulumi.Input[bool] examples: renders all machine configs with the commented examples (default true)
        :param pulumi.Input[str] install_disk: the disk to install to (default "/dev/sda")
        :param pulumi.Input[str] install_image: the image used to perform an installation (default "ghcr.io/talos-systems/installer:v0.14.2")
        :param pulumi.Input[str] kubernetes_version: desired kubernetes version to run (default "1.23.4")
        :param pulumi.Input[bool] kubespan: enable kubespan feature
        :param pulumi.Input[bool] persist: the desired persist value for configs (default true)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] registry_mirrors: list of registry mirrors to use in format: <registry host>=<mirror URL>
        :param pulumi.Input[pulumi.InputType['SecretsBundleArgs']] secrets: Talos Secrets Bundle
        :param pulumi.Input[pulumi.InputType['TalosVersionOutputArgs']] talos_version: the desired Talos version to refer to
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Talos cluster config resource

        :param str resource_name: The name of the resource.
        :param ClusterConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_sans: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cluster_discovery: Optional[pulumi.Input[bool]] = None,
                 cluster_endpoint: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 config_patches: Optional[pulumi.Input[pulumi.InputType['ConfigPatchesArgs']]] = None,
                 config_patches_control_plane: Optional[pulumi.Input[pulumi.InputType['ConfigPatchesArgs']]] = None,
                 config_patches_worker: Optional[pulumi.Input[pulumi.InputType['ConfigPatchesArgs']]] = None,
                 config_version: Optional[pulumi.Input[pulumi.InputType['TalosMachineConfigVersionOutputArgs']]] = None,
                 dns_domain: Optional[pulumi.Input[str]] = None,
                 docs: Optional[pulumi.Input[bool]] = None,
                 examples: Optional[pulumi.Input[bool]] = None,
                 install_disk: Optional[pulumi.Input[str]] = None,
                 install_image: Optional[pulumi.Input[str]] = None,
                 kubernetes_version: Optional[pulumi.Input[str]] = None,
                 kubespan: Optional[pulumi.Input[bool]] = None,
                 persist: Optional[pulumi.Input[bool]] = None,
                 registry_mirrors: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secrets: Optional[pulumi.Input[pulumi.InputType['SecretsBundleArgs']]] = None,
                 talos_version: Optional[pulumi.Input[pulumi.InputType['TalosVersionOutputArgs']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterConfigArgs.__new__(ClusterConfigArgs)

            __props__.__dict__["additional_sans"] = additional_sans
            if cluster_discovery is None:
                cluster_discovery = True
            __props__.__dict__["cluster_discovery"] = cluster_discovery
            if cluster_endpoint is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_endpoint'")
            __props__.__dict__["cluster_endpoint"] = cluster_endpoint
            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["config_patches"] = config_patches
            __props__.__dict__["config_patches_control_plane"] = config_patches_control_plane
            __props__.__dict__["config_patches_worker"] = config_patches_worker
            __props__.__dict__["config_version"] = config_version
            if dns_domain is None:
                dns_domain = 'cluster.local'
            __props__.__dict__["dns_domain"] = dns_domain
            if docs is None:
                docs = True
            __props__.__dict__["docs"] = docs
            if examples is None:
                examples = True
            __props__.__dict__["examples"] = examples
            if install_disk is None:
                install_disk = '/dev/sda'
            __props__.__dict__["install_disk"] = install_disk
            if install_image is None:
                install_image = 'ghcr.io/talos-systems/installer:v0.14.2'
            __props__.__dict__["install_image"] = install_image
            if kubernetes_version is None:
                kubernetes_version = '1.23.4'
            __props__.__dict__["kubernetes_version"] = kubernetes_version
            __props__.__dict__["kubespan"] = kubespan
            if persist is None:
                persist = True
            __props__.__dict__["persist"] = persist
            __props__.__dict__["registry_mirrors"] = registry_mirrors
            if secrets is None and not opts.urn:
                raise TypeError("Missing required property 'secrets'")
            __props__.__dict__["secrets"] = None if secrets is None else pulumi.Output.secret(secrets)
            __props__.__dict__["talos_version"] = talos_version
            __props__.__dict__["controlplane_config"] = None
            __props__.__dict__["talos_config"] = None
            __props__.__dict__["worker_config"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["secrets"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(ClusterConfig, __self__).__init__(
            'talos:index:clusterConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ClusterConfig':
        """
        Get an existing ClusterConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClusterConfigArgs.__new__(ClusterConfigArgs)

        __props__.__dict__["additional_sans"] = None
        __props__.__dict__["cluster_discovery"] = None
        __props__.__dict__["cluster_endpoint"] = None
        __props__.__dict__["cluster_name"] = None
        __props__.__dict__["config_patches"] = None
        __props__.__dict__["config_patches_control_plane"] = None
        __props__.__dict__["config_patches_worker"] = None
        __props__.__dict__["config_version"] = None
        __props__.__dict__["controlplane_config"] = None
        __props__.__dict__["dns_domain"] = None
        __props__.__dict__["docs"] = None
        __props__.__dict__["examples"] = None
        __props__.__dict__["install_disk"] = None
        __props__.__dict__["install_image"] = None
        __props__.__dict__["kubernetes_version"] = None
        __props__.__dict__["kubespan"] = None
        __props__.__dict__["persist"] = None
        __props__.__dict__["registry_mirrors"] = None
        __props__.__dict__["secrets"] = None
        __props__.__dict__["talos_config"] = None
        __props__.__dict__["talos_version"] = None
        __props__.__dict__["worker_config"] = None
        return ClusterConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalSans")
    def additional_sans(self) -> pulumi.Output[Sequence[str]]:
        """
        additional Subject-Alt-Names for the APIServer certificate
        """
        return pulumi.get(self, "additional_sans")

    @property
    @pulumi.getter(name="clusterDiscovery")
    def cluster_discovery(self) -> pulumi.Output[bool]:
        """
        cluster discovery feature
        """
        return pulumi.get(self, "cluster_discovery")

    @property
    @pulumi.getter(name="clusterEndpoint")
    def cluster_endpoint(self) -> pulumi.Output[str]:
        """
        The cluster endpoint
        """
        return pulumi.get(self, "cluster_endpoint")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        """
        cluster name
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="configPatches")
    def config_patches(self) -> pulumi.Output['outputs.ConfigPatches']:
        """
        generated machineconfigs (applied to all node types)
        """
        return pulumi.get(self, "config_patches")

    @property
    @pulumi.getter(name="configPatchesControlPlane")
    def config_patches_control_plane(self) -> pulumi.Output['outputs.ConfigPatches']:
        """
        generated machineconfigs (applied to 'controlplane' types)
        """
        return pulumi.get(self, "config_patches_control_plane")

    @property
    @pulumi.getter(name="configPatchesWorker")
    def config_patches_worker(self) -> pulumi.Output['outputs.ConfigPatches']:
        """
        generated machineconfigs (applied to 'worker' type)
        """
        return pulumi.get(self, "config_patches_worker")

    @property
    @pulumi.getter(name="configVersion")
    def config_version(self) -> pulumi.Output[str]:
        """
        the desired machine config version to refer to
        """
        return pulumi.get(self, "config_version")

    @property
    @pulumi.getter(name="controlplaneConfig")
    def controlplane_config(self) -> pulumi.Output[str]:
        """
        Talos Controlplane Config
        """
        return pulumi.get(self, "controlplane_config")

    @property
    @pulumi.getter(name="dnsDomain")
    def dns_domain(self) -> pulumi.Output[str]:
        """
        the dns domain to use for cluster
        """
        return pulumi.get(self, "dns_domain")

    @property
    @pulumi.getter
    def docs(self) -> pulumi.Output[bool]:
        """
        machine config documentation enabled
        """
        return pulumi.get(self, "docs")

    @property
    @pulumi.getter
    def examples(self) -> pulumi.Output[bool]:
        """
        machine config examples enabled
        """
        return pulumi.get(self, "examples")

    @property
    @pulumi.getter(name="installDisk")
    def install_disk(self) -> pulumi.Output[str]:
        """
        the disk to install to 
        """
        return pulumi.get(self, "install_disk")

    @property
    @pulumi.getter(name="installImage")
    def install_image(self) -> pulumi.Output[str]:
        """
        the image used to perform an installation
        """
        return pulumi.get(self, "install_image")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> pulumi.Output[str]:
        """
        desired kubernetes version to run
        """
        return pulumi.get(self, "kubernetes_version")

    @property
    @pulumi.getter
    def kubespan(self) -> pulumi.Output[bool]:
        """
        kubespan enabled
        """
        return pulumi.get(self, "kubespan")

    @property
    @pulumi.getter
    def persist(self) -> pulumi.Output[bool]:
        """
        persist value for configs
        """
        return pulumi.get(self, "persist")

    @property
    @pulumi.getter(name="registryMirrors")
    def registry_mirrors(self) -> pulumi.Output[Sequence[str]]:
        """
        list of registry mirrors
        """
        return pulumi.get(self, "registry_mirrors")

    @property
    @pulumi.getter
    def secrets(self) -> pulumi.Output['outputs.SecretsBundle']:
        """
        Talos Secrets Bundle
        """
        return pulumi.get(self, "secrets")

    @property
    @pulumi.getter(name="talosConfig")
    def talos_config(self) -> pulumi.Output[str]:
        """
        Talos Config
        """
        return pulumi.get(self, "talos_config")

    @property
    @pulumi.getter(name="talosVersion")
    def talos_version(self) -> pulumi.Output[str]:
        """
        the desired Talos version
        """
        return pulumi.get(self, "talos_version")

    @property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> pulumi.Output[str]:
        """
        Talos Worker Config
        """
        return pulumi.get(self, "worker_config")

