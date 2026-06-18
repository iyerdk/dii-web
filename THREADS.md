# DII Live Story Threads

Compact state file for the research agent. One entry per active thread.
Updated by the Thursday agent at the end of each edition run.

## Format per thread

```
## thread-id: kebab-case-id
Beat: [beat name]
Status: active | dormant | closed
Summary: [one sentence — current state with key figures]
Changelog:
- Edition N (YYYY-MM-DD): [what changed]
- Edition N (YYYY-MM-DD): [what changed]
```

`Summary` always reflects the current state. `Changelog` is append-only — never edit existing entries.

---

## thread-id: subsea-cable-disruption
Beat: Connectivity
Status: active
Summary: 17 cables disrupted via Red Sea corridor with no repair timeline; Iran formalised regulatory mandate requiring permits, annual fees, and exclusive maintenance rights for 7 Hormuz cables; Italy acquired TIM Sparkle (EC-cleared, €700M) — Rome takes direct state control of Mediterranean routing infrastructure; EU committed €347M to submarine cable security — €180M CEF backbone call for 13 Cable Projects of European Interest (June 30, 2026 deadline), €20M smart cable monitoring, €20M Baltic Sea emergency repair; Cable Security Toolbox released; GUIDE launched May 30 at Shangri-La Dialogue — 17 nations (7 EU member states + UK + Indo-Pacific partners) in first cross-regional military/intelligence information-sharing framework for undersea cable security; UK Defence Secretary disclosed tracking 3 Russian submarines surveying North Atlantic cable routes; FCC Second R&O (vote June 25, 2026) extends US cable landing licence regime to SLTE hardware — bars Covered List entities (Huawei/ZTE/HMN Technologies) from end-terminal equipment at US-landing cable points; three parallel governance layers now formed: EU Cable Security Toolbox (civilian), GUIDE (military/intelligence), FCC SLTE order (equipment); $10 trillion in daily financial transactions transit the named Hormuz cables.
Changelog:
- Edition 1 (2026-03-15): Gulf conflict disrupts 17 Red Sea submarine cables; traffic rerouted via Cape of Good Hope
- Edition 5 (2026-04-11): WorldLink announced — $700M UAE-Iraq hybrid cable, 900Tbps, sub-100ms Europe-ME latency, bypasses Suez corridor
- Edition 8 (2026-04-25): US-Iran conflict escalates to Hormuz; IRGC-linked media threatens 7 GCC submarine cables — dual-chokepoint closure with no historical precedent; no repair timeline while hostilities continue
- Edition 10 (2026-05-07): US Strategic Subsea Cables Act (S.3249, Shaheen/Barrasso) cleared Senate Foreign Relations Committee unanimously — 2 FTE State Dept cable diplomacy, sanctions mechanism, ICPC engagement; EU committed €20M to cable resilience stress-testing programme; Saudi stc announced $800M SilkLink 4,500km bypass cable with new landing stations
- Edition 12 (2026-05-21): Iran formalises Hormuz cable mandate via IRGC-affiliated Tasnim News Agency — permits, annual fees, exclusive maintenance rights for 7 cables; Falcon and GBI confirmed in Iranian territorial waters (TeleGeography); AAE-1 named; Google, Meta, Microsoft, Amazon cited as fee-payers; $10T daily financial transactions at risk; coincides with 72-day US-Iran naval standoff
- Edition 13 (2026-05-28): EU clears Italy's €700M TIM Sparkle nationalisation without conditions — MEF + Retelit (Cellnex-owned) take state control of Mediterranean routing; US OFAC/FCC clearance pending Q2 2026; Italy gains strategic veto over cable routing and hyperscaler contracts on the primary Hormuz/Red Sea alternative corridor
- Edition 14 (2026-06-04): EU commits €347M to submarine cable security across three CEF Digital calls — €180M backbone call for 13 Cable Projects of European Interest, €20M smart cable monitoring, €20M Baltic Sea emergency repair capacity; Cable Security Toolbox released; June 30, 2026 submission deadline live now
- Edition 15 (2026-06-11): GUIDE launched May 30 at Shangri-La Dialogue — 17 founding nations include 7 EU member states (Estonia, Finland, France, Italy, Latvia, Lithuania, Netherlands, Sweden), UK, Australia, NZ, Singapore, and 5 Indo-Pacific partners; voluntary, non-binding information-sharing framework covering Atlantic, Mediterranean, Indian Ocean, and Pacific chokepoints; UK Defence Secretary disclosed tracking 3 Russian submarines surveying North Atlantic cable routes concurrently; GUIDE operates in parallel with EU Cable Security Toolbox — dual military/intelligence and civilian/infrastructure governance frameworks now active for same physical infrastructure
- Edition 16 (2026-06-18): FCC draft Second R&O on submarine cable landing licences published June 4; vote scheduled June 25, 2026; framework extends US regulatory authority to SLTE — hardware at US cable-landing points converting optical signals to terrestrial traffic; Covered List entities (Huawei, ZTE, HMN Technologies/Huawei Marine Networks) barred from SLTE ownership, must file annual Foreign Adversary Annual Report; Nokia Submarine Networks, Subcom, Alcatel Submarine Networks are primary SLTE beneficiaries; three parallel governance layers now formed around the same physical infrastructure: EU Cable Security Toolbox (civilian/infrastructure), GUIDE (17-nation military/intelligence), FCC SLTE order (equipment layer)

