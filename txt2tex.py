import pickle


def convert_back(filename):
    with open(filename, 'r') as fin:
        source = fin.read()
    # print(source)
    filename_base = filename.split('.')[0]
    with open (f'{filename_base}_latexitem', 'rb') as fp:
        x = pickle.load(fp)

    for key in x.keys():
        print(key, x[key])
        source = source.replace(key, x[key])
    #%%
    with open(f"{filename_base}_trans.tex", 'w') as txt_file:
        txt_file.write(source)

if __name__ == '__main__':
    filename = "file/main.txt"
    convert_back(filename)