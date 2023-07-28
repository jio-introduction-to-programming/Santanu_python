
def persist_data(data, filename):
    file = open(filename,'w')
    file.write(data)
    file.close()  # Use Python built-in functions to write 'data' to 'filename'

def read_file(filename):
    file = open(filename,'r')
    print(file.read())
    file.close()
      # Use Python built-in functions to read contents of 'filename' and print them to screen

def write_file(filename, data):
    file = open(filename,'w')
    file.write(data)
    file.close()  # Use Python built-in functions to write 'data' to 'filename'

def delete_file(filename):
    import os
    os.remove(filename)  # Use Python built-in functions to delete 'filename'

def overwrite_file(filename, data):
    file = open(filename,'w')
    file.write(data)
    file.close()  # Use Python built-in functions to overwrite 'filename' with 'data'

def append_file(filename, data):
    file = open(filename,'a')
    file.write(data)
    file.close()  # Use Python built-in functions to append 'data' to 'filename'

def write_binary_file(filename, data):
    file = open('filename.bin','wb')
    file.write(b'data')
    file.close()  # Use Python built-in functions to write 'data' as binary to 'filename'

def read_image_file(filename):
    import cv2
    img = cv2.imread('filename.jpg')
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  # Use OpenCV to read 'filename' as an image

def read_csv_file(filename):
    import pandas as pd
    df=pd.read_csv('filename.csv')  # Use Pandas to read 'filename' as a csv

def write_csv_file(filename, df):
    import pandas as pd
    df = pd.Dataframe({'A': [1,2,3], 'B': [4,5,6]})
    df.to_csv('filename.csv', index=False)  # Use Pandas to write dataframe 'df' to 'filename'

def read_json_file(filename):
    import json
    with open(filename,'r')as filename:
        data = json.load(filename)  # Use json to read 'filename' as a json

def write_json_file(filename, data):
    import json
    with open(filename,'w')as filename:
        json.dump(data,filename)  # Use json to write 'data' to 'filename'

def write_pickle_file(filename, data):
    import pickle
    with open(filename,'wb')as filename:
        pickle.dump(data,filename)  # Use pickle to write 'data' to 'filename'

def read_pickle_file(filename):
    import pickle
    with open(filename,'rb') as filename:
        df=pickle.load(filename)  # Use pickle to read 'filename'
