import streamlit as st 

st.title("NLP Text Analysis Application")
st.write("This NLP Text Analysis Application allows users to perform various text processing operations, including tokenization, n-grams generation, and word cloud visualization. By entering text, users can easily explore and analyze its components, enhancing their understanding of language structure and frequency. ")

st.subheader("Textual Tokens")

# Creating a text input box
user_input = st.text_input("Enter your text:")

# All tokenisation methods
from nltk.tokenize import word_tokenize
wt = word_tokenize(user_input)

from nltk.tokenize import  sent_tokenize
snt = sent_tokenize(user_input)

from nltk.tokenize import blankline_tokenize
blt = blankline_tokenize(user_input)

from nltk.tokenize import WhitespaceTokenizer
wst = WhitespaceTokenizer().tokenize(user_input)

from nltk.tokenize import wordpunct_tokenize
wpt = wordpunct_tokenize(user_input)

# Buttons to submit the input
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Word Tokens",help = "Displays individual words from the text."):
        if user_input:
            st.write("Word Tokens: ", wt)
        else:
            st.write("Please enter some text.")

    if st.button("Sentence Tokens", help="Splits the text into individual sentences."):
        if user_input:
            st.write("Sentence Tokens: ", snt)
        else:
            st.write("Please enter some text.")

with col2:        
    if st.button("Blankline Tokens", help="Displays tokens separated by blank lines."):
        if user_input:
            st.write("Blankline Tokens: ", blt)
        else:
            st.write("Please enter some text.")
            
    if st.button("Whitespace Tokens", help="Splits the text based on whitespace characters."):
        if user_input:
            st.write("Whitespace Tokens: ", wst)
        else:
            st.write("Please enter some text.")

with col3:        
    if st.button("Punctuation Tokens", help="Splits the text into tokens, including punctuation marks."):
        if user_input:
            st.write("Punctuation Tokens: ", wpt)
        else:
            st.write("Please enter some text.")
            
            
st.subheader("Sequential Tokens")

# All tokenisation methods bigram, trigram, ngram
import nltk
from nltk.util import bigrams, trigrams, ngrams

user_input_tokens = nltk.word_tokenize(user_input) if user_input else []

bigrams = list(nltk.bigrams(user_input_tokens))
trigrams = list(nltk.trigrams(user_input_tokens))


if st.button("Bigrams",help="Generates pairs of consecutive words from the text."):
    if user_input:
            st.write("Bigrams: ", bigrams)
    else:
            st.write("Please enter some text.")
            
if st.button("Trigrams",help="Generates groups of three consecutive words from the text."):
    if user_input:
            st.write("Trigrams: ", trigrams)
    else:
            st.write("Please enter some text.")

# if st.button("Ngrams"):
#     if user_input:
#         n = st.number_input("Enter value of n", min_value=1, value=1)
#         if n>=1:
#             ngrams = list(nltk.ngrams(user_input_tokens, n))
#             if ngrams:
#                 st.write(f"{n}-grams: ", ngrams)
#             else:
#                 st.write("No n-grams generated. Check your input.")
#         else:
#             st.write("Please enter a valid value for n.")
#     else:
#         st.write("Please enter some text to generate n-grams.")
     
ngrams_input = st.number_input("Enter value of n for Ngrams",min_value=1, step=1)
ngrams = list(nltk.ngrams(user_input_tokens, ngrams_input))
st.write("")
if st.button("Ngrams", help="Generates sequences of n consecutive words from the text, where n is specified."):
    if user_input:
            st.write(f"{ngrams_input}-grams: ", ngrams)
    else:
        st.write("Please enter some text.")


st.subheader("WordCloud")

from wordcloud import WordCloud
import matplotlib.pyplot as plt

if st.button("Generate", help="Generate a visual representation of word frequency from the text."):
    if user_input:
        wc = WordCloud(margin=1, background_color='black', colormap='Accent', mode='RGBA').generate(user_input)
        plt.imshow(wc, interpolation = 'quadric')
        plt.axis('off')
        plt.margins(x=0, y=0)
        st.pyplot(plt)

    else:
        st.write("Please enter some text.")


