import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import (
    FilteredElementCollector,
    BuiltInCategory,
    BuiltInParameter,
    Transaction
)

# ------------------------------------------------------------
# CARBON COEFFICIENT LIBRARY (kgCO2e per m3, cradle-to-gate)
# Source: Arenas & Shafique (2024), Sustainable Futures
# Note: coefficients are per m3 of finished material.
# Density must NOT be multiplied separately — it is already
# embedded in these per-volume values.
# ------------------------------------------------------------
carbon_library = {
    "Concrete - C30": 317.0,
    "Concrete - C55": 362.0,
    "Rammed Earth":    34.0,
    "Interior wall":    0.0
}

# Calibration factor for North American industry alignment
# Apply to final results when reporting against GaBi/Tally
CALIBRATION_FACTOR = 1.23  # derived from validation (optional)

doc = __revit__.ActiveUIDocument.Document


def calculate_embodied_carbon():
    walls = (
        FilteredElementCollector(doc)
        .OfCategory(BuiltInCategory.OST_Walls)
        .WhereElementIsNotElementType()
    )

    t = Transaction(doc, "Update Embodied Carbon")
    t.Start()

    results = []

    for wall in walls:
        try:
            # Get wall type name (matches Revit wall type string)
            wall_type = doc.GetElement(wall.GetTypeId())
            wall_name = wall_type.get_Parameter(
                BuiltInParameter.SYMBOL_NAME_PARAM
            ).AsString()

            # Get net volume (accounts for door/window voids)
            # Revit stores internally in cubic feet; convert to m3
            vol_param = wall.get_Parameter(
                BuiltInParameter.HOST_VOLUME_COMPUTED
            )
            if not vol_param:
                results.append(f"Skipped (no volume): {wall_name}")
                continue

            volume_m3 = vol_param.AsDouble() * 0.0283168

            # Look up coefficient; default to 0 if not in library
            coefficient = carbon_library.get(wall_name, 0.0)

            # Total embodied carbon = volume x coefficient
            # No density multiplication — coefficient is per m3
            total_carbon = volume_m3 * coefficient

            # Write results back to shared parameters
            coeff_param = wall.LookupParameter("Carbon_Coefficient")
            carbon_param = wall.LookupParameter("Total_Embodied_Carbon")

            if coeff_param and carbon_param:
                coeff_param.Set(float(coefficient))
                carbon_param.Set(float(total_carbon))
                results.append(f"OK: {wall_name} | "
                               f"{volume_m3:.2f} m3 | "
                               f"{total_carbon:.1f} kgCO2e")
            else:
                results.append(
                    f"Failed (shared parameters missing): {wall_name}"
                )

        except Exception as e:
            results.append(f"Error on wall: {str(e)}")

    t.Commit()
    return results


if __name__ == "__main__":
    output = calculate_embodied_carbon()
    for line in output:
        print(line)
