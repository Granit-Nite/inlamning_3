import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from in3 import DataPlotter  # DataPlotter-klassen från in3.py filen

# CSV filen
file_path = r"C:\Code\Inlämning3\unlabelled_data.csv"

# DataPlotter-klassen och läs in data
plotter = DataPlotter(file_path)
plotter.read_data()


# Kollar positionen för varje punkt linjen y = -x
for x, y in zip(plotter.x_values, plotter.y_values):
    position = plotter.check_point_position(x, y)
    print(f"{position}")

# räknar ut om en punkt ligger till höger/ovan eller vänster/nedanför linjen
def check_point_position(x, y):
    linje_y = -x
    if y > linje_y:
        return 1  # höger/ovan
    else:
        return 0  # vänster/nedanför

#####################################################################


# Skapar en lista med klassificeringar (0 eller 1)
labels = [check_point_position(x, y) for x, y in zip(plotter.x_values, plotter.y_values)]

# Skapar en DataFrame och sparar till labelled_data.csv
df = pd.DataFrame({
    'x': plotter.x_values,
    'y': plotter.y_values,
    'label': labels  # 0 för vänster/nedanför, 1 för höger/ovan
})

# Sparar till filen
df.to_csv(r"C:\Code\Inlämning3\labelled_data.csv", index=False)

############################################################################

# Ritar graf2 med färg för klassificering
plt.xlabel('x')
plt.ylabel('y')

# Skapar en röd linje för y = -x
plotter.xpoints = np.array([-4, 4])
plotter.ypoints = np.array([4, -4])
plt.plot(plotter.xpoints, plotter.ypoints, color='r', label='y = -x')

# Separera punkter beroende på deras klass (0 eller 1) för att färga dem olika
class_0 = df[df['label'] == 0]
class_1 = df[df['label'] == 1]

# Ritar punkter för båda klasserna
plt.scatter(class_1['x'], class_1['y'], color='g', label='Höger/Ovan (1)')
plt.scatter(class_0['x'], class_0['y'], color='b', label='Vänster/Nedanför (0)')

plt.legend()
plt.show()
