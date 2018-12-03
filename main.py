import tqdm
import jieba
import os
import gensim
import codecs
from collections import Counter

#加载语料库
filename = '/home/fyz/nlp/fyz_word_embedding/corpus/sougou_corpus.txt'
fenci_file = "./corpus/souguo_seg.txt"
jieba.load_userdict("./names_separate.txt")
model_file = "./wiki.model"
bin_file = "./mix.word.300d.bin"
text_file = "./mix_dim_300.txt"
text_lines = []
line_str_result_list = []

if os.path.exists(fenci_file):
    print("导入分词文件......")
    with open(fenci_file, 'r') as f:
        for line in f.readlines():
            text_lines.append(line.strip().split())
else:
    f2 = open(fenci_file,'w')

    with open(filename, 'r') as f:
        dataset = f.readlines()
        for lines in tqdm.tqdm(dataset):
            line_result = []
            line = lines.split()
            for sentence in line :
                one_line = list(jieba.cut(sentence, cut_all=False))
                line_result.extend(one_line)
            line_str_result = " ".join(line_result)
            f2.write(line_str_result+'\n')
            text_lines.append(line_str_result.split())
            line_str_result_list.append(line_str_result)

    print('总共读入%d行文字' % (len(text_lines)))

#模型训练
print("模型训练......")
model = gensim.models.Word2Vec(size=300,min_count=1)

model.build_vocab(text_lines)

model.train(sentences=text_lines,total_examples = len(text_lines), epochs = 10)

model.save(model_file)

model.wv.save_word2vec_format(bin_file,binary=True)
#模型解析
print("模型解析......")
model = gensim.models.KeyedVectors.load_word2vec_format(bin_file,binary=True)

with codecs.open(text_file,'w') as f :
    for i,word in enumerate(model.vocab):
        f.write(word)
        f.write(" ")
        _vectors_ = []
        for vector in model.vectors[i]:
            _vectors_.append(vector)
        string = str(_vectors_).replace('[','')
        string = string.replace(']','')
        string = string.replace(',','')
        f.write(str(string)+"\n")
