import numpy as np
import pandas as pd

numbers = np.array([10, 20, 30, 40, 50])
print("NumPy array:", numbers)
print("Addition:", numbers + 5)
print("Multiplication:", numbers * 2)
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))

data = {
    "Name": ["Aarav", "Meera", "Riya"],
    "Marks": [85, 92, 78]
}
frame = pd.DataFrame(data)
print("Pandas DataFrame:")
print(frame)
print("Average marks:", frame["Marks"].mean())
