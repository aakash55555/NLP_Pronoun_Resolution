import pandas as pd;

from datasets import load_dataset
dataset = load_dataset(
   'winogrande', 'winogrande_l', split='train')


smaller_dataset = dataset.filter(lambda e, i: i<5000, with_indices=True)

n = 5000

total_phrases = pd.Series(smaller_dataset[:n]['sentence'])
all_option1 = pd.Series(smaller_dataset[:n]['option1'])
all_option2 = pd.Series(smaller_dataset[:n]['option2'])
all_answers = pd.Series(smaller_dataset[:n]['answer'])
video_id = pd.Series([ "development_new"+str(count) for count in range(1,n+1)])
empty0 = pd.Series([],dtype="object")
empty1 = pd.Series([],dtype="object")
empty2 = pd.Series([],dtype="object")
empty3 = pd.Series([],dtype="object")
sent1 = pd.Series([],dtype="object")
sent2 = pd.Series([],dtype="object")
gold_source = pd.Series([], dtype="object")

combined_dataframe = pd.concat([video_id, total_phrases,gold_source, sent1, sent2, all_option1, all_option2, empty2, empty3, all_answers], axis = 1)
combined_dataframe = combined_dataframe.rename(
    columns={0: 'video-id', 1:'startphrase', 2: 'gold-source', 3:'sent1', 4:'sent2', 5:'ending0', 6:'ending1', 7:'ending2', 8:'ending3', 9:'label'
    })

combined_dataframe[['sent1','sent2']] = combined_dataframe.startphrase.str.split("_",expand=True)
combined_dataframe['fold-ind'] = 1000
combined_dataframe['gold-source'] = "gold"
combined_dataframe = combined_dataframe[['video-id', 'fold-ind', 'startphrase', 'sent1', 'sent2', 'gold-source', 'ending0', 'ending1', 'ending2', 'ending3', 'label']]
# print(combined_dataframe)
combined_dataframe.to_csv("output/test.csv")
print("\nCheck test.csv for output")