// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.talos
{
    [talosResourceType("talos:index:Random")]
    public partial class Random : Pulumi.CustomResource
    {
        [Output("length")]
        public Output<int> Length { get; private set; } = null!;

        [Output("result")]
        public Output<string> Result { get; private set; } = null!;


        /// <summary>
        /// Create a Random resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Random(string name, RandomArgs args, CustomResourceOptions? options = null)
            : base("talos:index:Random", name, args ?? new RandomArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Random(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("talos:index:Random", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Random resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Random Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Random(name, id, options);
        }
    }

    public sealed class RandomArgs : Pulumi.ResourceArgs
    {
        [Input("length", required: true)]
        public Input<int> Length { get; set; } = null!;

        public RandomArgs()
        {
        }
    }
}
