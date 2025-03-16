import matplotlib.pyplot as plt
import numpy as np
import random   # for generating random numbers
import os
import codecs
import seaborn as sns
import pandas as pd

# Read the text from the .txt file in a string
text = open("mini-project/text.txt", encoding='utf-8').read()

text_utf8 = text.encode('utf-8')
text_utf8 = list(map(int, text_utf8))

# Function to generate a key of the same length as the text using random numbers for each character and ensure it is uniformly distributed using UTF-8 encoding
def make_key_utf8(text):    
    key = {}
    for i in range(len(text)):
        key[i] = random.randint(0, 255)
    return key

# Function to encrypt the text using the key using UTF-8 encoding
def encrypt_utf8(text, key):
    cipher = {}
    for i in range(len(text)):
        cipher[i] = text[i] ^ key[i]
    return cipher

# Function to decrypt the text using the key using UTF-8 encoding
def decrypt_utf8(cipher, key):
    decrypted_text = {}
    for i in range(len(cipher)):
        decrypted_text[i] = cipher[i] ^ key[i]
    return decrypted_text

# Function to plot the histogram of the text
def plot_histogram(title,data):
    frequencies = np.zeros(256)
    for i in range(len(data)):
        frequencies[(data[i])] += 1 
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel('Character')
    ax.set_ylabel('Frequency')
    plt.title(title)
    plt.bar(range(256), frequencies)

# Function to calculate the entropy of a given text or cypher
def entropy(data):
    frequencies = np.zeros(256)
    for i in range(len(data)):
        frequencies[(data[i])] += 1
    probabilities = frequencies / len(data)
    entropy = 0
    for i in range(256):
        if probabilities[i] > 0:
            entropy += probabilities[i] * np.log2(probabilities[i])
    return -entropy

# Function to plot a 3d bars plot off the joint pdf histogram of the text and the key

def plot_3d(text,key):
    frequencies = np.zeros((256,256))
    for i in range(len(text)):
        frequencies[(text[i])][(key[i])] += 1
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x_data, y_data = np.meshgrid(np.arange(256), np.arange(256))
    x_data = x_data.flatten()
    y_data = y_data.flatten()
    z_data = frequencies.flatten()
    ax.bar3d(x_data,y_data,np.zeros_like(z_data),1,1,z_data)
    ax.set_ylabel('Cipher')
    ax.set_xlabel('Message')
    ax.set_zlabel('Frequency')
    ax.set_title('Joint PDF Histogram of the Message and the Cipher')

def test(amount_of_characters):
    data = np.zeros(256)

    total_entropy = 0
    for j in range(amount_of_characters):
        entropy = 0
        for i in range(len(data)):
            entropy += (1/len(data)) * np.log2(1/(len(data)))
        total_entropy = total_entropy + entropy
    print('entropy:', -total_entropy)

    return 0    


print(type(text_utf8))
print( 'Size of the text', len(text_utf8))
key = make_key_utf8(text_utf8)
cypher = encrypt_utf8(text_utf8, key)
decrypted_text = decrypt_utf8(cypher, key)
if len(text_utf8) < 50:
    print('This is the key',key)
    print('This is the cypher',cypher)
    print('This is the decrypted text',decrypted_text)   

print('Entropy of the text:', entropy(text_utf8))
print('Entropy of the key:', entropy(key))
print('Entropy of the cypher:', entropy(cypher))
test(len(text_utf8))
print('Size of the key',len(key))
plot_histogram('Histogram of the text',text_utf8)
plot_histogram("Histogram of the key",key)
plot_histogram("Histogram of the cipher",cypher)
plot_histogram("Histogram of the decrypted text",decrypted_text)
plot_3d(cypher,text_utf8)
print(text == decrypted_text)
plt.show()
