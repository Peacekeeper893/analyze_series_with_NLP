
import pandas as pd

# def load_subtitles_dataset(dataset_path):
#     df = pd.read_csv(dataset_path)
#     df['season_episode'] = (df['Season'].str.split(' ').str[1].astype(int) - 1) * 10 + df['Episode'].str.split(' ').str[1].astype(int)
#     df_a = df.drop(['Season','Episode','Name','Release Date','Episode Title'],axis=1)
#     df_a['Sentence'] = df_a['Sentence'].astype(str)
#     df_a = df_a.groupby('season_episode')['Sentence'].agg(' '.join).reset_index()
#     df_a.rename(columns={'Sentence':'Subtitles'},inplace=True)
#     return df_a



# With class
def load_subtitles_dataset(dataset_path):
    df = pd.read_csv(dataset_path)
    df['season_episode'] = (df['Season'].str.split(' ').str[1].astype(int) - 1) * 10 + df['Episode'].str.split(' ').str[1].astype(int)
    df_a = df.drop(['Season','Episode','Release Date','Episode Title'],axis=1)
    df_a['Sentence'] = df_a['Sentence'].astype(str)
    df_a.rename(columns={'Sentence':'Subtitles'},inplace=True)
    
    return df_a