## thread-id: coreweave-gpu-debt
Beat: Data Infrastructure
Status: closed
Summary: CoreWeave's leveraged GPU model — $8.5B investment-grade facility (EP2), now $3.5B convertible raise alongside $35B Meta commitment and $66.8B contracted backlog; 9 of 10 top AI model providers on platform.
Changelog:
- Edition 2 (2026-04-04): CoreWeave closes $8.5B investment-grade GPU debt facility; institutional precedent set for GPU-as-collateral
- Edition 5 (2026-04-11): $21B Meta expansion + Anthropic deal in 48 hours; $3.5B convertible raise; backlog reaches $66.8B
- Edition 13 (2026-05-28): Thread closed — no development in 8 consecutive editions; CoreWeave/Meta thesis tracked under hyperscaler-capex-supercycle

## thread-id: nuclear-ppas-data-centres
Beat: Energy & Power
Status: closed
Summary: Meta, Microsoft, Equinix all signed or announced nuclear PPAs; IEA confirms 485 TWh consumed globally in 2025 (+17%), Europe faces 70% growth by 2030; SMR conditional offtake pipeline grew from 25 GW to 45 GW in under four months; tech sector signed ~40% of all corporate renewable PPAs in 2025.
Changelog:
- Edition 2 (2026-04-04): Meta, Microsoft, Equinix announce nuclear PPA commitments; FERC interconnection review opens
- Edition 8 (2026-04-25): IEA publishes 2025 data — 485 TWh consumed globally (+17%); Europe faces +45 TWh (+70%) by 2030; SMR pipeline grew 25→45 GW in under four months; tech sector ~40% of all corporate renewable PPAs
- Edition 13 (2026-05-28): Thread closed — no nuclear or renewable PPA development in 5 consecutive editions (8→13); energy theme continues in ireland-dc-energy-policy, uk-ai-energy-gap, and nordics-infra-advantage threads

## thread-id: sea-dc-buildout
Beat: Data Infrastructure
Status: closed
Summary: AWS, Google, Microsoft all announced major SEA capex 2024–2025; power grid reliability identified as binding constraint; data localisation laws tightening in Indonesia, Vietnam, Thailand.
Changelog:
- Edition 2 (2026-04-04): Hyperscaler SEA capex wave confirmed; grid reliability flagged as primary bottleneck
- Edition 13 (2026-05-28): Thread closed — no development in 11 consecutive editions; SEA hyperscaler buildout continues but outside DII's Nordics/UK/Western Europe editorial focus

## thread-id: nvidia-supply-crunch
Beat: Data Infrastructure
Status: closed
Summary: Vera Rubin lead times 9–12 months; CoreWeave Meta deal incorporates first commercial Vera Rubin deployments; inference economics shifting as H100 supply normalises.
Changelog:
- Edition 2 (2026-04-04): Vera Rubin lead times 9–12 months; inference economics shifting
- Edition 5 (2026-04-11): First commercial Vera Rubin deployments confirmed in CoreWeave-Meta contract
- Edition 13 (2026-05-28): Thread closed — no development in 8 consecutive editions; Rubin GPU supply tracked where relevant within hyperscaler-capex-supercycle (Nscale/Narvik Microsoft commitment is the current live data point)

