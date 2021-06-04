# Parallel Sentence Aligner

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ml4asia/parallel-sentence-aligner/blob/main/parallel-sentence-aligner.ipynb)

This is a simple program which, given texts in two different languages, aligns the texts sentence-by-sentence based on their semantic closeness.

This relies on [spaCy sentenzier](https://spacy.io/api/sentencizer) and Google's [multilingual universal sentence encoder](https://tfhub.dev/google/universal-sentence-encoder-multilingual/3). You can run it on Google Colab.

Although the demo is for English and Chinese, it supports any languages supported by the sentence encoder (Arabic, Chinese-simplified, Chinese-traditional, English, French, German, Italian, Japanese, Korean, Dutch, Polish, Portuguese, Spanish, Thai, Turkish, Russian).

## Example

Input (taken from [Machine Learning Glossary](https://developers.google.com/machine-learning/glossary)): 

```
categorical data
Features having a discrete set of possible values. Blahblah. 

For example, consider a categorical feature named house style, 
which has a discrete set of three possible values: Tudor, ranch, 
colonial. By representing house style as categorical data, the
model can learn the separate impacts of Tudor, ranch, and colonial
on house price. Sometimes, values in the discrete set are mutually
exclusive, and only one value can be applied to a given example.
For example, a car maker categorical feature would probably permit
only a single value (Toyota) per example. Other times, more than
one value may be applicable. A single car could be painted more
than one different color, so a car color categorical feature would
likely permit a single example to have multiple values (for
example, red and white). Categorical features are sometimes called
discrete features.

Contrast with numerical data
```

```
分类数据

一种特征，拥有一组离散的可能值。

以某个名为 house style 的分类特征为例，该特征拥有一组离散的可能值（共三个），
即 Tudor, ranch, colonial。通过将 house style 表示成分类数据，相应模型可以
学习 Tudor、ranch 和 colonial 分别对房价的影响。有时，离散集中的值是互斥的，
只能将其中一个值应用于指定样本。例如，car maker 分类特征可能只允许一个样本有
一个值 (Toyota)。你好。在其他情况下，则可以应用多个值。一辆车可能会被喷涂多种
不同的颜色，因此，car color 分类特征可能会允许单个样本具有多个值（例如 red 和
white）。分类特征有时称为离散特征。

与数值数据相对。
完
```

Output:

```
---
categorical data Features having a discrete set of possible values.
分类数据  一种特征，拥有一组离散的可能值。
---
Blahblah.

---
For example, consider a categorical feature named house style,  which has a discrete set of three possible values: Tudor, ranch,  colonial.
以某个名为 house style 的分类特征为例，该特征拥有一组离散的可能值（共三个）， 即 Tudor, ranch, colonial。
---
By representing house style as categorical data, the model can learn the separate impacts of Tudor, ranch, and colonial on house price.
通过将 house style 表示成分类数据，相应模型可以 学习 Tudor、ranch 和 colonial 分别对房价的影响。
---
Sometimes, values in the discrete set are mutually exclusive, and only one value can be applied to a given example.
有时，离散集中的值是互斥的， 只能将其中一个值应用于指定样本。
---
For example, a car maker categorical feature would probably permit only a single value (Toyota) per example.
例如，car maker 分类特征可能只允许一个样本有 一个值 (Toyota)。
---

你好。
---
Other times, more than one value may be applicable.
在其他情况下，则可以应用多个值。
---
A single car could be painted more than one different color, so a car color categorical feature would likely permit a single example to have multiple values (for example, red and white).
一辆车可能会被喷涂多种 不同的颜色，因此，car color 分类特征可能会允许单个样本具有多个值（例如 red 和 white）。
---
Categorical features are sometimes called discrete features.
分类特征有时称为离散特征。
---
Contrast with numerical data
与数值数据相对。
---

完

```
