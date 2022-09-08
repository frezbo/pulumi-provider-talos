// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package talos

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Generate machine configuration for a Talos worker node.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-talos/sdk/go/talos"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			machineSecrets, err := talos.NewTalosMachineSecrets(ctx, "machineSecrets", nil)
//			if err != nil {
//				return err
//			}
//			talosconfig, err := talos.NewTalosClientConfiguration(ctx, "talosconfig", &talos.TalosClientConfigurationArgs{
//				ClusterName:    pulumi.String("example-cluster"),
//				MachineSecrets: machineSecrets.MachineSecrets,
//				Endpoints: pulumi.StringArray{
//					pulumi.String("10.5.0.2"),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = talos.NewTalosMachineConfigurationWorker(ctx, "machineconfigWorker", &talos.TalosMachineConfigurationWorkerArgs{
//				ClusterName:     talosconfig.ClusterName,
//				ClusterEndpoint: pulumi.String("https://cluster.local:6443"),
//				MachineSecrets:  machineSecrets.MachineSecrets,
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
type TalosMachineConfigurationWorker struct {
	pulumi.CustomResourceState

	// The endpoint of the Talos cluster
	ClusterEndpoint pulumi.StringOutput `pulumi:"clusterEndpoint"`
	// The name of the cluster in the generated config
	ClusterName pulumi.StringOutput `pulumi:"clusterName"`
	// config patches to apply to the generated config
	ConfigPatches pulumi.StringArrayOutput `pulumi:"configPatches"`
	// the desired machine config version to generate
	ConfigVersion pulumi.StringPtrOutput `pulumi:"configVersion"`
	// whether to render all machine configs adding the documentation for each field
	DocsEnabled pulumi.BoolPtrOutput `pulumi:"docsEnabled"`
	// whether to render all machine configs with the commented examples
	ExamplesEnabled pulumi.BoolPtrOutput `pulumi:"examplesEnabled"`
	// desired kubernetes version to run
	KubernetesVersion pulumi.StringPtrOutput `pulumi:"kubernetesVersion"`
	// the generated worker config
	MachineConfig pulumi.StringOutput `pulumi:"machineConfig"`
	// The machine secrets for the cluster
	MachineSecrets pulumi.StringOutput `pulumi:"machineSecrets"`
	// The version of Talos for which to generate configs
	TalosVersion pulumi.StringPtrOutput `pulumi:"talosVersion"`
}

