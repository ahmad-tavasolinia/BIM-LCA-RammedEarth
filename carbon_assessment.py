import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

# 1. CORE CONFIGURATION (Scientific Coefficients)
# We use 317.0 for Concrete and 34.0 for RE as per Arenas & Shafique (2024)
carbon_library = {
    "Concrete - C30": 317.0, 
    "Rammed Earth": 34.0
}
DENSITY = 2200 # kg/m3 (Standard compacted density)

doc = __revit__.ActiveUIDocument.Document

def calculate_embodied_carbon():
    # Collector to find all structural walls
    walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType()
    
    t = Transaction(doc, "Update Embodied Carbon")
    t.Start()
    
    for wall in walls:
        # Get Material Name
        mat_id = wall.GetPrimaryMaterialId()
        material = doc.GetElement(mat_id)
        mat_name = material.Name if material else "Unknown"
        
        # Get Volume (Revit internal units are Cubic Feet, convert to m3)
        vol_param = wall.get_Parameter(BuiltInParameter.HOST_VOLUME_COMPUTED)
        volume_m3 = vol_param.AsDouble() * 0.0283168
        
        # Match material to our scientific library
        coeff = carbon_library.get(mat_name, 0)
        
        if coeff > 0:
            # Calculation logic
            total_gwp = volume_m3 * DENSITY * coeff
            
            # PUSH TO REVIT: Ensure you have a Shared Parameter named 'Live_GWP'
            gwp_param = wall.LookupParameter("Live_GWP")
            if gwp_param:
                gwp_param.Set(total_gwp)
    
    t.Commit()

if __name__ == "__main__":
    calculate_embodied_carbon()