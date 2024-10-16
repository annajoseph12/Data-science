print("SJC23MCA-2017 : Anna S")
print("Batch : MCA 2023-25")
def gen_ngrams(text,wordsToCombine):
    words=text.split()
    output=[]
    for i in range(len(words)-wordsToCombine):
        output.append(words[i:i+wordsToCombine])
    return output
x=gen_ngrams(text='using the iris data set,implement the KNN algorithm',wordsToCombine=3)
print(x)