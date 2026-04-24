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
Summary: Gulf conflict disrupted 17 cables via Red Sea corridor; rerouting via Cape of Good Hope adding ~150ms latency; WorldLink $700M hybrid cable announced as first purpose-built bypass route via Iraq.
Changelog:
- Edition 1 (2026-03-15): Gulf conflict disrupts 17 Red Sea submarine cables; traffic rerouted via Cape of Good Hope
- Edition 5 (2026-04-11): WorldLink announced — $700M UAE-Iraq hybrid cable, 900Tbps, sub-100ms Europe-ME latency, bypasses Suez corridor

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
Summary: Meta, Microsoft, Equinix all signed or announced nuclear PPAs; FERC review of interconnection queue pending; UAE Barakah operational capacity cited as competitive advantage for Gulf DC buildout.
Changelog:
- Edition 2 (2026-04-04): Meta, Microsoft, Equinix announce nuclear PPA commitments; FERC interconnection review opens

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
Summary: VodafoneThree approved in UK; Goldman flags Italy, Sweden, Denmark, Germany as next consolidation candidates; Draghi Report framework cited as most permissive regulatory posture in a generation.
Changelog:
- Edition 3 (2026-04-04): VodafoneThree merger approved; regulatory posture shift confirmed; Goldman consolidation map published

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
Summary: Nordics satisfy all three AI infrastructure criteria simultaneously — low power cost (Sweden ~8p, Norway ~6p/kWh), grid access, and regulatory predictability; emerging as preferred European DC investment destination.
Changelog:
- Edition 6 (2026-04-24): Nordics cited as benchmark vs UK energy costs in Stargate UK pause analysis; structural advantage confirmed