## thread-id: european-telecom-consolidation
Beat: Western Europe
Status: active
Summary: VodafoneThree approved in UK; SFR: binding MOU signed June 6, 2026 — €20.35B, Bouygues 42% (~€8.5B, 52% of SFR revenue), Free 31% (~€6.3B), Orange 27% (~€5.5B); break-up fees €100M–€2B; AdC president Coeuré warned June 10 deal "ne va pas de soi," citing 2005 French mobile price-collusion precedent; parallel filings (Bouygues/Orange → AdC, Free/Iliad → EC due to non-French revenue); no formal pre-notification received; regulatory closing H2 2027; Romania 4→3 completed June 30 — Vodafone/Telekom Romania legal merger, OTE exits at €70M (near-zero EV), Digi acquires spectrum + towers for €40M (vs €200M+ auction value); Romania ARPU trajectory is the empirical test for AdC's price-risk thesis; TIM: Poste Italiane €10.8B bid, Italian state to hold 50%+ of €27B combined group.
Changelog:
- Edition 3 (2026-04-04): VodafoneThree merger approved; regulatory posture shift confirmed; Goldman consolidation map published
- Edition 8 (2026-04-25): Orange/Bouygues/Iliad enter €20.35B exclusive SFR negotiations — France 4→3 operators; Poste Italiane launches €10.8B TIM bid — Italian state to control 50%+ of combined €27B revenue group; Goldman Italy thesis confirmed
- Edition 10 (2026-05-07): SFR May 15 exclusivity deadline — final 11-day sprint; Bouygues 42% (~€8.5B) takes B2B and rural mobile, Free 31% (~€6.3B), Orange 27% (~€5.5B); Romania 4→3 cleared simultaneously (Vodafone Romania + Digi Romania divide Telekom Romania assets) — second EU market confirming permissive consolidation posture
- Edition 12 (2026-05-21): SFR exclusivity extended three weeks to June 5 — deal not yet signed; €20.35B terms and asset split unchanged; official statements include "no certainty" language; Autorité de la concurrence clock not started; June 5 is the new hard deadline
- Edition 14 (2026-06-04): SFR June 5 deadline now 1 day out — second extension, still unsigned; Autorité de la concurrence not formally notified; Altice France €40B+ debt pressure unchanged; EU Commission Draft Revised Merger Guidelines (April 30) abandon 2-year investment benefit horizon and codify "loss of investment competition" — structurally favourable for 4→3 defence; public consultation June 26
- Edition 15 (2026-06-11): Binding MOU signed June 6 — one day after June 5 deadline; break-up fees in the €100M–€2B range established, materially raising exit cost above any prior milestone; asset split confirmed (Bouygues 42%/~€8.5B/52% revenue, Free 31%/~€6.3B, Orange 27%/~€5.5B); Orange CEO Heydemann publicly referenced "behavioral remedies" before formal notification — signals Phase 2 engagement, not Phase 1 fast-track; Autorité de la concurrence clock starts only on formal filing (definitive documents H2 2026); regulatory closing H2 2027
- Edition 16 (2026-06-18): AdC president Benoît Coeuré warns June 10 that SFR deal "ne va pas de soi" — cites 2005 French mobile price-collusion case (France's last three-player market structure) as substantive risk; parallel regulatory tracks confirmed: Bouygues/Orange file with AdC, Free (Iliad) must file with EC due to non-French revenue weight; no formal pre-notification received by AdC as of June 10; regulatory close no earlier than H2 2027 (18 months from formal filing)
- Edition 16 (2026-06-18): Romania 4→3 completed June 30 — Vodafone Romania and Telekom Romania Mobile Communications complete legal merger; OTE (Deutsche Telekom/Hellenic Telekom subsidiary) exits at €70M total (near-zero EV); Vodafone paid €30M (postpaid, retail, network); Digi paid €40M (prepaid, spectrum, towers worth €200M+ at auction); Romania is second EU 4→3 market in 2026 after VodafoneThree UK (April 2026); three-player market: Orange, Vodafone, Digi; Romania ARPU data 12–18 months post-merger is the empirical test for AdC's price-risk thesis in SFR review

## thread-id: us-semiconductor-tariffs
Beat: Data Infrastructure
Status: closed
Summary: Phase 1 25% tariff on advanced chips since Jan 15 with data centre exemption; April 14 Phase 2 report deadline passed; July 1 data centre chip review is next milestone.
Changelog:
- Edition 4 (2026-04-05): Trump Section 232 order — 25% tariff on advanced chips, data centre exemption carved out
- Edition 5 (2026-04-11): April 14 Phase 2 report deadline tracked; July 1 next decision point
- Edition 13 (2026-05-28): Thread closed — no development in 8 consecutive editions; July 1 data centre chip review passed without major new policy; tariff risk absorbed into baseline supply chain assumptions

## thread-id: dc-valuation-reset
Beat: Capital & Deals
Status: closed
Summary: Aligned Data Centers sold to BlackRock/AIP/MGX for $40B — largest DC acquisition ever, 140% above prior AirTrunk record; AIP targeting $100B total deployment; new pricing floor set for AI-capable DC assets.
Changelog:
- Edition 5 (2026-04-11): Macquarie exits Aligned at $40B to BlackRock/AIP/MGX; beats AirTrunk record by 140%; AIP opens $100B programme
- Edition 13 (2026-05-28): Thread closed — no development in 8 consecutive editions; DC asset valuation theme continues within Capital & Deals coverage (Blackstone/Google TPU JV is the current live data point)

## thread-id: uk-ai-energy-gap
Beat: UK & Ireland
Status: active
Summary: OpenAI paused Stargate UK citing industrial electricity at 24.67p/kWh (~4x US rates); UK secured NSIP opt-in for large data centres (bypasses local planning authorities, aligns consent with energy infrastructure delivery); Ofcom to gain cybersecurity oversight of data centres via Cyber Security and Resilience Bill; Ofgem Phase 1 demand connection reform (data centres the explicit focus): financial gatekeeping proposed — refundable deposits, commitment fees, FID evidence, planning permission as queue entry conditions; UK demand queue tripled to 125 GW with ~50 GW linked to data centres (~140 DCs in queue, only 71/~20 GW at FID); tCSNP2 transmission plan refresh due June 2026; energy pricing gap vs Nordic and US markets remains unaddressed by all proposed reforms.
Changelog:
- Edition 6 (2026-04-24): OpenAI pauses Stargate UK indefinitely — energy cost and copyright regulation cited; 8,000-GPU north-east England deployment on hold
- Edition 12 (2026-05-21): UK secures parliamentary backing for NSIP opt-in for major data centres — nationally-determined planning track, 12–24 month approvals, bypasses local authorities; Ofcom cybersecurity oversight extension confirmed via Cyber Security and Resilience Bill; industrial electricity at 24.67p/kWh unchanged — planning reform addresses one bottleneck but not the primary investment constraint
- Edition 13 (2026-05-28): EDCA €176B European DC forecast cites UK 24.67p/kWh as the clearest illustration of grid-as-constraint thesis across FLAP-D markets; no new UK planning applications or Ofgem queue decisions; Ofgem grid connection queue resolution remains the next structural watch
- Edition 15 (2026-06-11): Ofgem Phase 1 demand connection reform launched — data centres explicit focus; UK demand queue tripled in 7 months (41 GW Nov 2024 → 125 GW Jun 2025), ~50 GW linked to data centres; NESO identifies ~140 DCs in queue, only 71 (~20 GW) at FID; proposed gatekeeping: refundable deposits, progressive commitment fees, secured financing evidence, outline planning permission; tCSNP2 transmission investment plan refresh due June 2026 — determines grid-capable corridors for 2028–2032; industrial electricity 24.67p/kWh unchanged

## thread-id: nordics-infra-advantage
Beat: Nordics
Status: active
Summary: Nordics satisfy all three AI infrastructure criteria simultaneously — low power cost (Norway ~€0.03–0.04/kWh, Sweden ~€0.05/kWh), grid access, and regulatory predictability; Nscale's Narvik campus ($4.2B total capital, $790M infrastructure debt, Eksfin/state backing, Microsoft 30,000+ Rubin GPUs) confirms Norway as Europe's AI compute anchor; atNorth NOR01 (Haugaland, 350MW, $1.1B Phase 1, CPP Investments 60%/Equinix 40%, Statnett dedicated substation, 2028) raises Norway's total announced AI hyperscale pipeline to ~580MW; EQT launched €8B GlobalConnect sale; DTCP acquired Dark Fiber Group; advantage sharpens vs Ireland CRU generation obligation and UK's 24.67p/kWh.
Changelog:
- Edition 6 (2026-04-24): Nordics cited as benchmark vs UK energy costs in Stargate UK pause analysis; structural advantage confirmed
- Edition 8 (2026-04-25): EQT launches €8B GlobalConnect sale — 244,000km fibre, 23 DCs, 27 subsea cables; Goldman Sachs mandated; Antin among early bidders; Nordic power cost advantage re-confirmed vs UK 24.67p/kWh
- Edition 10 (2026-05-07): DTCP acquires Dark Fiber Group — greenfield independent long-haul dark fibre across all four Nordic markets targeting hyperscaler inter-DC connectivity gap; Nordic power cost advantage further confirmed vs Ireland CRU generation obligation (new entrant cost rising) and UK 24.67p/kWh
- Edition 12 (2026-05-21): GlobalConnect Kattegat cable (Sweden-Denmark, €11.9M, 50% EU co-funded) advances Nordic fibre corridor mid-sale; KKR Helix platform's build-partner model flags Nordic power economics as likely early European target geography
- Edition 13 (2026-05-28): Nscale closes $790M (€670M) infrastructure debt for Narvik 230MW campus (ABN AMRO, DNB, Eksfin, Nordea, SEB); Eksfin participation confirms Norwegian government classification as national industrial infrastructure; Microsoft commits 30,000+ NVIDIA Rubin GPUs for H2 2027; accordion to 520MW potential; total capital committed to Narvik exceeds $4.2B; EDCA €176B European DC forecast cites Nordic power economics as primary new-build advantage
- Edition 16 (2026-06-18): atNorth announces NOR01 at Haugaland Business Park — 350MW full build, 120MW Phase 1, NOK 11B (~$1.1B), 2028 power availability; Statnett (Norway's TSO) building dedicated substation — same national industrial infrastructure model as Nscale Narvik (Eksfin); CPP Investments (60%/~$1.6B) + Equinix (40%) as owners post-$4B acquisition from Partners Group (February 2026); Equinix deploys first Norwegian colocation footprint via NOR01; Norway total announced AI hyperscale pipeline ~580MW (NOR01 + Narvik); Haugesund node power ~€0.04/kWh vs UK 24.67p/kWh unchanged

## thread-id: globalconnect-sale
Beat: Nordics
Status: dormant
Summary: EQT targeting €8B sale of GlobalConnect via Goldman Sachs — 244,000km fibre across Denmark, Norway, Sweden, Germany, Finland; 23 data centres, 27 subsea cables, 30,000 business customers; Antin Infrastructure Partners among early bidders; Kattegat cable (92km, 288 strands, €11.9M, 2027 go-live, 50% EU CEF2 co-funded) announced mid-sale under Bifrost programme; DTCP's Dark Fiber Group in same geography as greenfield competitor. No process update in 3 editions.
Changelog:
- Edition 8 (2026-04-25): EQT launches €8B GlobalConnect sale; Goldman Sachs mandated; Antin identified as early bidder; EQT to sell as single entity rather than break up integrated fibre-DC-subsea model
- Edition 10 (2026-05-07): DTCP acquires Dark Fiber Group as independent carrier-neutral dark fibre entrant in GlobalConnect's Nordic geography — bifurcates Nordic fibre opportunity between integrated legacy platform (GlobalConnect at €8B) and greenfield hyperscaler-oriented build (Dark Fiber Group)
- Edition 12 (2026-05-21): GlobalConnect announces Kattegat cable — 92km Sweden-Denmark link, 288 strands, €11.9M investment, EU CEF2 co-funds €5.9M (50%), 2027 go-live; part of Bifrost programme targeting 3,000km+ new Nordic fibre; capex committed mid-sale to demonstrate active network investment thesis to prospective buyers
- Edition 15 (2026-06-11): Thread moved to dormant — no first-round bid announcement or process update in editions 13, 14, 15; Goldman Sachs auction ongoing; next milestone is first-round bid submissions or buyer shortlist announcement

## thread-id: hyperscaler-capex-supercycle
Beat: Data Infrastructure
Status: active
Summary: Combined 2026 hyperscaler capex revised to $785B (Moody's) — $60B above prior $725B consensus; Moody's projects approaching $1 trillion in 2027; Q1 2026 optical DC interconnect equipment purchases up 50% YoY; individual guidance: Microsoft $190B, Amazon $200B, Alphabet $180–190B, Meta $125–145B; Blackstone committed $5B equity to Google TPU JV (total $25B with leverage); aggregate institutional private capital committed to AI infrastructure platforms exceeds $75B; private capital cross-platform across NVIDIA GPU-centric and proprietary AI silicon structures.
Changelog:
- Edition 10 (2026-05-07): Q1 2026 combined hyperscaler capex $112B — double Q1 2025; full-year 2026 tracking $725B vs ~$410B in 2025; Alphabet revised guide to $180–190B; Amazon $200B; Meta $125–145B (shares -6%); Alphabet CFO: 2027 will "significantly increase"; AWS Q1 revenue $37.59B +28% YoY — fastest in 15 quarters; Microsoft AI $37B annualised run rate +123% YoY
- Edition 13 (2026-05-28): Blackstone commits $5B equity to Google TPU compute-as-a-service JV (total $25B with leverage, announced May 18–20); Benjamin Treynor Sloss CEO; 500MW by 2027; largest private-capital commitment to non-GPU AI compute platform to date; Blackstone now holds cross-platform AI compute exposure (DC REIT + Google TPU JV)
- Edition 14 (2026-06-04): Moody's Ratings revises 2026 combined hyperscaler capex to $785B — $60B above prior consensus — and projects approaching $1 trillion by 2027; Q1 2026 cloud provider optical DC interconnect equipment purchases up 50% YoY; aggregate institutional private capital committed to AI infrastructure platforms exceeds $75B across KKR Helix, Blackstone/Google TPU JV, AIP/Aligned

## thread-id: ireland-dc-energy-policy
Beat: UK & Ireland
Status: active
Summary: CRU final connection policy requires all data centres ≥1 MVA to build and operate matching generation or storage, participate in the wholesale electricity market, and source ≥80% of annual electricity from additional Irish-sourced renewables within six years of grid energisation — converting operators into energy infrastructure developers; Ireland's DC load is ~800 MW and ~21% of national electricity demand; Irish High Court granted leave April 28, 2026 for judicial review of the policy — Friends of the Irish Environment, Friends of the Earth Ireland, and ClientEarth challenge the 20% non-renewable allowance as legally insufficient; suspension of new connection approvals is the highest-consequence potential outcome.
Changelog:
- Edition 10 (2026-05-07): CRU issues final Large Energy User connection policy — generation obligation equal to full import capacity, mandatory wholesale market participation, 80% Irish-sourced renewables within 6 years; applies to all facilities ≥1 MVA MIC; fundamentally reprices Ireland's tier-1 DC market entry cost; sharpens competitive advantage of Nordic markets without equivalent obligation
- Edition 13 (2026-05-28): EDCA €176B European DC forecast explicitly names CRU generation obligation as evidence that grid readiness — not capital — is the binding European DC investment constraint; no new CRU connection approvals or Green Energy Park announcements this edition
- Edition 14 (2026-06-04): Irish High Court grants leave April 28 for judicial review of CRU data centre connection policy — Friends of the Irish Environment, Friends of the Earth Ireland, and ClientEarth; challenge argues 20% non-renewable allowance violates Irish and EU climate law; court could order policy revision or suspend new connection approvals pending revised CRU decision; hearing timeline 12–18 months from leave grant

## thread-id: germany-huawei-removal
Beat: Western Europe
Status: closed
Summary: End-2026 hard deadline for removing Huawei/ZTE from 5G core networks — Deutsche Telekom, Vodafone Germany, and Telefonica Deutschland under binding bilateral agreements with Federal Ministry of Interior; Nokia and Ericsson are primary replacement vendors; 2029 deadline follows for radio access networks. No operator-level development in 5 consecutive editions since Edition 10.
Changelog:
- Edition 10 (2026-05-07): 8 months to end-2026 core deadline — all three German operators in execution sprint; Nokia and Ericsson expanded German delivery capacity; 2029 radio access phase is larger and more expensive; Germany's bilateral agreement model being studied by France, Italy, and Netherlands for their own Chinese vendor reviews
- Edition 13 (2026-05-28): Thread moved to dormant — no operator-level update in 3 editions; end-2026 core deadline now 7 months out; next expected milestone is operator announcement of core network transition completion or Q3 2026 progress disclosure
- Edition 15 (2026-06-11): Thread closed — no operator-level development in 5 editions (11–15) since last update in Edition 10; end-2026 core deadline 6 months out; reopen on operator transition completion announcement or material delay disclosure

## thread-id: kkr-helix-ai-infra
Beat: Capital & Deals
Status: dormant
Summary: KKR launched Helix Digital Infrastructure on April 30, 2026 — $10B+ committed capital (sovereign wealth fund + 2 strategic partners), Adam Selipsky (ex-AWS CEO) as Chair/CEO, Waldemar Szlezak (KKR global head of digital infrastructure) as CIO; mandate spans data centres, power generation and transmission, and connectivity; build-partner model for hyperscalers wanting capacity off-balance-sheet; further capital raises planned. No new asset announcement in 3 editions.
Changelog:
- Edition 12 (2026-05-21): KKR launches Helix Digital Infrastructure — $10B+ committed, Adam Selipsky (ex-AWS CEO) as Chair/CEO, Waldemar Szlezak as CIO; full-stack AI infrastructure build-partner mandate; first purpose-built platform of this type at institutional scale
- Edition 15 (2026-06-11): Thread moved to dormant — no new Helix asset announcement or European geographic commitment in editions 13, 14, 15; next expected milestone is first European campus announcement or additional capital raise

## thread-id: dt-tmobile-merger
Beat: Western Europe
Status: dormant
Summary: Deutsche Telekom evaluating full all-share combination with T-Mobile US via new Irish-domiciled holding company — combined market cap ~$260–300B, 200M+ subscribers globally; DT already holds 53%+ of T-Mobile US; structure mirrors 2018 Linde-Praxair; talks described as early stage, no binding agreement signed; deal would be the largest in telecoms history. No new development in 3 editions.
Changelog:
- Edition 12 (2026-05-21): Deutsche Telekom reported to be evaluating full T-Mobile US combination — all-share deal via new holding company (~$260–300B combined market cap); Bloomberg confirmed late April 2026; early stage, no agreement; Ireland flagged as incorporation jurisdiction; Linde-Praxair structural template; antitrust complexity across FCC, DOJ, and European Commission
- Edition 15 (2026-06-11): Thread moved to dormant — no new development in editions 13, 14, 15; early-stage evaluation reported in late April 2026 continues; next milestone is formal announcement of intent or confirmation that talks have ended

## thread-id: hscale-non-flap-buildout
Beat: Western Europe
Status: active
Summary: Bain Capital and Aquila Group's HSCALE platform committed €2B+ across 250MW at two liquid-cooled campuses in Northwest Milan (Settimo) — both targeted for 2028 ready-for-service; platform thesis is non-FLAP EMEA markets (Italy, Spain, Poland) offer better risk-adjusted returns than congested Dublin, Amsterdam, Frankfurt; Digital Realty simultaneously launched BCN1 Barcelona; first hyperscaler lease announcements and Italian grid connection timeline are the next watch.
Changelog:
- Edition 13 (2026-05-28): HSCALE closes second Milan campus (Settimo, NW Milan) — €2B+ total committed, 250MW, liquid-cooled-first, 2028 RFS; Bain Capital + Aquila Group co-founded HSCALE in 2025 as EMEA non-FLAP hyperscale platform; implied ~€8M/MW capital intensity consistent with European greenfield benchmarks; Digital Realty simultaneously launched BCN1 Barcelona (Sant Adrià de Besòs)

## thread-id: european-cable-sovereignty
Beat: Connectivity
Status: active
Summary: Italian MEF + Retelit (Cellnex-owned) acquired TIM Sparkle for €700M (EC-cleared April 13, 2026, no conditions) — Italy takes direct state control of Mediterranean subsea routing; US OFAC/FCC clearance pending Q2 2026; part of a pattern: France (Altice SFR oversight), Germany (Huawei/ZTE removal mandate), Italy (Sparkle acquisition) — three European state-level interventions in strategic telecom infrastructure in 2026, none blocked by EC competition law.
Changelog:
- Edition 13 (2026-05-28): EC approves €700M TIM Sparkle sale to MEF + Retelit (Cellnex-owned) without antitrust conditions; US OFAC/FCC clearance pending, TIM guided Q2 2026; TIM share buyback triggered on completion; Italy controls routing and contract terms for the primary Hormuz/Red Sea alternative corridor

## thread-id: european-dc-ppa-drought
Beat: Energy & Power
Status: active
Summary: European data centre PPA volumes fell 38% — 4.2 GW (2024) to 2.6 GW (2025); offshore wind DC PPA segment collapsed from 1.35 GW (2024) to 0.5 GW (2025) to 100 MW in Q1 2026; structural causes are wind project delivery delays, developer-operator pricing standoff on capture rates, and hyperscaler pivot toward nuclear and hydro baseload; wider EU PPA market deal count down 60% YoY; Nordic hydro markets (Norway, Sweden) are primary European beneficiaries; EDCA €176B DC buildout forecast has no confirmed clean power basis for significant FLAP-D geography.
Changelog:
- Edition 14 (2026-06-04): Rystad Energy confirms European DC PPA volumes fell 38% (2024→2025); offshore wind DC PPA segment collapsed to 100 MW in Q1 2026 from 1.35 GW in 2024; wider EU PPA market deal count down 60% YoY, contracted capacity down 40% vs 2024; structural causes identified as wind project delays, capture rate pricing standoff, and operator pivot to baseload alternatives

## thread-id: softbank-france-ai-dc
Beat: Western Europe
Status: active
Summary: SoftBank Group committed up to €75B to build 5 GW of AI data centre capacity in France — announced May 30, 2026 at Macron's Choose France summit; €45B Phase 1 confirmed for 3.1 GW across Dunkirk (Loon-Plage), Bosquel, and Bouchain in Hauts-de-France, targeted 2031 RFS; Schneider Electric manufacturing co-located at Port of Dunkirk; Phase 2 €30B contingent on Phase 1 execution; 5 GW requires ~5 TWh/year at typical PUE — no PPA or grid connection strategy disclosed; largest single FDI commitment in French modern economic history.
Changelog:
- Edition 15 (2026-06-11): SoftBank Group announces €75B France AI data centre commitment at Choose France summit — €45B Phase 1 confirmed for 3.1 GW (Dunkirk/Loon-Plage, Bosquel, Bouchain), 2031 RFS; Phase 2 €30B contingent; Schneider Electric co-located at Dunkirk for enclosure and power module manufacturing; 5 GW total exceeds combined France/Germany/Netherlands current operating capacity; no PPA or French grid connection strategy disclosed; Masayoshi Son present alongside Macron

## thread-id: eu-ai-gigafactory
Beat: Data Infrastructure
Status: active
Summary: EU's €20B AI gigafactory initiative (5 sovereign AI data centres) facing structural confidence failure — bidder pool collapsed from ~70 expressions of interest to ~10 expected submissions; bidding round deferred May → July 2026; only €4.1B of €20B has confirmed EU funding; €15.9B member state and private co-investment has not materialised; Schwarz Group (Lidl/Kaufland parent) building 200+ MW data centre south of Berlin without waiting for EU subsidy; bilateral investment structures (SoftBank France, Microsoft/Google bilateral capex) pre-empting the sovereign capacity rationale.
Changelog:
- Edition 15 (2026-06-11): EU AI gigafactory bidder pool collapses ~70 → ~10; bidding round deferred May → July 2026 after EC repeatedly delayed selection criteria; only 2 of 5 planned centres can receive EU funding pre-2028; confirmed EU subsidy €4.1B vs €15.9B unconfirmed co-investment; Schwarz Group (Lidl/Kaufland parent, Europe's largest retailer) building 200+ MW south of Berlin independently; at least 2 remaining consortia considering withdrawal; bilateral investment structures (SoftBank France €75B, this edition) displacing EU-governed programme rationale

## thread-id: goodman-cpp-european-dc
Beat: Capital & Deals
Status: active
Summary: CPP Investments (50%) and Goodman Group (50%) European Data Centre Partnership — €8B total platform, €2.2B initial commitment (A$3.9B), 50/50 JV announced December 22, 2025; 4 projects commencing construction by June 30, 2026: PAR01 and PAR02 (Paris), FRA02 (Frankfurt), AMS01 (Amsterdam); combined 435MW primary power, 282MW IT load; all 4 sites have secured power connections and planning permits; Goodman Group is Australia's largest industrial REIT entering European hyperscale DC for the first time; CPP total European DC allocation approaching $5B combining Goodman FLAP-D JV (50%) and atNorth Nordic AI compute (60%).
Changelog:
- Edition 16 (2026-06-18): Goodman Group + CPP Investments European DC Partnership enters construction phase — 4 projects (PAR01/PAR02 Paris, FRA02 Frankfurt, AMS01 Amsterdam) commencing by June 30, 2026; 435MW primary power, 282MW IT load; all 4 with secured power connections and planning permits; €8B total platform capacity, €2.2B initial commitment, 50/50 JV (announced December 22, 2025); CPP holds dual European DC exposure: Goodman FLAP-D (50%) + atNorth Nordic AI compute (60%, NOR01 350MW); total European DC allocation approaching $5B
