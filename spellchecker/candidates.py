import Levenshtein


def compute_exp_likelihood(wordA: str, wordB: str, alpha: float = 0.5) -> float:
    """
    Computes levenshtein distance between two words and returns exponential likelihood.
    :param wordA: first comparison word
    :param wordB: second comparison word
    :param alpha: base term used to penalize increasing edits between words. defaults to a factor of 2.
    """
    dist = Levenshtein.distance(wordA, wordB)
    return alpha**dist

def get_candidates(vocab: list, observation: str, max_edits: int = 2) -> list:
    """Utility to get possible candidates from the word list with edit distance <= 2 by default."""
    return [word for word in vocab if Levenshtein.distance(observation, word) <= max_edits]
