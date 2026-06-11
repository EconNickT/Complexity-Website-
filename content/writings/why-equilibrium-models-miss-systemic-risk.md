---
title: Why traditional models miss *systemic risk.*
subtitle: Standard equilibrium models assume independence. Real markets are interconnected networks where small shocks cascade. It's time for a new framework.
topic: Complexity economics
category: Essay
date: 2026-06-10
references:
  - "Arthur, W. B. (2021). *Foundations of complexity economics.* Nature Reviews Physics."
  - "Haldane, A. G. & May, R. M. (2011). *Systemic risk in banking ecosystems.* Nature 469, 351–355."
related:
  - tag: "Portfolio · № 001"
    title: "Banking deserts in America."
    href: /projects/banking-deserts-article.html
    desc: Spatial and network analysis of financial-access gaps.
---
The 2008 financial crisis caught most economists off guard. Standard risk models suggested everything was fine — right up until it wasn't. The problem wasn't just bad luck or isolated failures. It was a fundamental limitation in how we model economic systems.

Traditional economic models assume that markets operate in equilibrium, that agents are independent, and that risks follow predictable distributions. But real financial systems are **complex adaptive systems** — networks of interconnected institutions where small shocks can cascade into systemic crises.

## The equilibrium *assumption.*

Most economic models are built on the assumption that markets tend toward equilibrium — a stable state where supply equals demand and prices reflect all available information. This framework, rooted in physics analogies from the 19th century, gives us clean mathematical solutions and clear predictions.

> In economic theory, equilibrium is a state where all market forces are balanced. But financial markets are dynamic, constantly adapting systems where feedback loops dominate.

Financial markets don't actually operate this way. They're dynamic, where:

- **Feedback loops dominate.** Price changes trigger trading strategies that further move prices.
- **Regime shifts occur.** Market behavior can fundamentally change, not just oscillate around equilibrium.
- **Emergence matters.** System-level behaviors arise that can't be predicted from individual components.

## The independence *problem.*

Traditional risk models often assume that individual failures are independent events. If Bank A fails, standard models might calculate the probability of Bank B failing separately. This fundamentally misunderstands how financial systems work. Banks aren't isolated entities — they're nodes in a dense network of counterparty relationships.

## A complexity *perspective.*

Complexity economics offers a different framework. Instead of seeking equilibrium, it studies how systems evolve. Instead of assuming independence, it maps the networks that connect economic agents.

::: takeaway Key insight — phase transitions
**Systems can appear stable for long periods, then suddenly shift to a crisis state.** These aren't gradual changes — they're regime shifts where the rules of the game fundamentally change. Think of water freezing: nothing happens for a while, then everything happens at once.
:::

## Measuring systemic *risk.*

So how do we actually measure risk in complex financial networks? Several approaches have emerged from complexity research, particularly **network centrality measures**.

Network science provides tools to identify systemically important institutions:

- **Degree centrality.** How many counterparties does an institution have?
- **Betweenness centrality.** Does it serve as a critical bridge in the network?
- **Eigenvector centrality.** Is it connected to other important nodes?

```python
# Example: Calculating network centrality in Python
import networkx as nx

# Build financial network from exposure data
G = nx.from_pandas_edgelist(df, source='lender', target='borrower')

# Calculate centrality to identify systemic nodes
centrality = nx.eigenvector_centrality(G)

print(f"Systemic Risk Score: {centrality['Bank_A']:.3f}")
```

## *Conclusion.*

Traditional economic models aren't wrong — they're incomplete. They work well for analyzing marginal changes around stable equilibria. But they systematically miss the network effects, feedback loops, and emergent phenomena that drive systemic crises.

Complexity economics doesn't replace traditional models; it complements them. By treating financial systems as complex adaptive networks rather than collections of independent agents, we gain new tools for understanding and managing systemic risk.
