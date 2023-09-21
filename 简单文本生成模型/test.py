# -*- coding: utf-8 -*-
# time:2023/8/21 14:49
# file test.py
# outhor:czy
# email:1060324818@qq.com

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding

# Define your input text data
text = """Your input text goes here..."""

# Preprocessing
chars = sorted(list(set(text)))
char_to_idx = {char: idx for idx, char in enumerate(chars)}
idx_to_char = {idx: char for char, idx in char_to_idx.items()}
num_chars = len(chars)
seq_length = 50  # Length of input sequences
step = 3  # Stride between sequences

input_seqs = []
output_chars = []

for i in range(0, len(text) - seq_length, step):
    input_seqs.append(text[i:i + seq_length])
    output_chars.append(text[i + seq_length])

num_seqs = len(input_seqs)

# Convert input sequences and output characters to numerical representations
X = np.zeros((num_seqs, seq_length, num_chars), dtype=np.bool)
y = np.zeros((num_seqs, num_chars), dtype=np.bool)

for i, seq in enumerate(input_seqs):
    for t, char in enumerate(seq):
        X[i, t, char_to_idx[char]] = 1
    y[i, char_to_idx[output_chars[i]]] = 1

# Build the RNN model
model = Sequential([
    LSTM(128, input_shape=(seq_length, num_chars)),
    Dense(num_chars, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam')

# Training the model
model.fit(X, y, batch_size=128, epochs=50)

# Generating text using the trained model
start_idx = np.random.randint(0, len(text) - seq_length)
seed_text = text[start_idx:start_idx + seq_length]

generated_text = seed_text

for _ in range(200):  # Generate 200 characters
    x_pred = np.zeros((1, seq_length, num_chars))
    for t, char in enumerate(seed_text):
        x_pred[0, t, char_to_idx[char]] = 1

    preds = model.predict(x_pred, verbose=0)[0]
    next_char_idx = np.random.choice(num_chars, p=preds)
    next_char = idx_to_char[next_char_idx]

    generated_text += next_char
    seed_text = seed_text[1:] + next_char

print(generated_text)

