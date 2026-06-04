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
Summary: 17 cables disrupted via Red Sea corridor with no repair timeline; Iran formalised regulatory mandate requiring permits, annual fees, and exclusive maintenance rights for 7 Hormuz cables; Italy acquired TIM Sparkle (EC-cleared, €700M) — Rome takes direct state control of Mediterranean routing infrastructure; EU committed €347M to submarine cable security — €180M CEF backbone call for 13 Cable Projects of European Interest (June 30, 2026 deadline), €20M smart cable monitoring, €20M Baltic Sea emergency repair; Cable Security Toolbox released as EU-wide resilience standard; $10 trillion in daily financial transactions transit the named Hormuz cables.
Changelog:
- Edition 1 (2026-03-15): Gulf conflict disrupts 17 Red Sea submarine cables; traffic rerouted via Cape of Good Hope
- Edition 5 (2026-04-11): WorldLink announced — $700M UAE-Iraq hybrid cable, 900Tbps, sub-100ms Europe-ME latency, bypasses Suez corridor
- Edition 8 (2026-04-25): US-Iran conflict escalates to Hormuz; IRGC-linked media threatens 7 GCC submarine cables — dual-chokepoint closure with no historical precedent; no repair timeline while hostilities continue
- Edition 10 (2026-05-07): US Strategic Subsea Cables Act (S.3249, Shaheen/Barrasso) cleared Senate Foreign Relations Committee unanimously — 2 FTE State Dept cable diplomacy, sanctions mechanism, ICPC engagement; EU committed €20M to cable resilience stress-testing programme; Saudi stc announced $800M SilkLink 4,500km bypass cable with new landing stations
- Edition 12 (2026-05-21): Iran formalises Hormuz cable mandate via IRGC-affiliated Tasnim News Agency — permits, annual fees, exclusive maintenance rights for 7 cables; Falcon and GBI confirmed in Iranian territorial waters (TeleGeography); AAE-1 named; Google, Meta, Microsoft, Amazon cited as fee-payers; $10T daily financial transactions at risk; coincides with 72-day US-Iran naval standoff
- Edition 13 (2026-05-28): EU clears Italy's €700M TIM Sparkle nationalisation without conditions — MEF + Retelit (Cellnex-owned) take state control of Mediterranean routing; US OFAC/FCC clearance pending Q2 2026; Italy gains strategic veto over cable routing and hyperscaler contracts on the primary Hormuz/Red Sea alternative corridor
- Edition 14 (2026-06-04): EU commits €347M to submarine cable security across three CEF Digital calls — €180M backbone call for 13 Cable Projects of European Interest, €20M smart cable monitoring, €20M Baltic Sea emergency repair capacity; Cable Security Toolbox released; June 30, 2026 submission deadline live now

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
Summary: VodafoneThree approved in UK; SFR: June 5, 2026 is the second and current exclusivity deadline — €20.35B terms (Bouygues 42%, Free 31%, Orange 27%) unchanged, deal unsigned, Autorité de la concurrence not yet notified, Altice France carrying €40B+ debt load; EU Commission published Draft Revised Merger Guidelines April 30 — abandons rigid 2-year benefit horizon, codifies "loss of investment competition" theory, public consultation June 26; Romania 4→3 cleared; TIM: Poste Italiane €10.8B bid, Italian state to hold 50%+ of €27B combined group.
Changelog:
- Edition 3 (2026-04-04): VodafoneThree merger approved; regulatory posture shift confirmed; Goldman consolidation map published
- Edition 8 (2026-04-25): Orange/Bouygues/Iliad enter €20.35B exclusive SFR negotiations — France 4→3 operators; Poste Italiane launches €10.8B TIM bid — Italian state to control 50%+ of combined €27B revenue group; Goldman Italy thesis confirmed
- Edition 10 (2026-05-07): SFR May 15 exclusivity deadline — final 11-day sprint; Bouygues 42% (~€8.5B) takes B2B and rural mobile, Free 31% (~€6.3B), Orange 27% (~€5.5B); Romania 4→3 cleared simultaneously (Vodafone Romania + Digi Romania divide Telekom Romania assets) — second EU market confirming permissive consolidation posture
- Edition 12 (2026-05-21): SFR exclusivity extended three weeks to June 5 — deal not yet signed; €20.35B terms and asset split unchanged; official statements include "no certainty" language; Autorité de la concurrence clock not started; June 5 is the new hard deadline
- Edition 14 (2026-06-04): SFR June 5 deadline now 1 day out — second extension, still unsigned; Autorité de la concurrence not formally notified; Altice France €40B+ debt pressure unchanged; EU Commission Draft Revised Merger Guidelines (April 30) abandon 2-year investment benefit horizon and codify "loss of investment competition" — structurally favourable for 4→3 defence; public consultation June 26

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
Summary: OpenAI paused Stargate UK citing industrial electricity at 24.67p/kWh (~4x US rates); UK secured NSIP opt-in for large data centres (bypasses local planning authorities, aligns consent with energy infrastructure delivery); Ofcom to gain cybersecurity oversight of data centres via Cyber Security and Resilience Bill; energy pricing gap vs Nordic and US markets remains unaddressed.
Changelog:
- Edition 6 (2026-04-24): OpenAI pauses Stargate UK indefinitely — energy cost and copyright regulation cited; 8,000-GPU north-east England deployment on hold
- Edition 12 (2026-05-21): UK secures parliamentary backing for NSIP opt-in for major data centres — nationally-determined planning track, 12–24 month approvals, bypasses local authorities; Ofcom cybersecurity oversight extension confirmed via Cyber Security and Resilience Bill; industrial electricity at 24.67p/kWh unchanged — planning reform addresses one bottleneck but not the primary investment constraint
- Edition 13 (2026-05-28): EDCA €176B European DC forecast cites UK 24.67p/kWh as the clearest illustration of grid-as-constraint thesis across FLAP-D markets; no new UK planning applications or Ofgem queue decisions; Ofgem grid connection queue resolution remains the next structural watch

