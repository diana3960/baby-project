## Import the Data


```python
import pandas as pd 
import matplotlib.pyplot as plt

%matplotlib inline

```


```python
df = pd.read_csv("netflix_titles.csv")
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>show_id</th>
      <th>type</th>
      <th>title</th>
      <th>director</th>
      <th>cast</th>
      <th>country</th>
      <th>date_added</th>
      <th>release_year</th>
      <th>rating</th>
      <th>duration</th>
      <th>listed_in</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>s1</td>
      <td>Movie</td>
      <td>Dick Johnson Is Dead</td>
      <td>Kirsten Johnson</td>
      <td>NaN</td>
      <td>United States</td>
      <td>September 25, 2021</td>
      <td>2020</td>
      <td>PG-13</td>
      <td>90 min</td>
      <td>Documentaries</td>
      <td>As her father nears the end of his life, filmm...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>s2</td>
      <td>TV Show</td>
      <td>Blood &amp; Water</td>
      <td>NaN</td>
      <td>Ama Qamata, Khosi Ngema, Gail Mabalane, Thaban...</td>
      <td>South Africa</td>
      <td>September 24, 2021</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>2 Seasons</td>
      <td>International TV Shows, TV Dramas, TV Mysteries</td>
      <td>After crossing paths at a party, a Cape Town t...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>s3</td>
      <td>TV Show</td>
      <td>Ganglands</td>
      <td>Julien Leclercq</td>
      <td>Sami Bouajila, Tracy Gotoas, Samuel Jouy, Nabi...</td>
      <td>NaN</td>
      <td>September 24, 2021</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>1 Season</td>
      <td>Crime TV Shows, International TV Shows, TV Act...</td>
      <td>To protect his family from a powerful drug lor...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>s4</td>
      <td>TV Show</td>
      <td>Jailbirds New Orleans</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>September 24, 2021</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>1 Season</td>
      <td>Docuseries, Reality TV</td>
      <td>Feuds, flirtations and toilet talk go down amo...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>s5</td>
      <td>TV Show</td>
      <td>Kota Factory</td>
      <td>NaN</td>
      <td>Mayur More, Jitendra Kumar, Ranjan Raj, Alam K...</td>
      <td>India</td>
      <td>September 24, 2021</td>
      <td>2021</td>
      <td>TV-MA</td>
      <td>2 Seasons</td>
      <td>International TV Shows, Romantic TV Shows, TV ...</td>
      <td>In a city of coaching centers known to train I...</td>
    </tr>
  </tbody>
</table>
</div>



### About This Dataset
This dataset includes information about movies and TV shows that are available on Netflix. Each row in the dataset represents one title on the platform. The dataset contains details like the title name, whether it’s a movie or a TV show, the release year, rating, duration, and the country where it was produced. I chose this dataset because Netflix is something most people are familiar with, which makes it easier to explore patterns and trends in streaming content.

## Observing the Data


```python
df.shape
```




    (8807, 12)




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 8807 entries, 0 to 8806
    Data columns (total 12 columns):
     #   Column        Non-Null Count  Dtype 
    ---  ------        --------------  ----- 
     0   show_id       8807 non-null   object
     1   type          8807 non-null   object
     2   title         8807 non-null   object
     3   director      6173 non-null   object
     4   cast          7982 non-null   object
     5   country       7976 non-null   object
     6   date_added    8797 non-null   object
     7   release_year  8807 non-null   int64 
     8   rating        8803 non-null   object
     9   duration      8804 non-null   object
     10  listed_in     8807 non-null   object
     11  description   8807 non-null   object
    dtypes: int64(1), object(11)
    memory usage: 825.8+ KB
    


```python
df.describe(include="all")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>show_id</th>
      <th>type</th>
      <th>title</th>
      <th>director</th>
      <th>cast</th>
      <th>country</th>
      <th>date_added</th>
      <th>release_year</th>
      <th>rating</th>
      <th>duration</th>
      <th>listed_in</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>8807</td>
      <td>8807</td>
      <td>8807</td>
      <td>6173</td>
      <td>7982</td>
      <td>7976</td>
      <td>8797</td>
      <td>8807.000000</td>
      <td>8803</td>
      <td>8804</td>
      <td>8807</td>
      <td>8807</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>8807</td>
      <td>2</td>
      <td>8807</td>
      <td>4528</td>
      <td>7692</td>
      <td>748</td>
      <td>1767</td>
      <td>NaN</td>
      <td>17</td>
      <td>220</td>
      <td>514</td>
      <td>8775</td>
    </tr>
    <tr>
      <th>top</th>
      <td>s1</td>
      <td>Movie</td>
      <td>Dick Johnson Is Dead</td>
      <td>Rajiv Chilaka</td>
      <td>David Attenborough</td>
      <td>United States</td>
      <td>January 1, 2020</td>
      <td>NaN</td>
      <td>TV-MA</td>
      <td>1 Season</td>
      <td>Dramas, International Movies</td>
      <td>Paranormal activity at a lush, abandoned prope...</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>1</td>
      <td>6131</td>
      <td>1</td>
      <td>19</td>
      <td>19</td>
      <td>2818</td>
      <td>109</td>
      <td>NaN</td>
      <td>3207</td>
      <td>1793</td>
      <td>362</td>
      <td>4</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2014.180198</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8.819312</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1925.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2013.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2017.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2019.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2021.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### Observations on The Dataset
