# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:37:13 2024

@author: Cheslin van Wyk(SPU)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("movie_dataset.csv")




print(df.info())
print("-------------------")
print(df.describe())

# This is getting rid of the spaces in the column names
df.rename(columns=lambda x: x.strip().replace(" ", "_"), inplace=True)

# Check if there are any NaN
print(df.isna().sum())
print("-------------------")


# Drop the movies with nan revenue
df.dropna(inplace = True)
# Reset the index
df = df.reset_index(drop=True)

# Check if there are any NaN left should be 0
print(df.isna().sum())
print("-------------------")



# Question 1
higest_rated_movie = df.sort_values("Rating", ascending=False).iloc[0]
print(higest_rated_movie["Title"])

# Question 2
sum_rev = df["Revenue_(Millions)"].sum()
count_rev = df["Revenue_(Millions)"].count()
avg_rev =  sum_rev / count_rev
print(avg_rev)
print("---------------------------------")

# Question 3
movies_cond = df[df["Year"].apply(lambda x: x>=2015 and x <=2017)]
sum_movies_cond = movies_cond["Revenue_(Millions)"].sum()
count_movies_cond = movies_cond["Revenue_(Millions)"].count()
avg_rev_movies_cond = sum_movies_cond / count_movies_cond
print(avg_rev_movies_cond)
print("--------------------------------")

# Question 4, I dont find 198 in the options since I just dropped the NaN values but if I didnt drop it the answer is different
movies_rel_2016 = df[df["Year"] == 2016]
print(movies_rel_2016["Year"].count())
print("--------------------")

# Question 5
movies_rel_nolan = df[df["Director"] == "Christopher Nolan"]
print(movies_rel_nolan["Director"].count())
print("--------------------")

# Question 6
movies_rating_high = df[df["Rating"] >= 8.0]
print(movies_rating_high["Rating"].count())
print("--------------------")

# Question 7
nolan_movies_median = movies_rel_nolan["Rating"].median()
print(nolan_movies_median)
print("--------------------")

# Question 8 please note I got 2006 but i dropped cells before i dropped values its 2007
grouped_by_year = df.groupby("Year")
sum_group_movies = grouped_by_year["Rating"].sum()
count_group_movies = grouped_by_year["Rating"].count()
avg_group_movies = sum_group_movies / count_group_movies
year_movie_highest_avg = avg_group_movies.sort_values(ascending=False)

# Question 9 i get 382 because of the dropped cells if I comment out that I dropped the cells and run it i get 575
movies_made_2006 = count_group_movies.iloc[0]
movies_made_2016 = count_group_movies.iloc[-1]
print(((movies_made_2016-movies_made_2006)/movies_made_2006)*100)



# Question 10
actors_count = {}

for actors in df["Actors"].str.split(","):
    for actor in actors:
        actor = actor.strip()
        if actor in actors_count:
            actors_count[actor] = actors_count[actor] + 1
        else:
            actors_count[actor] = 1
            
actors_count_list = list(actors_count.items())

most_common_actor = pd.DataFrame(actors_count_list, columns=["Actor", "Count"])

print(most_common_actor.sort_values("Count",ascending=False).iloc[0])

# Question 11
genre_count = {}

for genres in df["Genre"].str.split(","):
    for genre in genres:
        genre = genre.strip()
        if genre in genre_count:
            genre_count[genre] = genre_count[genre] + 1
        else:
            genre_count[genre] = 1

amount_genres = len(genre_count)
genres = list(genre_count.items())


# Question 11
col = ["Rank","Title", "Genre", "Description", "Director", "Actors"]
df.drop(columns=col,inplace=True)
df.dropna(inplace=True)
print(df.info())

corr_imbd = df.corr()
print(corr_imbd)

plt.figure(figsize = (15,8))
sns.heatmap(corr_imbd , annot=True , annot_kws= {'size':12})
plt.title("Correlation Heatmap - IMBD" , fontsize = 20)
plt.xticks(fontsize = 15,rotation = 90)
plt.yticks(fontsize = 15)
plt.show()