// NewTalosMachineConfigurationWorker registers a new resource with the given unique name, arguments, and options.
func NewTalosMachineConfigurationWorker(ctx *pulumi.Context,
	name string, args *TalosMachineConfigurationWorkerArgs, opts ...pulumi.ResourceOption) (*TalosMachineConfigurationWorker, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ClusterEndpoint == nil {
		return nil, errors.New("invalid value for required argument 'ClusterEndpoint'")
	}
	if args.ClusterName == nil {
		return nil, errors.New("invalid value for required argument 'ClusterName'")
	}
	if args.MachineSecrets == nil {
		return nil, errors.New("invalid value for required argument 'MachineSecrets'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource TalosMachineConfigurationWorker
	err := ctx.RegisterResource("talos:index/talosMachineConfigurationWorker:TalosMachineConfigurationWorker", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTalosMachineConfigurationWorker gets an existing TalosMachineConfigurationWorker resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTalosMachineConfigurationWorker(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TalosMachineConfigurationWorkerState, opts ...pulumi.ResourceOption) (*TalosMachineConfigurationWorker, error) {
	var resource TalosMachineConfigurationWorker
	err := ctx.ReadResource("talos:index/talosMachineConfigurationWorker:TalosMachineConfigurationWorker", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TalosMachineConfigurationWorker resources.
type talosMachineConfigurationWorkerState struct {
	// The endpoint of the Talos cluster
	ClusterEndpoint *string `pulumi:"clusterEndpoint"`
	// The name of the cluster in the generated config
	ClusterName *string `pulumi:"clusterName"`
	// config patches to apply to the generated config
	ConfigPatches []string `pulumi:"configPatches"`
	// the desired machine config version to generate
	ConfigVersion *string `pulumi:"configVersion"`
	// whether to render all machine configs adding the documentation for each field
	DocsEnabled *bool `pulumi:"docsEnabled"`
	// whether to render all machine configs with the commented examples
	ExamplesEnabled *bool `pulumi:"examplesEnabled"`
	// desired kubernetes version to run
	KubernetesVersion *string `pulumi:"kubernetesVersion"`
	// the generated worker config
	MachineConfig *string `pulumi:"machineConfig"`
	// The machine secrets for the cluster
	MachineSecrets *string `pulumi:"machineSecrets"`
	// The version of Talos for which to generate configs
	TalosVersion *string `pulumi:"talosVersion"`
}

type TalosMachineConfigurationWorkerState struct {
	// The endpoint of the Talos cluster
	ClusterEndpoint pulumi.StringPtrInput
	// The name of the cluster in the generated config
	ClusterName pulumi.StringPtrInput
	// config patches to apply to the generated config
	ConfigPatches pulumi.StringArrayInput
	// the desired machine config version to generate
	ConfigVersion pulumi.StringPtrInput
	// whether to render all machine configs adding the documentation for each field
	DocsEnabled pulumi.BoolPtrInput
	// whether to render all machine configs with the commented examples
	ExamplesEnabled pulumi.BoolPtrInput
	// desired kubernetes version to run
	KubernetesVersion pulumi.StringPtrInput
	// the generated worker config
	MachineConfig pulumi.StringPtrInput
	// The machine secrets for the cluster
	MachineSecrets pulumi.StringPtrInput
	// The version of Talos for which to generate configs
	TalosVersion pulumi.StringPtrInput
}

func (TalosMachineConfigurationWorkerState) ElementType() reflect.Type {
	return reflect.TypeOf((*talosMachineConfigurationWorkerState)(nil)).Elem()
}

type talosMachineConfigurationWorkerArgs struct {
	// The endpoint of the Talos cluster
	ClusterEndpoint string `pulumi:"clusterEndpoint"`
	// The name of the cluster in the generated config
	ClusterName string `pulumi:"clusterName"`
	// config patches to apply to the generated config
	ConfigPatches []string `pulumi:"configPatches"`
	// the desired machine config version to generate
	ConfigVersion *string `pulumi:"configVersion"`
	// whether to render all machine configs adding the documentation for each field
	DocsEnabled *bool `pulumi:"docsEnabled"`
	// whether to render all machine configs with the commented examples
	ExamplesEnabled *bool `pulumi:"examplesEnabled"`
	// desired kubernetes version to run
	KubernetesVersion *string `pulumi:"kubernetesVersion"`
	// The machine secrets for the cluster
	MachineSecrets string `pulumi:"machineSecrets"`
	// The version of Talos for which to generate configs
	TalosVersion *string `pulumi:"talosVersion"`
}

// The set of arguments for constructing a TalosMachineConfigurationWorker resource.
type TalosMachineConfigurationWorkerArgs struct {
	// The endpoint of the Talos cluster
	ClusterEndpoint pulumi.StringInput
	// The name of the cluster in the generated config
	ClusterName pulumi.StringInput
	// config patches to apply to the generated config
	ConfigPatches pulumi.StringArrayInput
	// the desired machine config version to generate
	ConfigVersion pulumi.StringPtrInput
	// whether to render all machine configs adding the documentation for each field
	DocsEnabled pulumi.BoolPtrInput
	// whether to render all machine configs with the commented examples
	ExamplesEnabled pulumi.BoolPtrInput
	// desired kubernetes version to run
	KubernetesVersion pulumi.StringPtrInput
	// The machine secrets for the cluster
	MachineSecrets pulumi.StringInput
	// The version of Talos for which to generate configs
	TalosVersion pulumi.StringPtrInput
}

func (TalosMachineConfigurationWorkerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*talosMachineConfigurationWorkerArgs)(nil)).Elem()
}

type TalosMachineConfigurationWorkerInput interface {
	pulumi.Input

	ToTalosMachineConfigurationWorkerOutput() TalosMachineConfigurationWorkerOutput
	ToTalosMachineConfigurationWorkerOutputWithContext(ctx context.Context) TalosMachineConfigurationWorkerOutput
}

func (*TalosMachineConfigurationWorker) ElementType() reflect.Type {
	return reflect.TypeOf((**TalosMachineConfigurationWorker)(nil)).Elem()
}

func (i *TalosMachineConfigurationWorker) ToTalosMachineConfigurationWorkerOutput() TalosMachineConfigurationWorkerOutput {
	return i.ToTalosMachineConfigurationWorkerOutputWithContext(context.Background())
}

func (i *TalosMachineConfigurationWorker) ToTalosMachineConfigurationWorkerOutputWithContext(ctx context.Context) TalosMachineConfigurationWorkerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TalosMachineConfigurationWorkerOutput)
}

// TalosMachineConfigurationWorkerArrayInput is an input type that accepts TalosMachineConfigurationWorkerArray and TalosMachineConfigurationWorkerArrayOutput values.
// You can construct a concrete instance of `TalosMachineConfigurationWorkerArrayInput` via:
//
//	TalosMachineConfigurationWorkerArray{ TalosMachineConfigurationWorkerArgs{...} }
type TalosMachineConfigurationWorkerArrayInput interface {
	pulumi.Input

	ToTalosMachineConfigurationWorkerArrayOutput() TalosMachineConfigurationWorkerArrayOutput
	ToTalosMachineConfigurationWorkerArrayOutputWithContext(context.Context) TalosMachineConfigurationWorkerArrayOutput
}

type TalosMachineConfigurationWorkerArray []TalosMachineConfigurationWorkerInput

func (TalosMachineConfigurationWorkerArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*TalosMachineConfigurationWorker)(nil)).Elem()
}

