Appendix C (Transaction-Based Parameter Injection): The Revit API's TransactionManager sequence:
 (1) open transaction (unlock Revit database for writing);
 (2) calculate environmental metrics using LCI mapping;
 (3) force-write Carbon_Coefficient and Total_Embodied_Carbon values into element shared parameters;
 (4) log success or failure;
 (5) close transaction and commit changes.
 Carbon data persists with the .rvt file (no external links), is queryable in schedules, filters,
 and custom reports, propagates automatically when geometry updates, and enables near-real-time feedback in Properties palette.
 The try-except block serves as built-in quality assurance: if a wall lacks required parameters,
 the script logs a 'Failed' status rather than terminating the entire process.
Appendix D (Multi-Layer Assembly Extension):
 Proposed implementation iterating through CompoundStructure.GetLayers() to retrieve material ID and layer thickness for each layer,
 then calculating layer volume as: wall_area × layer_thickness × 0.0283168 (converting to m³), looking up the coefficient per material name,
 and accumulating a running carbon total before injecting the weighted aggregate into Total_Embodied_Carbon.
 This approach enables accurate calculation for composite assemblies (e.g., concrete structure + 150mm insulation + air barrier + cladding).
Appendix E (External Coefficient Database): Proposed CSV-based coefficient library with columns: Material, Region, CO2_per_m3, Source. Example entries:
 Concrete - C30 / Europe / 317.0 / Arenas & Shafique 2024;
 Concrete - C30 / North America / 390.6 / GaBi Professional; Rammed Earth / Global / 34.0 / Arenas & Shafique 2024;
 Rammed Earth / Europe / 29.1 / GaBi Aggregates (calculated). Python implementation uses pandas to load the CSV, filter by region,
 and generate the carbon_library dictionary — enabling non-programmers to update coefficients in Excel, maintaining regional libraries with version control,
 and supporting potential API integration with online EPD repositories such as EC3, Ökobaudat, and INIES.
