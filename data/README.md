# Data Access Instructions

Dataset: Spotify Tracks Dataset
Source: Kaggle — maharshipandya/-spotify-tracks-dataset
License: CC0 (Public Domain)

## Download Instructions

Option A — Kaggle CLI:
    pip install kaggle
    kaggle datasets download -d maharshipandya/-spotify-tracks-dataset
    unzip spotify-tracks-dataset.zip -d data/
    rename the csv file to dataset.csv and place in data/

Option B — Manual:
    Visit: https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset
    Click Download and place the CSV as data/dataset.csv

## Data Description
- 114,000 tracks across 125 genres
- 20 columns including 13 numeric audio features
- Target variable: track_genre (filtered to top 10 genres)
- No personally identifiable information
