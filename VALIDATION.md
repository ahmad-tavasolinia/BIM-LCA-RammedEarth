# Validation

## Rammed Earth Coefficient

The academic coefficient (34 kgCO₂/m³) is sourced from Arenas & 
Shafique (2024), a cradle-to-gate LCA of Colombian earthen 
construction using SimaPro v8.4 and the Ecoinvent database, covering 
soil excavation, compaction, local transportation, and regional grid 
carbon intensity.

Since Tally's GaBi database has no pre-defined rammed earth category, 
validation used a reconstructed mix: 1,300 kg coarse aggregate + 
700 kg sand + 200 kg water + 0 kg Portland cement per m³ 
(density 2,200 kg/m³). GaBi yielded 29.1 kgCO₂/m³ — a 17% variance 
from the academic coefficient, attributable to regional context 
(Colombian vs. European production) and energy mix differences. 
Both values are valid for their respective contexts.

## Concrete C30 Coefficient

The academic coefficient (317 kgCO₂/m³) reflects European residential 
specifications: 280-320 kg cement/m³, 20-35% SCM replacement, under 
EN 206 efficiency-focused standards.

Tally's GaBi output for the same volume implied an effective 
coefficient of 390.6 kgCO₂/m³ — consistent with North American 
structural-grade concrete (335-390 kg cement/m³, 10-20% SCM, ACI 318 
standards). GaBi defaults to weighted averages across commercial and 
infrastructure applications rather than residential-grade minimums.

## Validation Results

Tool validated on a single-storey residential prototype 
(162.25 m², 34.59 m³ wall volume) against Tally (GaBi Professional).

| Metric | Result |
|---|---|
| Volume extraction variance | 0% |
| Carbon variance (industry-aligned coefficients) | 7.3% |
| Systematic offset across both materials | 17-19% |
| Comparative reduction estimate difference | 3.3 percentage points |

The 7.3% variance falls within standard LCA uncertainty ranges 
(±10% for cradle-to-gate assessments).

## Calibration

A calibration factor of ×1.23 (derived from 13,510 ÷ 10,965) 
can be applied for North American industry alignment. 
European projects can likely use academic coefficients without 
adjustment. Asian and other regional contexts should validate 
against local EPD databases.

## Scope Note

This tool calculates cradle-to-gate (A1-A3) embodied carbon only. 
It should not be used for whole-life carbon claims without 
incorporating construction (A4-A5), operational (B), and 
end-of-life (C) stages.
