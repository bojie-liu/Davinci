
from gensim.models import Word2Vec

_model_path = "/Users/joshualiu/dev/data/word2vec-for-wiki-master/wiki_model"

if __name__ == "__main__":
    model = Word2Vec.load(_model_path)
    rlt = model.doesnt_match("乔布斯 盖茨 黄仁勋 科技 学科".split())
    print(rlt)