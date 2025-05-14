#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ''
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        # Replace all sentence-ending punctuation with a common delimiter
        modified_value = re.sub(r'[.!?]', '|', self.value)
        # Split on the delimiter
        sentences = modified_value.split('|')
        # Filter out empty strings
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
