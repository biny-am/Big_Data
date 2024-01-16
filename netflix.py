# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset

data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/netflix_titles.csv')

# Explore the data structure
print(data.head())
print(data.info())

# Handle missing values 
data = data.dropna(subset=["type",'rating'])  

# Answering the questions:

# 1. Most popular type
type_counts = data["type"].value_counts()
plt.bar(type_counts.index, type_counts.values)
plt.xticks(rotation=90)
plt.xlabel("type")
plt.ylabel("Number of Titles")
plt.title("Most Popular type on Netflix")
plt.show()

# 2. Most common keywords
keywords_list = data["description"].str.split(",").explode().str.strip()
common_keywords = keywords_list.value_counts().head(10)  # Show top 0 keywords
sns.barplot(x=common_keywords.index, y=common_keywords.values)
plt.xticks(rotation=90)
plt.xlabel("Keyword")
plt.ylabel("Frequency")
plt.title("Most Common Keywords in Netflix Titles")
plt.show()

# 3. Most popular directors
director_counts = data["director"].value_counts()
plt.bar(director_counts.index[:10], director_counts.values[:10])  # Show top 10 directors
plt.xticks(rotation=90)
plt.xlabel("Director")
plt.ylabel("Number of Titles")
plt.title("Most Popular Directors on Netflix")
plt.show()

# 4. Most popular actors
actor_counts = data["cast"].str.split(",").explode().value_counts()
plt.bar(actor_counts.index[:10], actor_counts.values[:10])  # Show top 10 actors
plt.xticks(rotation=90)
plt.xlabel("Actor")
plt.ylabel("Number of Titles")
plt.title("Most Popular Actors on Netflix")
plt.show()



# Filter data for movies and TV shows separately
movies = data[data["type"] == "Movie"]
tv_shows = data[data["type"] == "TV Show"]

# Histograms
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.hist(movies["rating"], bins=10, edgecolor="black")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.title("Movie Rating Distribution")

plt.subplot(1, 2, 2)
plt.hist(tv_shows["rating"], bins=10, edgecolor="black")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.title("TV Show Rating Distribution")
plt.tight_layout()
