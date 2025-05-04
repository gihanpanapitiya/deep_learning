from numpy import random

# encoder representations of four different words
word_1 = np.array([1, 0, 0])
word_2 = np.array([0, 1, 0])
word_3 = np.array([1, 1, 0])
word_4 = np.array([0, 0, 1])



# generating the weight matrices
random.seed(42) # to allow us to reproduce the same attention values
W_Q = random.randint(3, size=(3, 3))
W_K = random.randint(3, size=(3, 3))
W_V = random.randint(3, size=(3, 3))

words = np.array([word_1, word_2, word_3, word_4])

words

# generating the queries, keys and values
Q = words @ W_Q
K = words @ W_K
V = words @ W_V

Q

word_1@W_Q

word_2@W_Q

word_3@W_Q

word_4@W_Q







# scoring the query vectors against all key vectors
scores = Q @ K.transpose()

scores

K.shape[1]

from scipy.special import softmax

# computing the weights by a softmax operation
weights = softmax(scores / K.shape[1] ** 0.5, axis=1)

sum(weights[0])

# computing the attention by a weighted sum of the value vectors
attention = weights @ V

attention


#=========
embed = torch.nn.Embedding(4, embed_dim, 0)
# Next, lets's create the embeddings for each token. these embeddings can be considered as feature vectors that represent the tokens. To create the embeddings, we will use [`torch.nn.Embedding`](https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html) class. The first three parameters to this class are,
# - number of embeddings – how many unique tokens we have, 
# - embedding dimention – how many elements are in the embedding vector or feature vector,
# - padding index - the token that should be considered as the padding token.