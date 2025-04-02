# This script checks if the required libraries are installed in the 
# environment. Run this script to verify the setup once the environment is 
# created and activated, and the required libraries are installed.

# Run this file in a terminal with the command:
# On Linux:
# `python "00_Setup/00D_Environment Test.py"`
# On Windows:
# `python "00_Setup\00D_Environment Test.py"`

# Try to import the required libraries and catch ImportError exceptions.
failed_libraries = []
try:
    import numpy as np
except ImportError:
    failed_libraries.append("numpy")

try:
    import pandas as pd
except ImportError:
    failed_libraries.append("pandas")

try:
    import geopandas as gpd
except ImportError:
    failed_libraries.append("geopandas")

try:
    import linref as lr
except ImportError:
    failed_libraries.append("linref")

# If any libraries are missing, print a message and list them.
if failed_libraries:
    print("\nThe following libraries are missing:")
    for lib in failed_libraries:
        print(f"- {lib}")
    print("\nPlease install the missing libraries to proceed.\n")
# If all libraries are present, print a success message.
else:
    print("\nEnvironment has been setup correctly!\n")