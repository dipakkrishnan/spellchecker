from collections import Counter


class RelativeFrequency:

    def __init__(self, vocab: list):
        self.vocab = vocab
        self.counter = Counter(vocab)

    def get_relative_frequency(self, word: str) -> float:
        """Returns the probability of observing a word in the vocabulary."""
        return self.counter[word] / len(self.vocab)