func (i TalosMachineConfigurationWorkerArray) ToTalosMachineConfigurationWorkerArrayOutput() TalosMachineConfigurationWorkerArrayOutput {
	return i.ToTalosMachineConfigurationWorkerArrayOutputWithContext(context.Background())
}

func (i TalosMachineConfigurationWorkerArray) ToTalosMachineConfigurationWorkerArrayOutputWithContext(ctx context.Context) TalosMachineConfigurationWorkerArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TalosMachineConfigurationWorkerArrayOutput)
}

// TalosMachineConfigurationWorkerMapInput is an input type that accepts TalosMachineConfigurationWorkerMap and TalosMachineConfigurationWorkerMapOutput values.
// You can construct a concrete instance of `TalosMachineConfigurationWorkerMapInput` via:
//
//	TalosMachineConfigurationWorkerMap{ "key": TalosMachineConfigurationWorkerArgs{...} }
type TalosMachineConfigurationWorkerMapInput interface {
	pulumi.Input

	ToTalosMachineConfigurationWorkerMapOutput() TalosMachineConfigurationWorkerMapOutput
	ToTalosMachineConfigurationWorkerMapOutputWithContext(context.Context) TalosMachineConfigurationWorkerMapOutput
}

type TalosMachineConfigurationWorkerMap map[string]TalosMachineConfigurationWorkerInput

func (TalosMachineConfigurationWorkerMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*TalosMachineConfigurationWorker)(nil)).Elem()
}

func (i TalosMachineConfigurationWorkerMap) ToTalosMachineConfigurationWorkerMapOutput() TalosMachineConfigurationWorkerMapOutput {
	return i.ToTalosMachineConfigurationWorkerMapOutputWithContext(context.Background())
}

func (i TalosMachineConfigurationWorkerMap) ToTalosMachineConfigurationWorkerMapOutputWithContext(ctx context.Context) TalosMachineConfigurationWorkerMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TalosMachineConfigurationWorkerMapOutput)
}

type TalosMachineConfigurationWorkerOutput struct{ *pulumi.OutputState }

func (TalosMachineConfigurationWorkerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TalosMachineConfigurationWorker)(nil)).Elem()
}

func (o TalosMachineConfigurationWorkerOutput) ToTalosMachineConfigurationWorkerOutput() TalosMachineConfigurationWorkerOutput {
	return o
}

func (o TalosMachineConfigurationWorkerOutput) ToTalosMachineConfigurationWorkerOutputWithContext(ctx context.Context) TalosMachineConfigurationWorkerOutput {
	return o
}

// The endpoint of the Talos cluster
func (o TalosMachineConfigurationWorkerOutput) ClusterEndpoint() pulumi.StringOutput {
	return o.ApplyT(func(v *TalosMachineConfigurationWorker) pulumi.StringOutput { return v.ClusterEndpoint }).(pulumi.StringOutput)
}

// The name of the cluster in the generated config
func (o TalosMachineConfigurationWorkerOutput) ClusterName() pulumi.StringOutput {
	return o.ApplyT(func(v *TalosMachineConfigurationWorker) pulumi.StringOutput { return v.ClusterName }).(pulumi.StringOutput)
}

// config patches to apply to the generated config
func (o TalosMachineConfigurationWorkerOutput) ConfigPatches() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *TalosMachineConfigurationWorker) pulumi.StringArrayOutput { return v.ConfigPatches }).(pulumi.StringArrayOutput)
}