## thread-id: nordics-infra-advantage
Beat: Nordics
Status: active
Summary: Nordics satisfy all three AI infrastructure criteria simultaneously — low power cost (Norway ~€0.03–0.04/kWh, Sweden ~€0.05/kWh), grid access, and regulatory predictability; Nscale's Narvik campus ($4.2B total capital, $790M infrastructure debt, Eksfin/state backing, Microsoft 30,000+ Rubin GPUs) confirms Norway as Europe's AI compute anchor; EQT launched €8B GlobalConnect sale; DTCP acquired Dark Fiber Group; advantage sharpens vs Ireland CRU generation obligation and UK's 24.67p/kWh.
Changelog:
- Edition 6 (2026-04-24): Nordics cited as benchmark vs UK energy costs in Stargate UK pause analysis; structural advantage confirmed
- Edition 8 (2026-04-25): EQT launches €8B GlobalConnect sale — 244,000km fibre, 23 DCs, 27 subsea cables; Goldman Sachs mandated; Antin among early bidders; Nordic power cost advantage re-confirmed vs UK 24.67p/kWh
- Edition 10 (2026-05-07): DTCP acquires Dark Fiber Group — greenfield independent long-haul dark fibre across all four Nordic markets targeting hyperscaler inter-DC connectivity gap; Nordic power cost advantage further confirmed vs Ireland CRU generation obligation (new entrant cost rising) and UK 24.67p/kWh
- Edition 12 (2026-05-21): GlobalConnect Kattegat cable (Sweden-Denmark, €11.9M, 50% EU co-funded) advances Nordic fibre corridor mid-sale; KKR Helix platform's build-partner model flags Nordic power economics as likely early European target geography
- Edition 13 (2026-05-28): Nscale closes $790M (€670M) infrastructure debt for Narvik 230MW campus (ABN AMRO, DNB, Eksfin, Nordea, SEB); Eksfin participation confirms Norwegian government classification as national industrial infrastructure; Microsoft commits 30,000+ NVIDIA Rubin GPUs for H2 2027; accordion to 520MW potential; total capital committed to Narvik exceeds $4.2B; EDCA €176B European DC forecast cites Nordic power economics as primary new-build advantage

