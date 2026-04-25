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
Summary: Gulf conflict disrupted 17 cables via Red Sea corridor; US-Iran conflict escalates with IRGC-linked media threatening 7 Hormuz cables serving GCC states at 90%+ dependency — dual-corridor closure with no historical precedent; WorldLink $700M hybrid bypass under construction but not yet operational.
Changelog:
- Edition 1 (2026-03-15): Gulf conflict disrupts 17 Red Sea submarine cables; traffic rerouted via Cape of Good Hope
- Edition 5 (2026-04-11): WorldLink announced — $700M UAE-Iraq hybrid cable, 900Tbps, sub-100ms Europe-ME latency, bypasses Suez corridor
- Edition 8 (2026-04-25): US-Iran conflict escalates to Hormuz; IRGC-linked media threatens 7 GCC submarine cables — dual-chokepoint closure with no historical precedent; no repair timeline while hostilities continue

## thread-id: coreweave-gpu-debt
Beat: Data Infrastructure
Status: active
Summary: CoreWeave's leveraged GPU model — $8.5B investment-grade facility (EP2), now $3.5B convertible raise alongside $35B Meta commitment and $66.8B contracted backlog; 9 of 10 top AI model providers on platform.
Changelog:
- Edition 2 (2026-04-04): CoreWeave closes $8.5B investment-grade GPU debt facility; institutional precedent set for GPU-as-collateral
- Edition 5 (2026-04-11): $21B Meta expansion + Anthropic deal in 48 hours; $3.5B convertible raise; backlog reaches $66.8B

## thread-id: nuclear-ppas-data-centres
Beat: Energy & Power
Status: active
Summary: Meta, Microsoft, Equinix all signed or announced nuclear PPAs; IEA confirms 485 TWh consumed globally in 2025 (+17%), Europe faces 70% growth by 2030; SMR conditional offtake pipeline grew from 25 GW to 45 GW in under four months; tech sector signed ~40% of all corporate renewable PPAs in 2025.
Changelog:
- Edition 2 (2026-04-04): Meta, Microsoft, Equinix announce nuclear PPA commitments; FERC interconnection review opens
- Edition 8 (2026-04-25): IEA publishes 2025 data — 485 TWh consumed globally (+17%); Europe faces +45 TWh (+70%) by 2030; SMR pipeline grew 25→45 GW in under four months; tech sector ~40% of all corporate renewable PPAs

## thread-id: sea-dc-buildout
Beat: Data Infrastructure
Status: active
Summary: AWS, Google, Microsoft all announced major SEA capex 2024–2025; power grid reliability identified as binding constraint; data localisation laws tightening in Indonesia, Vietnam, Thailand.
Changelog:
- Edition 2 (2026-04-04): Hyperscaler SEA capex wave confirmed; grid reliability flagged as primary bottleneck

## thread-id: nvidia-supply-crunch
Beat: Data Infrastructure
Status: active
Summary: Vera Rubin lead times 9–12 months; CoreWeave Meta deal incorporates first commercial Vera Rubin deployments; inference economics shifting as H100 supply normalises.
Changelog:
- Edition 2 (2026-04-04): Vera Rubin lead times 9–12 months; inference economics shifting
- Edition 5 (2026-04-11): First commercial Vera Rubin deployments confirmed in CoreWeave-Meta contract

## thread-id: european-telecom-consolidation
Beat: Western Europe
Status: active
Summary: VodafoneThree approved in UK; SFR: Orange/Bouygues/Iliad in €20.35B exclusive negotiations (France 4→3); TIM: Poste Italiane €10.8B bid, Italian state to hold 50%+ of €27B combined group; Goldman consolidation thesis confirmed across France and Italy simultaneously.
Changelog:
- Edition 3 (2026-04-04): VodafoneThree merger approved; regulatory posture shift confirmed; Goldman consolidation map published
- Edition 8 (2026-04-25): Orange/Bouygues/Iliad enter €20.35B exclusive SFR negotiations — France 4→3 operators; Poste Italiane launches €10.8B TIM bid — Italian state to control 50%+ of combined €27B revenue group; Goldman Italy thesis confirmed

## thread-id: us-semiconductor-tariffs
Beat: Data Infrastructure
Status: active
Summary: Phase 1 25% tariff on advanced chips since Jan 15 with data centre exemption; April 14 Phase 2 report deadline passed; July 1 data centre chip review is next milestone.
Changelog:
- Edition 4 (2026-04-05): Trump Section 232 order — 25% tariff on advanced chips, data centre exemption carved out
- Edition 5 (2026-04-11): April 14 Phase 2 report deadline tracked; July 1 next decision point

## thread-id: dc-valuation-reset
Beat: Capital & Deals
Status: active
Summary: Aligned Data Centers sold to BlackRock/AIP/MGX for $40B — largest DC acquisition ever, 140% above prior AirTrunk record; AIP targeting $100B total deployment; new pricing floor set for AI-capable DC assets.
Changelog:
- Edition 5 (2026-04-11): Macquarie exits Aligned at $40B to BlackRock/AIP/MGX; beats AirTrunk record by 140%; AIP opens $100B programme

## thread-id: uk-ai-energy-gap
Beat: UK & Ireland
Status: active
Summary: OpenAI paused Stargate UK citing industrial electricity at 24.67p/kWh (~4x US rates); UK AI Growth Zone energy discount mechanism unoperationalised; second operator pause would shift narrative to UK-systemic.
Changelog:
- Edition 6 (2026-04-24): OpenAI pauses Stargate UK indefinitely — energy cost and copyright regulation cited; 8,000-GPU north-east England deployment on hold

## thread-id: nordics-infra-advantage
Beat: Nordics
Status: active
Summary: Nordics satisfy all three AI infrastructure criteria simultaneously — low power cost (Sweden ~8p, Norway ~6p/kWh), grid access, and regulatory predictability; EQT launched €8B GlobalConnect sale (244,000km fibre, 23 DCs, 27 subsea cables) via Goldman Sachs — Antin among early bidders.
Changelog:
- Edition 6 (2026-04-24): Nordics cited as benchmark vs UK energy costs in Stargate UK pause analysis; structural advantage confirmed
- Edition 8 (2026-04-25): EQT launches €8B GlobalConnect sale — 244,000km fibre, 23 DCs, 27 subsea cables; Goldman Sachs mandated; Antin among early bidders; Nordic power cost advantage re-confirmed vs UK 24.67p/kWh

## thread-id: globalconnect-sale
Beat: Nordics
Status: active
Summary: EQT targeting €8B sale of GlobalConnect via Goldman Sachs — 244,000km fibre across Denmark, Norway, Sweden, Germany, Finland; 23 data centres, 27 subsea cables, 30,000 business customers; Antin Infrastructure Partners among early bidders; EQT selling as single integrated entity; new Åland cable completing 2026.
Changelog:
- Edition 8 (2026-04-25): EQT launches €8B GlobalConnect sale; Goldman Sachs mandated; Antin identified as early bidder; EQT to sell as single entity rather than break up integrated fibre-DC-subsea model
