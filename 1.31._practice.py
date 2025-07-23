import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt

irisdb= sns.load_dataset("iris")
titanicdb=sns.load_dataset("titanic")
penguinsdb=sns.load_dataset("penguins")

print(irisdb.head())
print(titanicdb.head())
print(penguinsdb.head())

irisx = irisdb["petal_length"]
irisy = irisdb["sepal_length"]

sns.scatterplot(x=irisx, y=irisy, hue=irisdb["species"])
plt.xlabel("Petal Length")
plt.ylabel("Sepal Length")
plt.title("Relación Petal Length vs Sepal Length (Iris)")
plt.show()

sns.countplot(x="class", hue="survived", data=titanicdb)
plt.title("Conteo de sobrevivientes y no sobrevivientes por clase")
plt.ylabel("Número de personas")
plt.xlabel("Clase")
plt.show()


sns.boxplot(x="species", y="body_mass_g", data=penguinsdb)
plt.xlabel("Species")
plt.ylabel("Body Mass (g)")
plt.title("Distribución de masa corporal por especie (Pingüinos)")
plt.show()


