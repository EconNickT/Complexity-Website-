---
title: Did the United–Continental merger *hurt consumers?*
summary: A difference-in-differences analysis of 13.7 million fare observations, weighing firm and consumer welfare. Fares rose as the market recovered from the recession, but the merger itself does not appear to have harmed consumers.
date: 2026-09-29
category: Working paper
ticker: UCM
tags:
  - Econometrics
  - Industrial organization
originalUrl: https://complexityinsights.substack.com/p/did-the-united-continental-merger
aiUse:
cover: /images/writings/did-the-united-continental-merger/cover.svg
coverAlt: Route map of the United and Continental hub networks joined by the 2010 merger.
stat:
  value: 13.7M
  label: observations in the difference-in-differences panel
draft: false
---
## Economic Welfare Implications

The airline industry is famous for being an industry where the major players (the big four) clearly engage in parallel pricing/tacit collusion. This follow-the-leader mechanic of the airline market is clear when one airline raises prices shortly after the others follow suit, and when others begin to offer certain perks, it will not take long for the others to begin offering the same perks. Sometimes this leads to actual collusion as in the famous case of the American Airlines CEO’s call to the Braniff Airlines CEO in 1982 where the AA CEO suggests that if BA raises their prices by 20% AA will follow. This means that the airline industry is susceptible to interdependent and coordinated pricing. Therefore, consolidation in the airline industry should be scrutinized to the fullest extent to ensure overall market welfare is only improved.

We will analyze the welfare of the merging firms and consumer welfare. The merger closed in October 2010 and Continental was fully integrated on March 3rd 2012. This means we have a large amount of post-merger data we can analyze to determine the welfare implications of the merger. There were many of the arguments of critics of the merger voicing desire to challenge the merger. The critics pointing out, the airline industry has a very high barriers to entry, due to aircraft costing hundreds of millions of dollars, on top of the limited landing/terminal availability and expensive labor markets. Below we test these theories.

## Firm Welfare

The airline industry was going through an extremely tumultuous time in the 2000s. With consumer travel slumps due to fears after the 9/11 attacks, litigation due to United being one of the hijacked airlines, and finally, due to the massive recession in 2007-2009 which resulted in a sharp decrease in leisure and business travel. The industry and more specifically United was financially unstable. All of these factors combined led United to seek opportunities that shored up their financial future.

After the integration the firm scaled down duplicate background roles. This comes in the form of HR, technical departments, non-airport customer service roles etc. Before the merger the combined firms had 30,836 employees filling these roles (according to each firm’s respective 10-K). Two years post-merger these roles were reduced to 14,611, this is a 52.6% decrease in headcount - quite significant. Other positions such as pilot and flight attendant headcounts mostly stayed the same. This was unexpected because during the merger, the firms still took shipments of new aircraft. This indicates improved labor efficiency per flight.

There were significant efficiencies gained from combining capital. Continental was an ideal acquisition for United since CO’s entire national fleet consisted of Boeing Aircraft. Both firms also had almost identical regional jet profiles, mostly using Embraer jets. This fits perfectly into United’s existing aircraft stock, ultimately leading to decreased maintenance costs related to parts, maintenance training, etc. Both airlines are also hub and spoke airlines. With Continental’s and United maintaining non-overlapping hubs in different parts of the country. This creates a robust network effect. The firm can offer more options to consumers and increase the number of connections available.

And finally a strong motivation of the merger was financial incentives. United was going through significant financial turmoil in the 2000’s. There was increased litigation risks due to two of their aircraft being hijacked on 9/11, the recession hit the entire industry hard, but especially United, due the collapse of Lehman brothers, the company lost an additional $124 million that was tied up in oil futures. After the merger, load factors increased. Revenue per available seat mile increased by 2 cents while cost per available seat mile increased by only 1.87 cents. Post-merger profit margins were above United’s pre-merger but below Continentals, so United achieved its goal of strengthening and stabilizing its business.

## Consumer Welfare

The airline industry has a low theoretical maximum number of firms that could operate in the market. Expensive aircraft, limited landing slots, and immense regulatory costs lead to large barriers to entry. Because of this, mergers and acquisitions in the airline industry could have significant long-term impact on consumer welfare. Airline mergers have historically drawn relatively light intervention and few were successfully blocked until the JetBlue-Spirit merger proposal. This lack of serious scrutiny due to the precedents could lead to some potential breach in merger guidelines going unaddressed. Particularly guidelines 1, 2, and 3. The airline market is notorious for engaging in follow-the-leader behavior. So any reduction in significant competition could lead to serious harmful repercussions for consumers.

First it is important to note, since this merger occurred as the economy was coming out of a major recession. The recovery led to some consumers reentering the market, and inflationary changes, going from recessionary imposed deflation to inflation of 3.15% within a span of two years (FRED). There are a few important metrics to determine changes in consumer welfare. Looking at competition for customers, consumer choice, and price effects, we can determine relative welfare changes.

Airport market competition reduced somewhat significantly as a natural consequence of the 2nd and 4th largest airlines merging. 454 airports went from four airlines to three and 120 went from three to just two. Ultimately more than a thousand airports lost a service provider, while fewer than 200 airports gained one. Because airlines are prone to various levels of collusion, this is a problem leading to increased perceived odds of increased prices.

The combined firm also gained control over a robust set of hub airports that carry significant passenger traffic. Most of the nation is now accessible to these hub airports. This increases the amount of flight possibilities for flyers. While reducing the number of layovers and out of network flight connections needed. Problems could arise post-merger from some of these hubs due to the combined firm controlling significant airport landing spots in large markets like Chicago and Houston. And if United had not divested from Newark they would control 73% of landing spots.

![Stata regression output: log itinerary fare regressed on a post-merger indicator, a United/Continental route indicator, their interaction, log distance, a round-trip dummy and year fixed effects, with robust standard errors, on 13,730,428 observations.](/images/writings/did-the-united-continental-merger/figure-1-stata-regression.webp)
*Figure 1. STATA regression output.*

We used the Bureau of Transportation statistics DB1B data that takes a sample of 10% of all annual ticket sales. Since ticket demand is highly cyclical we only used the first quarter sales. We regressed the log of itinerary fare on a post-merger indicator, a United/Continental-route indicator, their interaction, flight distance, a round-trip dummy, and year fixed effects.

United_continental was a dummy variable equal to one if either airline flew to that airport and zero if either airline did not. Post_united_continental was an interaction term looking at specific effects of the merger on those airlines routes. And all prices are relative to other airlines.

We got statistically significant results with very impressive t values. Our post-merger prices increased approximately 21.5%. And flights that were serviced by United and Continental pre-merger fares were 6.4% higher than average but post-merger they only increased by 1.6%. Now it is important to note that due to the market coming out of the recession and oil prices doubling in the early 2010’s there was significant market turbulence.

Overall the market turned out to be more robust than originally assumed. Organizations like the Government Accountability Office predicted it would take decades to replace continental and return competition to its pre-merger levels, while the big four are still the largest firms, this proved to be wrong. While the fare prices did increase after the merger this was largely due to the market rebounding. Since approximately 2015, fare prices have held relatively steady. This is largely due to industry mavericks increasing in market share. Whenever firms like Spirit enters, fares significantly decrease. The merger does not appear to have harmed consumers once recession recovery and fuel effects are accounted for. And since United was in financial turmoil it may have been a good thing the firms merged. As it potentially saved a big player in the airlines industry from going under and further reducing competition.
