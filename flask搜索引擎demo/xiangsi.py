#!/usr/bin/env python
# -*- coding: utf-8 -*-

#根据搜索词进行tf-idf相似匹配度排行
import time
import pandas as pd
import multiprocessing as mp
from sklearn.feature_extraction.text import TfidfVectorizer

# 进程处理函数
def myfun(rawlist, result_dic):
    while rawlist:
        temp = rawlist.pop(0)
        search_text = temp[2]
        content = temp[1] + search_text
        # 建立TF-IDF矩阵：
        # 定义一个TF-IDF矢量化器对象。删除所有英文停止词，如'the'， 'a'
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        # 通过拟合和转换数据来构造所需的TF-IDF矩阵，TFIDF=TFxIDF,
        tfidf_matrix = tfidf_vectorizer.fit_transform([content])
        # TF=（某词在文档中出现的次数/文档的总词量,IDF=loge（语料库中文档总数/包含该词的文档数+1）
        word_score = 0
        # 拆分搜索词，计算累加idf值
        for word in search_text.split(' '):
            word_id = tfidf_vectorizer.vocabulary_.get(word, -1)
            if word_id != -1:
                word_score += tfidf_matrix.toarray()[0][word_id]
        result_dic[temp[0]] = word_score


search_text = 'twisted pet treat'
# 进程函数
def main():
    # 读取数据
    df = pd.read_excel('./patentdata.xlsx')
    # 进程数processes_num根据自己电脑的核数定
    processes_num = 2
    pool = mp.Pool(processes=processes_num)
    start_time = time.time()
    manager = mp.Manager()
    rawlist = manager.list()
    result_dic = manager.dict()
    num = df.shape[0]
    for i in range(num):
        content_t = df.loc[i, 'Content']
        id_t = df.loc[i, 'ID']
        rawlist.append([id_t, content_t, search_text])
    for i in range(processes_num):
        pool.apply_async(myfun, (rawlist, result_dic,))
    pool.close()
    pool.join()

    # 相似度排行个数
    same_coumt = 10
    dic_re = sorted(result_dic.items(), key=lambda x: x[1], reverse=True)[:same_coumt]
    fin_result = [id_r[0] for id_r in dic_re]
    print(f'相似ID：{fin_result}')
    print(time.time() - start_time)
    return fin_result

# 主函数
if __name__ == '__main__':
    fin_result = main()
