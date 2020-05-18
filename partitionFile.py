import pandas

# Reads a file and partitions it based on
# HEADER_VLUE creating multiple files.
filetohandle = './'
CSV_HEADER = ''
chunksize = 10 ** 6

def readFileWithPandas():
    print("Starting to crunch...")
    for chunk in pandas.read_csv(filetohandle, sep=',', header=0, skipinitialspace=True, chunksize=chunksize):
        print("Crunching...")
        uniquelist = list(chunk['REPLACE_THIS_TAG_VALUE'].unique())
        for i in uniquelist:
            f = chunk.loc[chunk['REPLACE_THIS_TAG_VALUE'] == i]
            f.to_csv(str(i)+'.csv', mode='a', index=False, sep=',')

readFileWithPandas()