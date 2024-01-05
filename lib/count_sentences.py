class MyString:
    def __init__(self, value=""):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("The value must be a string.\n")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        replaced_value = self.value.replace('.', '@').replace('?', '@').replace('!', '@')
        sentences = replaced_value.split('@')
        sentences = [sentence for sentence in sentences if sentence]
        return len(sentences)
