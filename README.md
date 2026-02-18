# BIM-LCA-RammedEarth
Python-native Revit integration for embodied carbon assessment of earthen construction.
# BIM-LCA Integration for Earthen Construction

This repository contains the Python-native workflow developed for the **10th International Conference on Researches in Science & Engineering**.

## Key Research Features
- **Direct Revit API Access:** Uses `FilteredElementCollector` for 0% variance in volume extraction.
- **Scientific vs. Default Data:** Implements a customizable coefficient library allowing for scientific overrides of commercial "Black Box" databases.
- **Real-time Feedback:** Updates Revit Shared Parameters synchronously during the design phase.

## Validation Ground Truth
- **Concrete C30:** 317.0 kgCO2e/m³ (Scientific Baseline)
- **Rammed Earth:** 34.0 kgCO2e/m³ (Scientific Baseline)
