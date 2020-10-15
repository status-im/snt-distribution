import pandas as pd
import numpy as np
import json

snt_stats = {
    'total_supply': 6804870174.8781,   
}

def lower(string):
    return string.lower()

def label_exp_group(value):
    labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
    for label in labels:
        if value <= 10**float(label):
            return label

# import known Status Addresses
status = pd.read_csv('./data_csv/utility.csv')
status['address'] = status['address'].apply(lower)
status['isStatus'] = True

# import holder accounts
holders = pd.read_csv('./data_csv/holders.csv')
holders['address'] = holders['address'].apply(lower)

# import exchange accounts
exchanges = pd.read_csv('./data_csv/exchanges.csv')
exchanges['address'] = exchanges['address'].apply(lower)
exchanges['isExchange'] = True

# merge into single dataset
holders = holders.merge(status, on="address", how="left")
holders = holders.merge(exchanges, on="address", how="left")

# clean up
holders['name_x'].fillna('', inplace=True)
holders['name_y'].fillna('', inplace=True)
holders['name'] = holders['name_x'] + holders['name_y']

# add additional columns
holders['percent'] = holders['balance'] / snt_stats['total_supply'] * 100
holders['exp_group'] = holders.balance.apply(label_exp_group)

# clean up NaN
holders['isContract'].fillna('False', inplace=True)
holders['isExchange'].fillna('False', inplace=True)
holders['isStatus'].fillna('False', inplace=True)

# filter out what we want
holders = holders[['address', 'balance', 'percent', 'exp_group', 'name', 'isContract', 'isExchange', 'isStatus']]

## Export holders CSV
holders.to_csv('./data_csv/holders_munged.csv')

##################### Plots creation
## Status vs Exchange vs Community
status_perc = holders[holders['isStatus'] == True].percent.sum()
exchange_perc = holders[holders['isExchange'] == True].percent.sum()
community_perc = 100 - status_perc - exchange_perc
vegaJson = {
  "$schema": "https://vega.github.io/schema/vega/v5.json",
  "description": "A basic bar chart example, with value labels shown upon mouse hover.",
  "width": 400,
  "height": 200,
  "padding": 5,

  "data": [
    {
      "name": "table",
      "values": [
        {"category": "Status", "amount": round(status_perc,2)},
        {"category": "Exchanges", "amount": round(exchange_perc,2)},
        {"category": "Community", "amount": round(community_perc,2)}
      ]
    }
  ],

  "signals": [
    {
      "name": "tooltip",
      "value": {},
      "on": [
        {"events": "rect:mouseover", "update": "datum"},
        {"events": "rect:mouseout",  "update": "{}"}
      ]
    }
  ],

  "scales": [
    {
      "name": "xscale",
      "type": "band",
      "domain": {"data": "table", "field": "category"},
      "range": "width",
      "padding": 0.05,
      "round": True
    },
    {
      "name": "yscale",
      "domain": {"data": "table", "field": "amount"},
      "nice": True,
      "range": "height"
    }
  ],

  "axes": [
    { "orient": "bottom", "scale": "xscale" },
    { "orient": "left", "scale": "yscale" }
  ],

  "marks": [
    {
      "type": "rect",
      "from": {"data":"table"},
      "encode": {
        "enter": {
          "x": {"scale": "xscale", "field": "category"},
          "width": {"scale": "xscale", "band": 1},
          "y": {"scale": "yscale", "field": "amount"},
          "y2": {"scale": "yscale", "value": 0}
        },
        "update": {
          "fill": {"value": "steelblue"}
        },
        "hover": {
          "fill": {"value": "red"}
        }
      }
    },
    {
      "type": "text",
      "encode": {
        "enter": {
          "align": {"value": "center"},
          "baseline": {"value": "bottom"},
          "fill": {"value": "#333"}
        },
        "update": {
          "x": {"scale": "xscale", "signal": "tooltip.category", "band": 0.5},
          "y": {"scale": "yscale", "signal": "tooltip.amount", "offset": -2},
          "text": {"signal": "tooltip.amount"},
          "fillOpacity": [
            {"test": "datum === tooltip", "value": 0},
            {"value": 1}
          ]
        }
      }
    }
  ]
}
with open('./static/status-exchange-community-donut.vg.json', 'w') as plot_file:
  json.dump(vegaJson, plot_file, ensure_ascii=False, indent=4, sort_keys=False)

## Exchange Treemap
exchangeBarJson = holders[holders['isExchange'] ==  True].groupby("name").sum().reset_index().reset_index().to_json(orient='records')
vegaJson ={
  "$schema": "https://vega.github.io/schema/vega/v5.json",
  "description": "A basic bar chart example, with value labels shown upon mouse hover.",
  "width": 400,
  "height": 200,
  "padding": 5,

  "data": [
    {
      "name": "table",
      "values": json.loads(exchangeBarJson)
    }
  ],

  "signals": [
    {
      "name": "tooltip",
      "value": {},
      "on": [
        {"events": "rect:mouseover", "update": "datum"},
        {"events": "rect:mouseout",  "update": "{}"}
      ]
    }
  ],

  "scales": [
    {
      "name": "xscale",
      "type": "band",
      "domain": {"data": "table", "field": "name"},
      "range": "width",
      "padding": 0.05,
      "round": True
    },
    {
      "name": "yscale",
      "domain": {"data": "table", "field": "percent"},
      "nice": True,
      "range": "height"
    }
  ],

  "axes": [
    { "orient": "bottom", "scale": "xscale" },
    { "orient": "left", "scale": "yscale" }
  ],

  "marks": [
    {
      "type": "rect",
      "from": {"data":"table"},
      "encode": {
        "enter": {
          "x": {"scale": "xscale", "field": "name"},
          "width": {"scale": "xscale", "band": 1},
          "y": {"scale": "yscale", "field": "percent"},
          "y2": {"scale": "yscale", "value": 0}
        },
        "update": {
          "fill": {"value": "steelblue"}
        },
        "hover": {
          "fill": {"value": "red"}
        }
      }
    },
    {
      "type": "text",
      "encode": {
        "enter": {
          "align": {"value": "center"},
          "baseline": {"value": "bottom"},
          "fill": {"value": "#333"}
        },
        "update": {
          "x": {"scale": "xscale", "signal": "tooltip.name", "band": 0.5},
          "y": {"scale": "yscale", "signal": "tooltip.percent", "offset": -2},
          "text": {"signal": "tooltip.percent"},
          "fillOpacity": [
            {"test": "datum === tooltip", "value": 0},
            {"value": 1}
          ]
        }
      }
    }
  ]
}
with open('static/exchange-treemap.vg.json', 'w') as treemapPlot:
  json.dump(vegaJson, treemapPlot, ensure_ascii=False, indent=4, sort_keys=False)




  