import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class DataPlotter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.x_values = []
        self.y_values = []
    
    def read_data(self):
        """Läser in data från CSV-fil och delar upp den i x- och y-värden."""
        with open(self.file_path) as f_read:
            data = [line.strip().split(",") for line in f_read.readlines()]
            self.x_values = [float(pair[0]) for pair in data]
            self.y_values = [float(pair[1]) for pair in data]

    def print_data(self):
        """Skriver ut alla x- och y-värden från filen."""
        for x, y in zip(self.x_values, self.y_values):
            print(f"x: {x}, y: {y}")
            
            
    def check_point_position(self, x, y):
        if y < -x:
            return f"Punkt ({x}, {y}) är vänster/nedanför om linjen y = -x"
        elif y > -x:
            return f"Punkt ({x}, {y}) är höger/ovanför om linjen y = -x"
        else:
            return f"Punkt ({x}, {y}) ligger på linjen y = -x"
        

    def plot_data(self):
        """Skapar en scatter plot med data och en referenslinje."""
        plt.xlabel('x')
        plt.ylabel('y')
        
        # Referenslinje från x = -4 till x = 4
        xpoints = np.array([-4, 4])
        ypoints = np.array([4, -4])
        plt.plot(xpoints, ypoints, color='r', label='y = -x')
        
        # Scatter plot för data
        plt.scatter(self.x_values, self.y_values, color='b', label='Data points')
        
        # Visar legend och grafen
        plt.legend()
        plt.show()
        
        

# Användning av klassen
file_path = r"C:\Code\Inlämning3\unlabelled_data.csv"
plotter = DataPlotter(file_path)
plotter.read_data()
plotter.print_data()
plotter.plot_data()
