import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Not Available', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)

# Convert date column
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

print("Data cleaned successfully!")

# Count Movies vs TV Shows
print("\nType Count:")
print(df['type'].value_counts())

# Most common rating
print("\nMost common rating:")
print(df['rating'].value_counts().head())

# Top 10 countries
print("\nTop countries:")
print(df['country'].value_counts().head(10))

import matplotlib.pyplot as plt
import seaborn as sns

# Plot Movies vs TV Shows
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows on Netflix")
plt.savefig("movies_vs_tvshows.png")
plt.show()

# ------------------ TOP GENRES ------------------

# Split genres (listed_in column)
genres = df['listed_in'].str.split(', ').explode()

top_genres = genres.value_counts().head(10)

# Plot
top_genres.plot(kind='bar')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_genres.png")
plt.show()

# ------------------ YEAR-WISE TREND ------------------

# Extract year from date_added
df['year_added'] = df['date_added'].dt.year

year_data = df['year_added'].value_counts().sort_index()

# Plot
year_data.plot(kind='line', marker='o')
plt.title("Content Added Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Shows")

plt.tight_layout()
plt.savefig("year_trend.png")
plt.show()
