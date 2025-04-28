import streamlit as st
from spellchecker import SpellChecker
import re

# Initialize Streamlit app
st.title("Paragraph Corrector")

# User Input
paragraph_input = st.text_area("Enter a paragraph with spelling mistakes...")

# Function to correct paragraph
def correct_paragraph(paragraph):
    spell = SpellChecker()
    
    # Regular expression to split words while keeping punctuation
    words = re.findall(r'\w+|[^\w\s]', paragraph)
    
    corrected_paragraph = []

    for word in words:
        # If the word is just punctuation, keep it
        if re.match(r'[^\w\s]', word):
            corrected_paragraph.append(word)
            continue
        
        # Strip punctuation for checking, if it exists
        clean_word = word.strip('.,!?;:()[]{}"\'')
        
        # Check if the word is misspelled
        if clean_word.lower() in spell:
            corrected_paragraph.append(word)
        else:
            candidates = list(spell.candidates(clean_word.lower()))
            if candidates:
                corrected_word = candidates[0]  # Take the first suggestion
                
                # Preserve the original punctuation and casing
                if word.istitle():
                    corrected_word = corrected_word.title()
                elif word.isupper():
                    corrected_word = corrected_word.upper()
                
                corrected_paragraph.append(corrected_word)
            else:
                corrected_paragraph.append(word)
    
    # Join the corrected words to form the final paragraph
    corrected_text = ''.join([f" {word}" if not word.startswith(tuple('.,!?;:()[]{}"\' ')) else word for word in corrected_paragraph]).strip()

    return corrected_text

# Button to Check Words
if st.button("Correct Paragraph"):
    corrected_text = correct_paragraph(paragraph_input)

    # Displaying results
    st.subheader("Original Paragraph:")
    st.write(paragraph_input)

    st.subheader("Corrected Paragraph:")
    st.write(corrected_text)
