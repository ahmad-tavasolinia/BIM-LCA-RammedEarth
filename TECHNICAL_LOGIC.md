# Technical Logic

## How the Script Works

The workflow runs in three steps inside a Revit Python environment 
(pyRevit or Dynamo Python node).

**Step 1 — Material mapping**
A Python dictionary acts as a local LCI database, mapping Revit wall 
type names to cradle-to-gate carbon coefficients (kgCO₂e/m³). 
Coefficients are per cubic metre of finished material — density is 
already accounted for in these values and must not be multiplied 
separately.

**Step 2 — Volume extraction**
The script iterates through all wall instances using 
FilteredElementCollector. For each wall, it retrieves the wall type 
name via BuiltInParameter.SYMBOL_NAME_PARAM and the net volume via 
HOST_VOLUME_COMPUTED (which accounts for door and window voids). 
Revit stores volumes in cubic feet internally; the conversion factor 
0.0283168 converts to m³.

**Step 3 — Calculation and parameter injection**
Carbon is calculated as:

    Total_Embodied_Carbon = volume_m3 × carbon_coefficient

Results are written into two shared parameters on each wall element:
- `Carbon_Coefficient` — the kgCO₂e/m³ value for that wall type
- `Total_Embodied_Carbon` — the total kgCO₂e for that wall instance

The Transaction ensures changes are committed atomically. A try-except 
block logs failures per wall rather than terminating the full run.

## Proposed Extension: Multi-Layer Assemblies

Current implementation assumes each wall is a single material. 
For composite walls, the following approach would iterate through 
compound structure layers:

    for layer in wall.GetCompoundStructure().GetLayers():
        layer_thickness = layer.Width * 0.3048  # feet to metres
        layer_area = wall.get_Parameter(
            BuiltInParameter.HOST_AREA_COMPUTED).AsDouble() * 0.0929
        layer_volume_m3 = layer_area * layer_thickness
        material = doc.GetElement(layer.MaterialId)
        mat_name = material.Name if material else "Unknown"
        coeff = carbon_library.get(mat_name, 0.0)
        total_carbon += layer_volume_m3 * coeff

## Proposed Extension: External Coefficient Database

To allow non-programmers to update coefficients without editing code, 
a CSV-based library could replace the hard-coded dictionary:

| Material | Region | CO2_per_m3 | Source |
|---|---|---|---|
| Concrete - C30 | Europe | 317.0 | Arenas & Shafique 2024 |
| Concrete - C30 | North America | 390.6 | GaBi Professional |
| Rammed Earth | Global | 34.0 | Arenas & Shafique 2024 |
| Rammed Earth | Europe | 29.1 | GaBi (reconstructed) |

Python implementation using pandas:

    import pandas as pd
    df = pd.read_csv("coefficients.csv")
    region_df = df[df["Region"] == selected_region]
    carbon_library = dict(zip(region_df["Material"], 
                              region_df["CO2_per_m3"]))
