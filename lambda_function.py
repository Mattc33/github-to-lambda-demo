import pandas as pd

def lambda_handler(event, context);
    data = {'col1': [1,2], 'col2': [3,4]}
    dataframe = pd.DataFrame(data=data)
    print(dataframe)
    print('Done x1')