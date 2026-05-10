#!/usr/bin/env python3
import json, urllib.request

WEBHOOK = "https://agile-hope-production.up.railway.app/webhook/publish"
EMAIL   = "https://agile-hope-production.up.railway.app/webhook/send-email"
SECRET  = "2e8a142d25995d892ff9f4500029c0c5"

BODY_LONG = """**[COMPANY]** has executed one of the most significant transactions in European digital infrastructure this year, with a deal valued at **€X billion** that reshapes the competitive landscape across multiple markets.

The transaction covers assets spanning **Y megawatts** of operational capacity across six countries, with a development pipeline adding a further Z MW over the next 36 months. Occupancy across the portfolio stands at 91%, anchored by long-term agreements from investment-grade counterparties on triple-net lease structures with a weighted average lease expiry of 8.4 years.

## Why the structure matters

The deal structure — a combination of equity and vendor financing — preserves the acquirer's balance sheet flexibility while allowing the seller to crystallise value at a premium to book. Infrastructure funds with a 10-year horizon are the natural buyer class for assets of this profile: predictable cash flows, inflation linkage, and a development pipeline that provides NAV upside beyond the core yield.

At the implied enterprise value per megawatt, the transaction prices at a **23% premium** to the previous comparable transaction in the same geography, reflecting the scarcity value of permitted, grid-connected capacity in a market where new site development timelines have extended to 4–6 years.

**What to watch:** Whether the vendor exercises its option to participate in the development pipeline — and how the deal prices compares to the Aligned Data Centers $40B benchmark when adjusted for market and asset quality differences. The next comparable transaction in this market is expected within 12 months based on known fund realisation timelines."""

BODY_MEDIUM = """**[OPERATOR]** has announced a strategic review of its passive infrastructure portfolio, covering **2,800 tower structures** across its core markets, with a formal sale process expected to launch in Q3 2026.

The portfolio generates approximately **€180 million** in annual EBITDA at a 72% margin, implying an enterprise value of €1.8–2.2 billion at market tower multiples of 10–12x. Three infrastructure funds are understood to have been approached for early-stage conversations: Cellnex Telecom, Phoenix Tower International, and a sovereign wealth vehicle active in Northern European infrastructure.

The operator's rationale is consistent with the sector-wide trend toward passive infrastructure separation: proceeds will reduce net debt from 3.1x to approximately 2.4x EBITDA, improving the operator's cost of capital and freeing capital for active network investment in fibre and 5G densification.

**What to watch:** The final sale multiple relative to comparable recent transactions, and whether the buyer opts for a leaseback structure or seeks to grow the portfolio through third-party co-location — which would materially affect the long-term returns profile."""

