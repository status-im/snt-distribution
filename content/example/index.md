+++
title = "SNT Distribution Analysis: A visual article"
description = "This is a demo article."
date = "2020-10-15"
thumbnail = ""
categories = [
  "demo"
]
tags = []

vega = true

[distill]
  [distill.supportFiles]
  dtitle = "dtitle.html"
  appendix = "appendix.html"
  bibliography = "refs.bib"

  [[distill.authors]]
  author = "Corey Petty, PhD"
  authorURL = "http://coreypetty.com"

    [[distill.authors.affiliations]]
    name = "Status.im"
    url = "https://status.im"

+++


<d-abstract>
  <p>This is the ﬁrst paragraph of the article. Test a long — dash — here it is.</p>
</d-abstract>

This is an article that will discribe how SNT is distributed throughout its community. There was a previous analysis performed by the author {{<cite bib="pettyDistribution2017">}} directly after the Status.im ICO. This analysis attempted to look at who participated directly with the token distribution smart contract, and how they relate to each other. Since then, there has been a lot of development, a lot of movement of the SNT token, and adoption of several exchanges whcih drastically alters the distribution.

Here we will create various plots that show, in as much detail as publicly possible, who holds what as it stands today and review is it looks any different than a naive view, or the snapshot given by the author directly after the ICO.

Here we have the initial SNT distribution seperation. It is most easily seperated into three seperate sections which each require further analysis:

{{<vega id="viz-compare" spec="status-exchange-community-donut.vg.json" >}}

1. `Status`- contracts and accounts related to the Status Network. These don't necessarily need to be owned and operated by the Status Network GmbH, but certaily include those accounts.
2. `Exchanges` - accounts that have been identified {{<cite bib="etherscan,f13endgist">}} as accounts used by exchanges to store funds.
3. `Community` - accounts that cannot be attribute elsewhere that hold SNT, we consider this the "community."

An initial glance at this distribution combined with a naive understanding of the specifics of the Status related holdings will lead to the narrative that SNT is "centralized."

---
## Plots of Status related addresses

---
## Plots of Exchange addresses

{{<vega id="viz-exchange" spec="exchange-treemap.vg.json" >}}

---
## Plots of the Community distribution

Here we break up the community accounts into groups of "exponential value."{{<footnote>}}Note that this plot is not interactive, because it is a picture and I haven't had time to create the vega-lite version of it yet.{{</footnote>}} That is, we bucket each address based on what order of magnitude it is, as well as note how big that bucket is to show how many people control how much total value. 

![alt](static_exp_group.png)

## Bringing it all together to get a real picture

Now that we have more insight into each of the sub-groups explained earlier, we can start to form a more informed picture of the total distribution of SNT across its various holders.