- The dataset has around 8,000 rows and 2 columns
- The dataset contains both movies and tv shows
- Some of the columns in the dataset have missing values, especially in the "Country" and the "Director" columns
- Most columns contain text-based information such as "title", "country", and "rating".


```python
df.isna().sum()

```




    show_id            0
    type               0
    title              0
    director        2634
    cast             825
    country          831
    date_added        10
    release_year       0
    rating             4
    duration           3
    listed_in          0
    description        0
    dtype: int64



- Some columns have missing values
- This is common for real datasets
- For this project, I have kept the data as is since the goal is to explore the dataset 

## Descriptive Summaries 


```python
df["type"].value_counts()
```




    type
    Movie      6131
    TV Show    2676
    Name: count, dtype: int64



- Netflix has more movies than TV shows 
- TV shows make up a smaller portion of the catalogue 


```python
df["rating"].value_counts().head(10)
```




    rating
    TV-MA    3207
    TV-14    2160
    TV-PG     863
    R         799
    PG-13     490
    TV-Y7     334
    TV-Y      307
    PG        287
    TV-G      220
    NR         80
    Name: count, dtype: int64




```python
df["release_year"].value_counts().sort_index().tail(10)
```




    release_year
    2012     237
    2013     288
    2014     352
    2015     560
    2016     902
    2017    1032
    2018    1147
    2019    1030
    2020     953
    2021     592
    Name: count, dtype: int64



## Visualizing The Data

### Graph 1: Movies VS TV Shows


```python
df["type"].value_counts().plot(kind="bar", color="thistle")
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()
```


    
![png](output_18_0.png)
    


The bar chart above shows:
- Netflix has more movies than TV shows
- TV shows make up a smaller portion 

### Graph 2: Titles Added Over Time


```python
df["release_year"].plot(kind="hist", bins=20, color="thistle")
plt.title("Distribution of Release Years")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.show()
```


    
![png](output_21_0.png)
    


The Histogram above shows that most of Netflix's content is from recent years, with only a few older titles.

### Graph 3: Top Countries


```python
df["country"].value_counts().head(10).plot(kind="bar", color="thistle")
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.show()
```


    
![png](output_24_0.png)
    


The bar chart above shows:

- The United States produces the largest number of titles on Netflix

- A small number of countries contribute most of the content on the platform

- This suggests that Netflix content is mainly concentrated in a few major production countries

### Overall Insights From Graphs:
- There are more movies than TV shows available on Netflix

- Most of the content on Netflix comes from the last 10 to 15 years

- A large portion of Netflix titles are produced in the United States

- Netflix content seems to be made mostly in a small number of countries


```python

```
