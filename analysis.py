import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')

print("The shape of the given dataset is : " , df.shape)

print(df.columns)
print(df.head())

print("The number of movies and Tv shows are : " ,df['type'].value_counts())
print("The missing values : " , df.isnull().sum())
print("The top 10 countries are : " ,df['country'].value_counts().head(10))
print("The top 10 genres are : " , df['listed_in'].value_counts().head(10))
print('The most common ratings are :  ', df['rating'].value_counts())


df_clean = df.copy()

df_clean['director'] = df_clean['director'].fillna('unknown') #as directors are not NaN so we have to fill it by unknown
df_clean['cast'] = df_clean['cast'].fillna('unknown')
df_clean['country'] = df_clean['country'].fillna('unknown')

df_clean['date_added'] = pd.to_datetime(
    df_clean['date_added'],
    errors='coerce'
)

df_clean['year_added'] = df_clean['date_added'].dt.year

print(df_clean['year_added'].value_counts().head(10))

india = df_clean[df_clean['country'].str.contains('India',na=False)]

print("India : " , len(india))


usa = df_clean[df_clean['country'].str.contains('United States',na=False)]

print("USA : " , len(usa))

india_count = len(india)
usa_count = len(usa)

if india_count > usa_count:
    print('india has more content')
else:
    print('usa has more content')    

fig ,axes = plt.subplots(2,2,figsize=(15,10))
content_type = df['type'].value_counts()

axes[0,0].bar(content_type.index , content_type.values)
axes[0,0].set_title("Movies vs TV SHows on netflix")
axes[0,0].set_xlabel("Content type")
axes[0,0].set_ylabel('Count')



top_countries = df['country'].value_counts().head(10)

axes[0,1].barh(top_countries.index, top_countries.values)
axes[0,1].set_title("Top 10 countries by Netflix Content")
axes[0,1].set_xlabel('Number of Titles')
axes[0,1].set_ylabel('Country')
plt.tight_layout()


year_counts = df_clean['year_added'].value_counts().sort_index()
print(year_counts)



axes[1,0].plot(year_counts.index,
         year_counts.values,
         marker = 'o')

axes[1,0].set_title("Netflix content added over time")
axes[1,0].set_xlabel('Year')
axes[1,0].set_ylabel('Number of titles')
axes[1,0].grid()


top_genre = df_clean['listed_in'].value_counts().head(10)
print(top_genre)


axes[1,1].barh(top_genre.index , top_genre.values)

axes[1,1].set_title('Top 10 genres on Netflix')
axes[1,1].set_xlabel('Number of titles')
axes[1,1].set_ylabel('Genre')
plt.tight_layout()
plt.show()
