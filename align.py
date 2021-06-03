import tensorflow_hub as hub
import numpy as np
import tensorflow_text

en_texts = [
    "categorical data",
    "Features having a discrete set of possible values.",
    "hogefuga",
    "For example, consider a categorical feature named house style, which has a discrete set of three possible values: Tudor, ranch, colonial.",
    "By representing house style as categorical data, the model can learn the separate impacts of Tudor, ranch, and colonial on house price.",
    "Sometimes, values in the discrete set are mutually exclusive, and only one value can be applied to a given example.",
    "For example, a car maker categorical feature would probably permit only a single value (Toyota) per example.",
    "Other times, more than one value may be applicable.",
    "A single car could be painted more than one different color, so a car color categorical feature would likely permit a single example to have multiple values (for example, red and white).",
    "Categorical features are sometimes called discrete features.",
    "Contrast with numerical data."
]

zh_texts = [
    "分类数据",
    "一种特征，拥有一组离散的可能值。",
    "以某个名为 house style 的分类特征为例，该特征拥有一组离散的可能值（共三个），即 Tudor, ranch, colonial。",
    "通过将 house style 表示成分类数据，相应模型可以学习 Tudor、ranch 和 colonial 分别对房价的影响。",
    "有时，离散集中的值是互斥的，只能将其中一个值应用于指定样本。",
    "例如，car maker 分类特征可能只允许一个样本有一个值 (Toyota)。",
    "垃圾句子",
    "在其他情况下，则可以应用多个值。",
    "一辆车可能会被喷涂多种不同的颜色，因此，car color 分类特征可能会允许单个样本具有多个值（例如 red 和 white）。",
    "分类特征有时称为离散特征。",
    "与数值数据相对。",
    "完"
]

def main():
    embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3")
    en_result = embed(en_texts)
    zh_result = embed(zh_texts)
    sims = np.inner(en_result, zh_result)
    print(sims)

    costs = np.zeros((len(en_texts)+1, len(zh_texts)+1))
    pointers = np.zeros((len(en_texts)+1, len(zh_texts)+1), dtype=int)

    for i in range(1, len(en_texts)+1):
        costs[i, 0] = costs[i-1, 0] + 1.
    
    for j in range(1, len(zh_texts)+1):
        costs[0, j] = costs[0, j-1] + 1.

    for i in range(1, len(en_texts)+1):
        for j in range(1, len(zh_texts)+1):
            choices = [
                (costs[i-1, j-1] + (1. - sims[i-1, j-1]), 1),
                (costs[i-1, j] + 1., 2),
                (costs[i, j-1] + 1., 3)
            ]
            best_choice = sorted(choices, key=lambda x: x[0])[0]
            costs[i, j], pointers[i, j] = best_choice

    aligned = []
    i, j = len(en_texts), len(zh_texts)
    while i > 0 or j > 0:
        if pointers[i, j] == 1:
            i -= 1
            j -= 1
            aligned.append((en_texts[i], zh_texts[j]))
        elif pointers[i, j] == 2:
            i -= 1
            aligned.append((en_texts[i], ''))
        elif pointers[i, j] == 3:
            j -= 1
            aligned.append(('', zh_texts[j]))

    aligned.reverse()
    print(aligned)

if __name__ == '__main__':
    main()
