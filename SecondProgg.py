import pandas as pd
left = pd.read_csv("CAvideos.csv")
right = pd.read_csv("GBvideos.csv")

print(left.shape, right.shape)
#merged_data= pd.merge(left, right, on='video_id')

merged_data= pd.merge(left, right [['video_id', 'likes', 'views']], on='video_id', how='left' )
print(merged_data.head)