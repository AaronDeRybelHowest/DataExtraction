"""
Mining datasets for finetuning the GPT-2 mini model
for text generation.
"""
import pandas as pd
import glob

def extract_data(dir,col, out):
    '''
    Extracts all csv data from a directory and
    saves it in a textfile.
    :param dir: directory path string
    :param col: column to extract from
    :param out: output path string
    :return:
    '''
    path = dir
    all_files = glob.glob(path + "/*.csv")

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)

    frame = pd.concat(li, axis=0, ignore_index=True)

    df_snippets = frame[col]
    df_snippets.to_csv(out, header=None, index=None, sep=' ', mode='a')

#the new york times dataset
extract_data(r'nyt-snippets/','snippet','snippets.txt')
extract_data(r'nyt-comments/','commentBody','comments.txt')

# other datasets ...
