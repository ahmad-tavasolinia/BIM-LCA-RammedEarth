# BIM-LCA-RammedEarth

A lightweight Python tool for embodied carbon assessment of earthen 
and conventional construction, embedded directly in Autodesk Revit.

## What It Does

Extracts wall volumes from a Revit model, maps them to peer-reviewed 
cradle-to-gate carbon coefficients, and writes the results back into 
the model as persistent shared parameters — making embodied carbon 
visible in schedules, the Properties palette, and filters without 
any external software.

## Key Features

- **Revit-native**: No external LCA software or plugins required
- **Transparent coefficients**: All values traceable to peer-reviewed 
  sources, not proprietary databases
- **Earthen materials included**: Rammed earth explicitly supported 
  alongside concrete — absent from most commercial tools
- **Real-time feedback**: Results update when wall types or geometry 
  change
- **Open source**: Full logic readable and modifiable by anyone

## Carbon Coefficients (Cradle-to-Gate, A1-A3)

| Material | Coefficient | Source |
| Concrete C30 | 317.0 kgCO₂e/m³ | Arenas & Shafique (2024) |
| Concrete C55 | 362.0 kgCO₂e/m³ | Arenas & Shafique (2024) |
| Rammed Earth | 34.0 kgCO₂e/m³ | Arenas & Shafique (2024) |

A 17-19% systematic offset exists between these academic coefficients 
and commercial databases (GaBi, Ecoinvent) due to regional mix design 
differences and database categorization. See VALIDATION.md for 
details. A calibration factor of ×1.23 can be applied for 
North American industry alignment.

## Limitations

- Cradle-to-gate (A1-A3) only — does not cover construction, use 
  phase, or end-of-life
- Validated on a single residential case study with two materials
- Each wall assumes a single material type (multi-layer extension 
  proposed in TECHNICAL_LOGIC.md)
- Requires basic Python and Revit API familiarity to adapt

## Repository Contents

- `carbon_assessment.py` — main script
- `TECHNICAL_LOGIC.md` — implementation notes and proposed extensions
- `VALIDATION.md` — coefficient sources and validation against Tally
