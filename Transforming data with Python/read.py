import pandas as pd
def load_data():
    df = pd.read_csv("hn_stories.csv")
    df.columns = ['submission_time','upvotes','url','headline']
    #print(df.columns)
    return df
    
if __name__ == "__main__":
    df = load_data()
    print(df.columns)