# SNT Distribution Analysis Repo
&#x1F534;&#x1F534;&#x1F534;

**DISCLAIMER: This repository is based on open source data and is not a complete identification of addresses and distribution. It serves as a best effort based on community gathered (and hoepfully reviewed) data. The blockchain data is simple, its identification and labeling is not, and is subject to being incorrect. Please report any incorrectness if you see it so that we can make the picture of the distribution more aligned with the reality.**

&#x1F534;&#x1F534;&#x1F534;

The purpose of this repository is to hold relevant information about the SNT token and its distribution among it's holders. It will also provide informational visualizations of the distribution across various identifiable user groups, as well as analysis articles that snapshot analysis at a given time.

The datasets are held in the [data_csv](data_csv) folder which contain the following updatable updatable files:
- [`holders.csv`](data_csv/holders.csv) - A file that snapshots holder account data. This file can be downloaded from [Etherscan](https://etherscan.io/token/0x744d70fdbe2ba4cf95131626614a1763df805b9e#balances) for up to 100,000 holders. 
- [`utility.csv`](data_csv/utility.csv) - A file that identifies various Status Network related smart contracts.
- [`exchanges.csv`](data/../data_csv/exchanges.csv) - A comma seperated value file that identifies various exchange addresses that may or may not store the SNT ERC20 token. 

Each of the following files has a specific format that will be enforced by the updating review process. This is to ensure auto-generated plots and derivative datasets are formed properly. The respetive formats will be detailed in the `data_csv` directory.

Data munging, derivative datasets, and vega-lite visualization files are generated via the [`munge_and_generate_plots.py`](munge_and_generate_plots.py) python script. Any time the above datasets are altered, **this file needs to be run on the local machine before submitting a PR** so that all derivative material is updated accordingly. This process will eventually be automated somehow, but for now it's still manual.

## Updating the base dataset
If you have information you'd like to add to the base dataset which derives all plots and analysis, please follow the guide in the [`data_csv`](data_csv) directory.

## Add a new plot based on the base dataset
If you would like to see a visualization that does not exist yet based on the available data, please follow the guide in the [`plots`](plots) directory.

---
## TODO
### Backend
- [ ] automate python script execution (or create seperate build process to create derivative material)
- [ ] abstract plot creation process and store in seperate directory
- [ ] abstract away utility functions used in python script
- [ ] re-format theme to be main visualization dashboard with associated research articles as secondary
### Content
- [ ] create main SNT visualization dashboard
- [ ] finish initial SNT Distribution Analys draft article
### Plots
- [ ] create plot - stale funds vs current
- [ ] create plot - order of magnitude plot
- [ ] create plot - change exchange bar to treemap
- [ ] create plot - treemap of distribution across Status