editions = [
    {
        "edition_num": 8,
        "date": "2026-04-25",
        "articles": [
            {
                "beat": "Capital & Deals",
                "title": "Test E8: Infrastructure Fund Closes EUR 12B Pan-European DC Portfolio",
                "subtitle": "A fictional consortium acquires 18 data centres across six markets in the largest single-fund close of the year.",
                "body_md": BODY_LONG.replace("[COMPANY]", "Meridian Infrastructure Partners").replace("X billion", "12 billion").replace("Y megawatts", "420 megawatts").replace("Z MW", "280 MW"),
                "summary": "Meridian Infrastructure Partners closes a EUR 12B acquisition of 18 European data centres across six markets, anchored by hyperscaler leases on 10-year triple-net terms with 280 MW of development upside.",
                "bullets": [
                    "EUR 12B acquisition of 18 data centres — 420 MW operational IT load across DE, FR, NL, SE, DK, PL",
                    "Average occupancy 91%; hyperscaler anchor leases on 10-year triple-net terms",
                    "Implied EV/MW of EUR 17M — 23% premium to European market average of EUR 13-14M/MW",
                    "WALE of 8.4 years — at the long end of comparable European DC portfolios",
                    "TeleEurope retains 15% minority stake; Meridian has 5-year realisation mandate"
                ],
                "sources": [{"title": "Test Source", "url": "https://example.com/test"}],
                "thread_tags": ["dc-valuation-reset"]
            },
            {
                "beat": "Nordics",
                "title": "Test E8: Telia Divests Finnish Tower Portfolio for EUR 1.4B to Cellnex",
                "subtitle": "Sweden's Telia exits passive infrastructure in Finland as Cellnex extends its Nordic footprint to 8,200 towers.",
                "body_md": BODY_MEDIUM.replace("[OPERATOR]", "Telia Company").replace("2,800 tower structures", "3,400 Finnish tower structures").replace("EUR 180 million", "EUR 210 million").replace("EUR 1.8-2.2 billion", "EUR 1.4 billion"),
                "summary": "Telia completes its Nordic passive infrastructure exit by selling 3,400 Finnish towers to Cellnex for EUR 1.4B, completing a EUR 4.2B total disposal programme and extending Cellnex's Nordic footprint to 8,200 sites.",
                "bullets": [
                    "EUR 1.4B sale of 3,400 Finnish towers to Cellnex — implied EUR 412K per tower",
                    "15-year master lease: Telia retains antenna access on all 3,400 structures",
                    "Cellnex Nordic portfolio reaches 8,200 towers across SE, DK, FI",
                    "Telia total passive infrastructure disposal programme: EUR 4.2B across four markets",
                    "Telia net debt target: 2.0x EBITDA; share buyback to follow"
                ],
                "sources": [{"title": "Test Source", "url": "https://example.com/test"}],
                "thread_tags": ["nordics-infra-advantage"]
            },
            {
                "beat": "UK & Ireland",
                "title": "Test E8: Ofcom Opens Spectrum Review That Could Reshape UK 5G Economics",
                "subtitle": "Proposed 700 MHz reallocation would cut BT's coverage advantage and force GBP 800M in network investment.",
                "body_md": "**Ofcom** has opened a formal consultation on reallocation of the **700 MHz** spectrum band in the UK, proposing to cap any single operator's holdings at **2x10 MHz** and redistribute surplus spectrum via a new auction. The review directly affects **BT/EE**, which holds 2x20 MHz in the band — double the proposed cap — and would be required to surrender half its 700 MHz holdings subject to final determination.\n\nThe 700 MHz band is the most valuable sub-GHz spectrum for rural 5G coverage, penetrating buildings and propagating over long distances at a fraction of the cost of higher-frequency alternatives. Ofcom's analysis estimates BT/EE currently achieves **23% better indoor 5G coverage** than its nearest competitor using its 700 MHz advantage — an asymmetry Ofcom considers structurally anti-competitive.\n\n## Financial implications\n\nForcing a 700 MHz reallocation would require BT/EE to invest an estimated **GBP 800 million** in densification using 3.5 GHz small cells to maintain equivalent coverage performance. VMO2 and Three UK would be the primary beneficiaries, each receiving spectrum that reduces their rural coverage gap by an estimated 15-18 percentage points.\n\nThe consultation runs until **September 30, 2026**, with a final statement expected in Q1 2027. Any reallocation would take effect no earlier than 2028, giving BT time to plan its network investment response.\n\n**What to watch:** BT's response to the consultation — expected to contest the coverage asymmetry analysis — and whether VMO2 and Three UK file a joint submission to accelerate the timeline ahead of their own investment planning cycles.",
                "summary": "Ofcom's 700 MHz spectrum review proposes capping BT/EE at half its current holding, potentially forcing GBP 800M in network investment and redistributing rural 5G coverage advantage to VMO2 and Three UK.",
                "bullets": [
                    "Ofcom proposes 2x10 MHz cap on 700 MHz — BT/EE currently holds 2x20 MHz",
                    "BT/EE 700 MHz advantage: 23% better indoor 5G coverage than nearest competitor",
                    "Estimated GBP 800M BT densification investment required post-reallocation",
                    "VMO2 and Three UK rural coverage gap: 15-18 percentage points behind BT/EE",
                    "Consultation closes September 30 2026; final statement expected Q1 2027"
                ],
                "sources": [{"title": "Test Source", "url": "https://example.com/test"}],
                "thread_tags": ["uk-ai-energy-gap"]
            },
            {
                "beat": "Energy & Power",
                "title": "Test E8: Germany Approves First Commercial SMR Site at Former Nuclear Plant",
                "subtitle": "RWE and NuScale win planning permission for a 462 MW modular reactor at Gundremmingen — Europe's first commercial SMR approval.",
                "body_md": "**RWE** and **NuScale Power** have received planning permission from the German federal nuclear authority for a **462 megawatt** small modular reactor at the Gundremmingen site in Bavaria — the first commercial SMR approval in Europe.\n\nThe approval reverses a decade of German nuclear policy. The coalition government's 2025 energy security review concluded that SMR technology — factory-manufactured, passively safe, and modular — addressed the safety objections that underpinned the original phase-out. Gundremmingen's existing grid connections and infrastructure reduce greenfield development cost by an estimated **EUR 800 million**.\n\n## The data centre driver\n\nRWE has pre-signed a **15-year corporate PPA** with an unnamed hyperscaler for 380 MW of the plant's output — 82% of capacity — at a fixed price of **EUR 68 per MWh**. This is 23% below the current German baseload forward curve, providing long-term energy cost certainty that grid power cannot match.\n\nConstruction begins Q2 2027, with first power targeted for **2031**. Total project cost is **EUR 3.8 billion**, with RWE holding 60% and NuScale 40%.\n\n**What to watch:** Whether the German approval triggers applications at other former nuclear sites — Philippsburg and Brokdorf are the leading candidates — and whether EUR 68/MWh becomes the reference price for European SMR offtake agreements.",
                "summary": "RWE and NuScale win Germany's first commercial SMR planning approval at Gundremmingen, anchored by a 15-year hyperscaler PPA covering 82% of the 462 MW plant's output at EUR 68 per MWh.",
                "bullets": [
                    "462 MW NuScale VOYGR-6 SMR approved at Gundremmingen — first commercial SMR permit in Europe",
                    "15-year PPA with hyperscaler: 380 MW at EUR 68/MWh — 23% below German forward curve",
                    "Total project cost EUR 3.8B; RWE 60%, NuScale 40%; first power 2031",
                    "Existing Gundremmingen infrastructure saves estimated EUR 800M vs greenfield",
                    "Construction start Q2 2027; NuScale VOYGR-6 has 4-year build timeline"
                ],
                "sources": [{"title": "Test Source", "url": "https://example.com/test"}],
                "thread_tags": ["nuclear-ppas-data-centres"]
            },
            {
                "beat": "Connectivity",
                "title": "Test E8: Equinix and Orange Commit USD 1.1B to 400Tbps Transatlantic Cable",
                "subtitle": "AtlanticBridge-2 will cut London-New York latency to 59ms with RFS targeted Q3 2028.",
                "body_md": "**Equinix** and **Orange Marine** have announced a joint **USD 1.1 billion** investment in a new transatlantic submarine cable system connecting Bude (UK), Sopelana (Spain), and Tuckerton (New Jersey). The **400 terabit per second** system delivers a London-New York round-trip latency of **59 milliseconds** — a 12% improvement on current best-in-class systems.\n\nAtlanticBridge-2 is an open cable system with capacity sold on indefeasible right of use terms. Equinix has pre-sold **40% of capacity** across 15-year IRU agreements, primarily to European hyperscaler edge deployments requiring guaranteed transatlantic throughput. Ready for Service is targeted **Q3 2028**.\n\n## Why the UK landing matters\n\nBude in Cornwall was selected over alternative sites due to existing duct infrastructure and proximity to Equinix's Slough campus, reducing backhaul cost to London by an estimated **GBP 4.2 million annually**. The Sopelana landing provides Southern European and Middle Eastern traffic an alternative to the congested Marseille cluster.\n\nAt USD 1.1 billion for 400Tbps, AtlanticBridge-2 implies **USD 2.75M per terabit** — in line with recent comparable systems and below the pre-2020 average of USD 4.5M/Tbps, reflecting continuing reductions in repeater and fibre manufacturing costs.\n\n**What to watch:** Whether the 40% pre-sold capacity figure attracts additional buyers before cable-laying — the typical threshold for financial close — and whether Orange Marine's current construction backlog affects the Q3 2028 RFS target.",
                "summary": "Equinix and Orange Marine commit USD 1.1B to AtlanticBridge-2, a 400Tbps transatlantic cable landing in Bude and Sopelana with RFS Q3 2028 and 40% of capacity already pre-sold.",
                "bullets": [
                    "USD 1.1B investment in AtlanticBridge-2 — 400Tbps, 7,200km, RFS Q3 2028",
                    "London-New York round-trip latency: 59ms — 12% improvement on current best",
                    "40% of capacity pre-sold on 15-year IRUs to European hyperscaler edge deployments",
                    "Cost per terabit: USD 2.75M — below pre-2020 average of USD 4.5M/Tbps",
                    "UK landing at Bude saves GBP 4.2M/year in backhaul vs alternative sites"
                ],
                "sources": [{"title": "Test Source", "url": "https://example.com/test"}],
                "thread_tags": ["subsea-cable-disruption"]
            }
        ]
    },
    {
        "edition_num": 9,
        "date": "2026-05-02",
        "articles": [
            {
                "beat": "Western Europe",
                "title": "Test E9: Deutsche Telekom Launches EUR 4B Rural Fibre Programme with KfW",
                "subtitle": "Germany's largest state-backed fibre commitment targets 3.2 million underserved premises by 2030.",
                "body_md": "**Deutsche Telekom** and state development bank **KfW** have jointly announced a **EUR 4 billion** rural fibre programme targeting **3.2 million** underserved premises across Germany's eastern states and rural Bavarian municipalities by 2030. KfW will provide EUR 1.6 billion in subsidised financing at a blended rate of 2.1%, with the remainder funded by Deutsche Telekom's own balance sheet.\n\nThe programme covers 847 municipalities where commercial fibre build is uneconomic at current ARPU levels — typically communities with fewer than 2,000 premises and take-up rates below 30% without subsidy. Deutsche Telekom has secured wholesale access commitments from four alternative operators as a precondition of the KfW financing, ensuring the infrastructure will serve the open-access model mandated by the Federal Network Agency.\n\n## The economics of rural fibre\n\nAt EUR 1,250 per premises passed (the programme's implied unit cost), the German rural build sits in line with McKinsey's 2024 European benchmarks for sparse-geography fibre deployment. Deutsche Telekom's 2023 programme in comparable municipalities achieved 34% take-up at month 24 — generating EUR 28/month ARPU — implying a payback period of approximately 12 years at the subsidised financing cost.\n\nKfW's participation is the critical enabler: unsubsidised, the programme would require ARPU of EUR 42/month to justify the capital, materially above current market pricing.\n\n**What to watch:** Whether the Bundesnetzagentur's open-access conditions create the wholesale pricing tension that slowed the UK's altnet sector — and whether any of the four wholesale access operators use the programme infrastructure to launch consumer-facing FTTH products in competition with Deutsche Telekom's retail brand.",
                "summary": "Deutsche Telekom and KfW commit EUR 4B to connect 3.2 million underserved German premises by 2030, with subsidised KfW financing at 2.1% making previously uneconomic rural fibre viable.",
                "bullets": [
                    "EUR 4B rural fibre programme — 3.2M underserved German premises by 2030",
                    "KfW provides EUR 1.6B at 2.1% blended rate; remainder from Deutsche Telekom balance sheet",
                    "847 municipalities targeted — sub-2,000 premises, below 30% take-up without subsidy",
                    "Implied cost per premises passed: EUR 1,250 — in line with McKinsey 2024 European benchmark",
                    "Four wholesale access operators committed as condition of KfW financing"
                ],
                "sources": [{"title": "Test Source", "url": "https://example.com/test"}],
                "thread_tags": []
            },
            {
                "beat": "European Telecom",
                "title": "Test E9: EC Clears VodafoneThree with Eight Spectrum Remedies",
                "subtitle": "The final merger clearance imposes 2x10 MHz of 3.5 GHz divestitures and a 10-year MVNO access obligation.",
                "body_md": "The European Commission has granted final clearance for the **VodafoneThree** merger in the United Kingdom under Phase II merger review, subject to eight structural and behavioural remedies. The clearance confirms the UK's four-to-three mobile market consolidation — reducing operators from BT/EE, Vodafone, Three, and VMO2 to BT/EE, the merged VodafoneThree, and VMO2.\n\nThe remedies include: divestiture of **2x10 MHz** of 3.5 GHz spectrum to a new market entrant or existing operator; a **10-year MVNO access obligation** at regulated wholesale rates; commitment to maintain Three's existing network investment plan through 2030; and a rural coverage obligation requiring 95% geographic 5G coverage by 2028.\n\n## What the remedies mean in practice\n\nThe spectrum divestiture is the most structurally significant remedy. At 2x10 MHz of 3.5 GHz — the primary 5G mid-band — the divestiture creates a meaningful re-entry path for a fourth operator or strengthens an existing MVNO's network ambitions. Sky Mobile, MVNO with **7.4 million UK subscribers**, is understood to have expressed interest in acquiring the spectrum to support a network build.\n\nThe MVNO access obligation at regulated rates introduces a price ceiling on wholesale access that will constrain VodafoneThree's ability to use its network scale advantage to price competitors out of the market — the EC's primary concern during the review.\n\n**What to watch:** Who acquires the divested 3.5 GHz spectrum — the identity of the buyer will determine whether the UK market remains effectively three-player or whether a credible fourth network emerges by 2030.",
                "summary": "The EC clears VodafoneThree under eight remedies including 2x10 MHz of 3.5 GHz spectrum divestitures and a 10-year MVNO access obligation at regulated wholesale rates.",
                "bullets": [
                    "VodafoneThree cleared by EC — UK market moves from four to three mobile operators",
                    "2x10 MHz of 3.5 GHz spectrum divested — primary 5G mid-band, meaningful re-entry path",
                    "10-year MVNO access obligation at regulated wholesale rates",
                    "Rural 5G coverage obligation: 95% geographic coverage by 2028",
                    "Sky Mobile (7.4M UK subscribers) understood to be interested in divested spectrum"
                ],
                "sources": [{"title": "Test Source", "url": "https://example.com/test"}],
                "thread_tags": ["european-telecom-consolidation"]
            },
            {
                "beat": "Data Infrastructure",
                "title": "Test E9: Microsoft Commits USD 3.2B to Nordic AI Infrastructure Programme",
                "subtitle": "Sweden and Finland receive the largest single hyperscaler commitment in Nordic history, anchored by 500 MW of new data centre capacity.",
                "body_md": "**Microsoft** has announced a **USD 3.2 billion** investment programme in Nordic AI infrastructure, covering **500 megawatts** of new data centre capacity across Sweden (350 MW) and Finland (150 MW) to be built between 2026 and 2030. The programme includes a skills training commitment for **25,000 professionals** in AI and cloud operations and a procurement commitment to source **100% renewable energy** through Nordic hydropower and wind PPAs.\n\nThe Swedish component — centred on a new campus in Sandviken, Gavleborg County — takes advantage of the region's combination of low-cost hydroelectric power (approximately **EUR 35/MWh** on long-term contracts), cool climate reducing cooling costs by an estimated 40% versus Southern European equivalents, and proximity to Stockholm's financial sector fibre routes.\n\n## Why this matters for the Nordics\n\nMicrosoft's commitment is the largest single hyperscaler investment in the Nordic region and sets a new benchmark for the investment size the region can attract. It follows AWS's EUR 1.8 billion Denmark announcement in March and Google's EUR 1.1 billion Finland expansion in January — bringing total hyperscaler committed Nordic capex in 2026 to approximately **EUR 6.5 billion** in the first four months of the year.\n\nFor infrastructure investors, the signal is clear: the Nordics' structural advantage — power cost, grid stability, regulatory predictability — is translating into committed hyperscaler capex at a pace that will tighten data centre land and grid capacity within 36 months.\n\n**What to watch:** Whether the Swedish and Finnish grid operators can absorb 500 MW of new load without extending connection timelines beyond the 18-24 months currently quoted for permitted sites.",
                "summary": "Microsoft commits USD 3.2B to 500 MW of Nordic data centre capacity across Sweden and Finland, bringing total hyperscaler Nordic capex commitments in 2026 to approximately EUR 6.5B in the first four months.",
                "bullets": [
                    "USD 3.2B Microsoft Nordic programme — 350 MW Sweden, 150 MW Finland, 2026-2030",
                    "Swedish campus in Sandviken benefits from EUR 35/MWh hydropower and 40% cooling cost reduction",
                    "25,000 professionals to be trained in AI and cloud operations",
                    "Total 2026 Nordic hyperscaler capex commitments: EUR 6.5B in four months (AWS, Google, Microsoft)",
                    "100% renewable energy commitment via Nordic hydropower and wind PPAs"
                ],
                "sources": [{"title": "Test Source", "url": "https://example.com/test"}],
                "thread_tags": ["nordics-infra-advantage", "sea-dc-buildout"]
            },
            {
                "beat": "Capital & Deals",
                "title": "Test E9: Macquarie Raises EUR 8B for Fourth Digital Infrastructure Fund",
                "subtitle": "The close is the largest European digital infrastructure fund ever raised, targeting fibre, towers, and AI-ready data centres.",
                "body_md": "**Macquarie Asset Management** has held a final close of its fourth digital infrastructure fund at **EUR 8 billion** — the largest European digital infrastructure fund ever raised — exceeding its original EUR 6 billion target by 33%. The fund attracted commitments from **62 LPs** across 19 countries, with European pension funds (45%), North American endowments (28%), and Middle Eastern sovereign wealth (27%) as the primary investor categories.\n\nMacquarie Digital Infrastructure Fund IV will target investments across three asset classes: pan-European fibre networks (40% target allocation), tower portfolios in consolidating markets (35%), and AI-ready data centres with hyperscaler anchor tenants (25%). The fund has already deployed approximately **EUR 800 million** across two seed investments not yet disclosed publicly.\n\n## What EUR 8B of dry powder means for the market\n\nMacquarie's fund close is the largest single addition to European digital infrastructure dry powder since the sector's institutional emergence. Combined with Meridian's EUR 12B close (Edition 8) and three other funds in market, European digital infrastructure dry powder is estimated to have reached **EUR 35 billion** — a figure that exceeds the total deal value of all European digital infrastructure transactions in 2023 and 2024 combined.\n\nThe implication for asset pricing is direct: with this volume of capital competing for a limited universe of quality assets, the bid/ask spread on European fibre and tower assets has compressed to near zero. Sellers are achieving ask price or above on the majority of processes.\n\n**What to watch:** Whether Macquarie's 25% DC allocation leads it to compete for the EQT GlobalConnect portfolio (Edition 7) — where it would be bidding against Antin and potentially sovereign wealth — and how quickly the EUR 800M in seed investments is disclosed.",
                "summary": "Macquarie closes its fourth digital infrastructure fund at EUR 8B — a record for European digital infrastructure — bringing estimated total European digital infrastructure dry powder to EUR 35B.",
                "bullets": [
                    "Macquarie Digital Infrastructure Fund IV closes at EUR 8B — 33% above EUR 6B target",
                    "62 LPs across 19 countries; European pensions 45%, North American endowments 28%, ME sovereign 27%",
                    "Allocation: 40% fibre, 35% towers, 25% AI-ready data centres",
                    "EUR 800M already deployed in two undisclosed seed investments",
                    "Total European digital infrastructure dry powder estimated at EUR 35B — exceeds 2023-24 deal volume combined"
                ],
                "sources": [{"title": "Test Source", "url": "https://example.com/test"}],
                "thread_tags": ["dc-valuation-reset"]
            },
            {
                "beat": "Energy & Power",
                "title": "Test E9: National Grid Accelerates GBP 6B Grid Upgrade to Unlock Stranded DC Capacity",
                "subtitle": "A revised connection queue process will unblock 4.2 GW of data centre capacity stuck behind legacy industrial applicants.",
                "body_md": "**National Grid** has announced a **GBP 6 billion** accelerated transmission upgrade programme targeting the grid constraints that have blocked an estimated **4.2 gigawatts** of data centre capacity from connecting in England and Wales. The programme, approved by Ofgem under an accelerated regulatory framework, will deliver 14 new 400kV substations and 1,800km of transmission reinforcement between 2026 and 2031.\n\nCritically, National Grid has also revised its connection queue management process, introducing a **merit order system** that prioritises applicants with confirmed planning permission, proven financing, and near-term construction readiness over legacy industrial applications that have held queue positions for 5-8 years without progressing. The change is estimated to unblock **2.1 GW** of data centre connections within 24 months.\n\n## Why the queue reform matters more than the capex\n\nThe GBP 6 billion transmission investment addresses the physical infrastructure constraint. But the queue reform addresses the systemic failure that has left 4.2 GW of shovel-ready data centre projects unable to connect despite available transmission capacity in many areas. Under the legacy queue model, a 1985-vintage industrial applicant with no active development plans could hold a connection position ahead of a fully financed data centre project — an absurdity that the merit order reform directly resolves.\n\nFor data centre operators in the UK, the practical implication is a reduction in expected connection timelines from the current 6-8 years in constrained areas to approximately **3-4 years** for projects meeting the merit order criteria.\n\n**What to watch:** Whether Ofgem extends the merit order approach to distribution-level connections — where the same queue dysfunction exists at smaller scale — and how quickly the 2.1 GW of newly accessible capacity attracts confirmed investment commitments.",
                "summary": "National Grid's GBP 6B transmission upgrade and connection queue merit order reform will unblock 4.2 GW of stranded UK data centre capacity, cutting connection timelines from 6-8 years to approximately 3-4 years.",
                "bullets": [
                    "GBP 6B National Grid transmission upgrade — 14 new 400kV substations, 1,800km reinforcement",
                    "4.2 GW of data centre capacity currently blocked in England and Wales connection queue",
                    "New merit order system prioritises construction-ready applicants over legacy queue positions",
                    "2.1 GW of data centre connections estimated to unblock within 24 months",
                    "Expected connection timeline reduction: 6-8 years to 3-4 years for qualifying projects"
                ],
                "sources": [{"title": "Test Source", "url": "https://example.com/test"}],
                "thread_tags": ["uk-ai-energy-gap", "nuclear-ppas-data-centres"]
            }
        ]
    },
    {
        "edition_num": 10,
        "date": "2026-05-09",
        "articles": [
            {
                "beat": "Nordics",
                "title": "Test E10: EQT GlobalConnect Sale Attracts Seven Bidders at EUR 8B Floor",
                "subtitle": "The pan-Nordic fibre and data centre operator draws sovereign wealth, pension funds, and two infrastructure managers to first-round bids.",
                "body_md": "**EQT's** sale process for **GlobalConnect** has attracted seven first-round bids at or above the **EUR 8 billion** floor price set when Goldman Sachs launched the auction in April. Bidders include **Antin Infrastructure Partners**, two unnamed sovereign wealth funds, a Canadian pension consortium, and three infrastructure fund managers. Final bids are due in August 2026 with a targeted close before year-end.\n\nGlobalConnect's **244,000km fibre network**, 23 data centres, and 27 subsea cables across Denmark, Norway, Sweden, Germany, and Finland represent a rare integrated pan-Nordic digital infrastructure platform. The new Aland subsea cable (Sweden-Finland), scheduled for completion in Q3 2026, will be included in the portfolio.\n\n## Why seven bidders at EUR 8B\n\nThe breadth of interest reflects three converging factors. First, the GlobalConnect portfolio is among the last large-scale pan-Nordic infrastructure assets available — post-sale, the market will be fragmented across many smaller operators with no comparable integrated footprint. Second, Microsoft's USD 3.2B Nordic commitment (Edition 9) and the broader hyperscaler capex wave have validated the investment thesis for Nordic digital infrastructure at a moment when dry powder is at record levels. Third, the data centre component — 23 facilities with hyperscaler-adjacent demand — gives GlobalConnect a valuation premium over pure-play fibre or tower assets.\n\nAt EUR 8 billion, the implied valuation for the fibre network alone (stripping out estimated EUR 2B for DC and subsea) is approximately **EUR 25 per home passed** — a modest premium to recent comparable Nordic fibre transactions.\n\n**What to watch:** Whether the final bid exceeds EUR 10 billion as bidders compete for the last integrated Nordic platform — and whether EQT's preference for a single buyer holds or whether a consortium bid breaks the portfolio into components.",
                "summary": "EQT's GlobalConnect sale draws seven first-round bids at the EUR 8B floor from sovereign wealth, pensions, and infrastructure funds, with final bids due August 2026 for the pan-Nordic fibre, DC, and subsea platform.",
                "bullets": [
                    "Seven first-round bids at EUR 8B floor — Antin, two sovereign wealth funds, Canadian pension consortium, three infra managers",
                    "GlobalConnect: 244,000km fibre, 23 data centres, 27 subsea cables across DK, NO, SE, DE, FI",
                    "New Aland subsea cable (SE-FI) completing Q3 2026 included in sale perimeter",
                    "Implied fibre-only valuation: EUR 25 per home passed — modest premium to Nordic comparables",
                    "Final bids due August 2026; targeted close before year-end"
                ],
                "sources": [{"title": "Test Source", "url": "https://example.com/test"}],
                "thread_tags": ["nordics-infra-advantage", "dc-valuation-reset"]
            },
            {
                "beat": "Western Europe",
                "title": "Test E10: SFR Sale EC Filing Triggers Spectrum Remedy Negotiations",
                "subtitle": "The Bouygues-Free-Orange consortium files for EC clearance as spectrum remedy talks open on 700 MHz and 3.5 GHz redistribution.",
                "body_md": "The **Bouygues-Free-Orange** consortium has filed for European Commission merger clearance for its **EUR 20.35 billion** acquisition of SFR's core assets, triggering the formal Phase I review period. EC competition analysts are expected to issue a request for information within 10 working days, with a Phase I decision due by **August 14, 2026**. A Phase II review — widely anticipated given the four-to-three market structure change — would extend the timeline into early 2027.\n\nThe spectrum remedy negotiations are expected to centre on **700 MHz** and **3.5 GHz** redistribution. SFR currently holds 2x15 MHz of 700 MHz and 100 MHz of 3.5 GHz. The consortium's proposed asset allocation — Bouygues absorbs the B2B base and rural mobile network; B2C and spectrum split three ways — creates an asymmetric spectrum outcome that the EC is expected to review closely.\n\n## The remedy precedent from VodafoneThree\n\nThe EC's VodafoneThree clearance (Edition 9) — requiring 2x10 MHz of 3.5 GHz divestiture and a 10-year MVNO access obligation — sets the clearest precedent for what France can expect. Applied to the SFR transaction, an equivalent remedy would require the consortium to divest approximately 30-40 MHz of 3.5 GHz to a new entrant or MVNO, and potentially impose MVNO access at regulated rates.\n\nFor French MVNOs — **NOS**, **La Poste Mobile**, and **Auchan Telecom** are the most likely beneficiaries — a regulated access obligation would provide the wholesale pricing floor needed to sustain competitive retail offerings post-consolidation.\n\n**What to watch:** Whether the EC issues a Phase II decision — which would signal material competition concerns — and how quickly the spectrum remedy negotiations converge on a structure that satisfies the EC without materially diluting the transaction economics for the consortium.",
                "summary": "The Bouygues-Free-Orange consortium files for EC clearance on the EUR 20.35B SFR acquisition, with Phase I due August 14 and a widely expected Phase II extending into 2027 over spectrum remedy terms.",
                "bullets": [
                    "EC Phase I filing lodged — decision due August 14 2026; Phase II widely expected",
                    "SFR spectrum holdings: 2x15 MHz at 700 MHz and 100 MHz at 3.5 GHz subject to remedy",
                    "VodafoneThree precedent implies 30-40 MHz of 3.5 GHz divestiture and MVNO access obligation",
                    "NOS, La Poste Mobile, and Auchan Telecom identified as likely MVNO remedy beneficiaries",
                    "Transaction economics: EUR 20.35B enterprise value; exclusivity expires May 15 2026"
                ],
                "sources": [{"title": "Test Source", "url": "https://example.com/test"}],
                "thread_tags": ["european-telecom-consolidation"]
            },
            {
                "beat": "Data Infrastructure",
                "title": "Test E10: AWS Announces EUR 2.4B Irish Data Centre Expansion Over Three Years",
                "subtitle": "Dublin and Cork receive the largest hyperscaler single-country commitment in Ireland's history, adding 480 MW of capacity.",
                "body_md": "**Amazon Web Services** has announced a **EUR 2.4 billion** Irish data centre expansion programme covering **480 megawatts** of new capacity across two campuses in Dublin and Cork, to be built between 2026 and 2029. The announcement is the largest single hyperscaler commitment in Ireland and doubles AWS's operational Irish footprint from approximately 500 MW to nearly 1 GW.\n\nThe Cork campus — AWS's first significant presence outside the Dublin cluster — responds directly to EirGrid's 2025 moratorium extension on new Dublin data centre connections, which has effectively capped additional capacity in the capital until 2028. Cork's available grid capacity and the Irish government's designation of the South Cork Economic Corridor as a strategic energy zone provide the regulatory and infrastructure certainty AWS requires.\n\n## The EirGrid constraint and its ripple effects\n\nEirGrid's Dublin connection moratorium has forced a geographic diversification of Irish data centre investment that would not have occurred under unconstrained market conditions. AWS's Cork expansion will be followed — industry sources suggest — by at least two further hyperscaler commitments outside Dublin in 2026, as operators that had been queuing for Dublin connections redirect capital to Cork, Limerick, and Galway.\n\nFor Ireland as a whole, the EUR 2.4B commitment sustains the country's position as Europe's premier hyperscaler data centre destination despite the Dublin constraint. Ireland's combination of EU membership, English language, IDA Ireland incentive framework, and existing hyperscaler operational presence creates switching costs that no other European jurisdiction can easily replicate.\n\n**What to watch:** Whether EirGrid extends the Dublin moratorium beyond 2028 — the decision expected in H2 2026 — and whether the Cork campus triggers a broader South Ireland data centre cluster development comparable to Dublin's in the 2010s.",
                "summary": "AWS commits EUR 2.4B to 480 MW of Irish data centre capacity across Dublin and Cork, with the Cork campus a direct response to EirGrid's Dublin connection moratorium that has reshaped Irish hyperscaler geography.",
                "bullets": [
                    "EUR 2.4B AWS Irish expansion — 480 MW across Dublin and Cork, 2026-2029",
                    "Cork campus is AWS's first significant Irish presence outside Dublin cluster",
                    "EirGrid Dublin moratorium effective until 2028 — directly forced geographic diversification",
                    "AWS Irish footprint doubles from approx 500 MW to nearly 1 GW",
                    "At least two further hyperscaler commitments outside Dublin expected in 2026 from industry sources"
                ],
                "sources": [{"title": "Test Source", "url": "https://example.com/test"}],
                "thread_tags": ["sea-dc-buildout"]
            },
            {
                "beat": "Connectivity",
                "title": "Test E10: WorldLink Begins Construction of Iraq Terrestrial Segment",
                "subtitle": "The USD 700M Europe-Middle East bypass cable breaks ground in Basra as the Gulf conflict enters its seventh month.",
                "body_md": "The **WorldLink** consortium — comprising UAE-based **DIL Technology**, Iraqi operator **Tech 964**, and **Breeze Investments** — has commenced construction of the terrestrial segment of its USD 700 million hybrid cable system, breaking ground in Basra on the 1,200km overland route through Iraq toward the Turkish border.\n\nWorldLink's **900 terabit per second** system is designed to deliver Europe-Middle East connectivity with a round-trip latency consistently below 100 milliseconds — the threshold required for real-time AI inference and financial trading applications. The Basra groundbreaking marks the transition from planning to execution, seven months after the project was first announced.\n\n## Progress against the threat environment\n\nThe Gulf conflict that created demand for WorldLink has, paradoxically, complicated its construction. The Basra terrestrial route passes through Maysan and Diyala governorates where IRGC-aligned militia activity has disrupted infrastructure projects. The consortium has engaged **Iraqi federal security forces** for route protection, a model used by oil pipeline operators but unprecedented for telecommunications infrastructure.\n\nProgress on the submarine segment — connecting the UAE coast to the Iraqi territorial waters entry point — is proceeding independently of the terrestrial work. The submarine cable ship **Ile de Brehat** has been contracted by Orange Marine for the 340km undersea route, with the marine survey completed in March 2026.\n\n**What to watch:** Whether the terrestrial route security arrangement holds as the project moves into the more challenging central Iraq segment — and whether the completion of the marine survey accelerates the permitting timeline for the UAE submarine landing station.",
                "summary": "The WorldLink consortium breaks ground on the Basra terrestrial segment of its USD 700M Europe-Middle East bypass cable, marking the transition from planning to active construction with route security provided by Iraqi federal forces.",
                "bullets": [
                    "WorldLink terrestrial groundbreaking in Basra — 1,200km overland route through Iraq to Turkish border",
                    "900 Tbps design capacity; sub-100ms Europe-Middle East round-trip latency target",
                    "Iraqi federal security forces engaged for route protection through Maysan and Diyala",
                    "Submarine segment: 340km UAE-Iraq undersea route; Ile de Brehat contracted by Orange Marine",
                    "Marine survey completed March 2026; UAE landing station permitting in progress"
                ],
                "sources": [{"title": "Test Source", "url": "https://example.com/test"}],
                "thread_tags": ["subsea-cable-disruption"]
            },
            {
                "beat": "UK & Ireland",
                "title": "Test E10: CityFibre Raises GBP 1.1B as Altnet Consolidation Accelerates",
                "subtitle": "The UK's largest independent fibre builder secures its fourth institutional funding round as VMO2 acquires two sub-scale rivals.",
                "body_md": "**CityFibre** has closed a **GBP 1.1 billion** funding round led by **Goldman Sachs Asset Management** and **Mubadala Investment Company**, bringing total equity raised since its 2018 privatisation to **GBP 5.8 billion**. The funding will extend CityFibre's FTTP footprint from the current **4.7 million premises passed** to a target of **8 million** by the end of 2028, covering 70 UK towns and cities.\n\nThe raise comes as the UK altnet sector undergoes the consolidation wave that analysts have forecast since 2023. In the same week, **VMO2** announced the acquisition of Netomnia and Broadway Partners — two sub-scale regional altnets with a combined footprint of approximately 280,000 premises — for a combined consideration of GBP 340 million. Both transactions price at approximately **GBP 1,200 per premises passed**, the lower end of the current UK FTTP valuation range.\n\n## CityFibre's strategic position\n\nAt 4.7 million premises and GBP 5.8 billion raised, CityFibre occupies a unique position in the UK altnet market: large enough to achieve operational efficiency but not yet at the scale where further equity dilution becomes structurally prohibitive. Goldman's participation signals continued institutional confidence in the UK FTTP thesis despite rising competitive intensity from Openreach.\n\nThe Mubadala co-investment is notable: the Abu Dhabi sovereign wealth fund's entry into UK digital infrastructure follows its participation in the Aligned Data Centers consortium (Edition 6) and signals a broader Gulf capital rotation into UK infrastructure assets despite the energy cost headwinds flagged by the Stargate UK pause.\n\n**What to watch:** Whether CityFibre's 8 million premises target is revised upward as VMO2 and other consolidators remove sub-scale competitors — and whether the GBP 1,200/premises valuation for Netomnia and Broadway Partners becomes the distressed-asset pricing floor for the next wave of altnet failures.",
                "summary": "CityFibre closes GBP 1.1B led by Goldman and Mubadala to extend from 4.7M to 8M UK premises by 2028, as VMO2 acquires two sub-scale altnets at GBP 1,200 per premises passed.",
                "bullets": [
                    "CityFibre raises GBP 1.1B — Goldman Sachs AM and Mubadala lead; total equity raised GBP 5.8B",
                    "Target: 4.7M premises currently; 8M premises by end 2028 across 70 UK towns",
                    "VMO2 acquires Netomnia and Broadway Partners — 280,000 premises combined for GBP 340M",
                    "Implied VMO2 acquisition price: GBP 1,200 per premises passed — lower end of UK FTTP range",
                    "Mubadala UK digital infrastructure entry follows Aligned Data Centers consortium participation"
                ],
                "sources": [{"title": "Test Source", "url": "https://example.com/test"}],
                "thread_tags": ["uk-ai-energy-gap", "european-telecom-consolidation"]
            }
        ]
    }
]

def post(url, data=None):
    body = json.dumps(data).encode() if data else b""
    req = urllib.request.Request(url, data=body, headers={
        "Content-Type": "application/json",
        "x-webhook-secret": SECRET
    })
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

for edition in editions:
    print(f"\nPublishing edition {edition['edition_num']}...")
    result = post(WEBHOOK, edition)
    print(f"  {result}")
    print(f"  Sending email...")
    email = post(EMAIL)
    print(f"  {email}")

print("\nDone.")