## thread-id: globalconnect-sale
Beat: Nordics
Status: active
Summary: EQT targeting €8B sale of GlobalConnect via Goldman Sachs — 244,000km fibre across Denmark, Norway, Sweden, Germany, Finland; 23 data centres, 27 subsea cables, 30,000 business customers; Antin Infrastructure Partners among early bidders; Kattegat cable (92km, 288 strands, €11.9M, 2027 go-live, 50% EU CEF2 co-funded) announced mid-sale under Bifrost programme; DTCP's Dark Fiber Group in same geography as greenfield competitor.
Changelog:
- Edition 8 (2026-04-25): EQT launches €8B GlobalConnect sale; Goldman Sachs mandated; Antin identified as early bidder; EQT to sell as single entity rather than break up integrated fibre-DC-subsea model
- Edition 10 (2026-05-07): DTCP acquires Dark Fiber Group as independent carrier-neutral dark fibre entrant in GlobalConnect's Nordic geography — bifurcates Nordic fibre opportunity between integrated legacy platform (GlobalConnect at €8B) and greenfield hyperscaler-oriented build (Dark Fiber Group)
- Edition 12 (2026-05-21): GlobalConnect announces Kattegat cable — 92km Sweden-Denmark link, 288 strands, €11.9M investment, EU CEF2 co-funds €5.9M (50%), 2027 go-live; part of Bifrost programme targeting 3,000km+ new Nordic fibre; capex committed mid-sale to demonstrate active network investment thesis to prospective buyers

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
Status: dormant
Summary: End-2026 hard deadline for removing Huawei/ZTE from 5G core networks (packet core, IMS, IP/MPLS backbone, network management) — Deutsche Telekom, Vodafone Germany, and Telefonica Deutschland under binding bilateral agreements with Federal Ministry of Interior; Nokia and Ericsson are primary replacement vendors; 2029 deadline follows for radio access and transport networks (tens of thousands of base stations).
Changelog:
- Edition 10 (2026-05-07): 8 months to end-2026 core deadline — all three German operators in execution sprint; Nokia and Ericsson expanded German delivery capacity; 2029 radio access phase is larger and more expensive; Germany's bilateral agreement model being studied by France, Italy, and Netherlands for their own Chinese vendor reviews
- Edition 13 (2026-05-28): Thread moved to dormant — no operator-level update in 3 editions; end-2026 core deadline now 7 months out; next expected milestone is operator announcement of core network transition completion or Q3 2026 progress disclosure

## thread-id: kkr-helix-ai-infra
Beat: Capital & Deals
Status: active
Summary: KKR launched Helix Digital Infrastructure on April 30, 2026 — $10B+ committed capital (sovereign wealth fund + 2 strategic partners), Adam Selipsky (ex-AWS CEO) as Chair/CEO, Waldemar Szlezak (KKR global head of digital infrastructure) as CIO; mandate spans data centres, power generation and transmission, and connectivity; build-partner model for hyperscalers wanting capacity off-balance-sheet; further capital raises planned.
Changelog:
- Edition 12 (2026-05-21): KKR launches Helix Digital Infrastructure — $10B+ committed, Adam Selipsky (ex-AWS CEO) as Chair/CEO, Waldemar Szlezak as CIO; full-stack AI infrastructure build-partner mandate; first purpose-built platform of this type at institutional scale

## thread-id: dt-tmobile-merger
Beat: Western Europe
Status: active
Summary: Deutsche Telekom evaluating full all-share combination with T-Mobile US via new Irish-domiciled holding company — combined market cap ~$260–300B, 200M+ subscribers globally; DT already holds 53%+ of T-Mobile US; structure mirrors 2018 Linde-Praxair; talks described as early stage, no binding agreement signed; deal would be the largest in telecoms history.
Changelog:
- Edition 12 (2026-05-21): Deutsche Telekom reported to be evaluating full T-Mobile US combination — all-share deal via new holding company (~$260–300B combined market cap); Bloomberg confirmed late April 2026; early stage, no agreement; Ireland flagged as incorporation jurisdiction; Linde-Praxair structural template; antitrust complexity across FCC, DOJ, and European Commission

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
