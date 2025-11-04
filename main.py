from sklearn.linear_model import LinearRegression

# Erstelle ein einfaches Dataset
X = [[1], [2], [3]]  # Eingabewerte
y = [2, 4, 6]        # Ausgabewerte

# Trainiere das Modell
model = LinearRegression()
model.fit(X, y)

# Mache eine Vorhersage
print("Vorhersage für x=4:", model.predict([[4]]))

