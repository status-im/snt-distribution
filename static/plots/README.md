# Plots Information
All interactive plots are created via the [Vega-Lite](https://vega.github.io/vega-lite/) or [Vega](https://vega.github.io/vega/) API. Both the derivative datasets and visualization specifications can be auto-generated via the [python script](../../munge_and_generate_plots.py) that is manually run before a PR is submitted. 

## plot data generation

In order for a Vega file to be rendered it will need to refer to a dataset. For most plots, the [base dataset](../data_csv) files will not be formatted appropriately even though all information is present within it. 

### Manual python script generation of derivative datasets
Currently, derivative datasets that are used for plots are generated in the python script mentioned above. 

If the python script is altered, it will need to be executed before any PR is accepted, so that all derivative files are updated before being hosted. This process will eventually be automated (hopefully). 

### Vega transform Grammar
Alternatively, [Vega](https://vega.github.io/vega/docs/transforms/) and [Vega-Lite](https://vega.github.io/vega-lite/docs/transform.html) have a transform grammar that allows for data transformations in the specification itself. This is more complicated but cleaner way to provide visualizations. 

If this is used, then it is recommended to use the large [`holders_munged.csv`](../../data_csv/holders_munged.csv) dataset as it has all base data combined into a single set. 