// the desired machine config version to generate
func (o TalosMachineConfigurationWorkerOutput) ConfigVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *TalosMachineConfigurationWorker) pulumi.StringPtrOutput { return v.ConfigVersion }).(pulumi.StringPtrOutput)
}

// whether to render all machine configs adding the documentation for each field
func (o TalosMachineConfigurationWorkerOutput) DocsEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *TalosMachineConfigurationWorker) pulumi.BoolPtrOutput { return v.DocsEnabled }).(pulumi.BoolPtrOutput)
}

// whether to render all machine configs with the commented examples
func (o TalosMachineConfigurationWorkerOutput) ExamplesEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *TalosMachineConfigurationWorker) pulumi.BoolPtrOutput { return v.ExamplesEnabled }).(pulumi.BoolPtrOutput)
}

// desired kubernetes version to run
func (o TalosMachineConfigurationWorkerOutput) KubernetesVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *TalosMachineConfigurationWorker) pulumi.StringPtrOutput { return v.KubernetesVersion }).(pulumi.StringPtrOutput)
}

// the generated worker config
func (o TalosMachineConfigurationWorkerOutput) MachineConfig() pulumi.StringOutput {
	return o.ApplyT(func(v *TalosMachineConfigurationWorker) pulumi.StringOutput { return v.MachineConfig }).(pulumi.StringOutput)
}

// The machine secrets for the cluster
func (o TalosMachineConfigurationWorkerOutput) MachineSecrets() pulumi.StringOutput {
	return o.ApplyT(func(v *TalosMachineConfigurationWorker) pulumi.StringOutput { return v.MachineSecrets }).(pulumi.StringOutput)
}

// The version of Talos for which to generate configs
func (o TalosMachineConfigurationWorkerOutput) TalosVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *TalosMachineConfigurationWorker) pulumi.StringPtrOutput { return v.TalosVersion }).(pulumi.StringPtrOutput)
}

type TalosMachineConfigurationWorkerArrayOutput struct{ *pulumi.OutputState }

func (TalosMachineConfigurationWorkerArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*TalosMachineConfigurationWorker)(nil)).Elem()
}

func (o TalosMachineConfigurationWorkerArrayOutput) ToTalosMachineConfigurationWorkerArrayOutput() TalosMachineConfigurationWorkerArrayOutput {
	return o
}

func (o TalosMachineConfigurationWorkerArrayOutput) ToTalosMachineConfigurationWorkerArrayOutputWithContext(ctx context.Context) TalosMachineConfigurationWorkerArrayOutput {
	return o
}

func (o TalosMachineConfigurationWorkerArrayOutput) Index(i pulumi.IntInput) TalosMachineConfigurationWorkerOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *TalosMachineConfigurationWorker {
		return vs[0].([]*TalosMachineConfigurationWorker)[vs[1].(int)]
	}).(TalosMachineConfigurationWorkerOutput)
}

type TalosMachineConfigurationWorkerMapOutput struct{ *pulumi.OutputState }

func (TalosMachineConfigurationWorkerMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*TalosMachineConfigurationWorker)(nil)).Elem()
}

func (o TalosMachineConfigurationWorkerMapOutput) ToTalosMachineConfigurationWorkerMapOutput() TalosMachineConfigurationWorkerMapOutput {
	return o
}

func (o TalosMachineConfigurationWorkerMapOutput) ToTalosMachineConfigurationWorkerMapOutputWithContext(ctx context.Context) TalosMachineConfigurationWorkerMapOutput {
	return o
}

func (o TalosMachineConfigurationWorkerMapOutput) MapIndex(k pulumi.StringInput) TalosMachineConfigurationWorkerOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *TalosMachineConfigurationWorker {
		return vs[0].(map[string]*TalosMachineConfigurationWorker)[vs[1].(string)]
	}).(TalosMachineConfigurationWorkerOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TalosMachineConfigurationWorkerInput)(nil)).Elem(), &TalosMachineConfigurationWorker{})
	pulumi.RegisterInputType(reflect.TypeOf((*TalosMachineConfigurationWorkerArrayInput)(nil)).Elem(), TalosMachineConfigurationWorkerArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*TalosMachineConfigurationWorkerMapInput)(nil)).Elem(), TalosMachineConfigurationWorkerMap{})
	pulumi.RegisterOutputType(TalosMachineConfigurationWorkerOutput{})
	pulumi.RegisterOutputType(TalosMachineConfigurationWorkerArrayOutput{})
	pulumi.RegisterOutputType(TalosMachineConfigurationWorkerMapOutput{})
}
