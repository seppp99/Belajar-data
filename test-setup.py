import pandas as pd
import sys

print(f"python version: {sys.version.split()[0]}")
print(f"pandas version: {pd.__version__}")

df = pd.DataFrame({"hari":["senin"], "status":["siap"]})