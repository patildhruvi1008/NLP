import streamlit as st
from spellchecker import SpellChecker

# Initialize Streamlit app
st.title("Paragraph Corrector")

# User Input
paragraph_input = st.text_area("Enter a paragraph with spelling mistakes...")

# Button to Check Words
if st.button("Correct Paragraph"):
    spell = SpellChecker()
    words = paragraph_input.split()
    corrected_paragraph = []
    
    for word in words:
        clean_word = word.strip('.,!?;:()[]{}"\'')  # Remove punctuation for checking
        if clean_word == '':
            corrected_paragraph.append(word)
            continue
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

    # Joining the corrected paragraph
    corrected_text = ' '.join(corrected_paragraph)

    # Displaying results
    st.subheader("Original Paragraph:")
    st.write(paragraph_input)

    st.subheader("Corrected Paragraph:")
    st.write(corrected_text)
