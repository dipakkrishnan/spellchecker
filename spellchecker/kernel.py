from spellchecker.candidates import compute_exp_likelihood, get_candidates
from spellchecker.priors import RelativeFrequency
from collections import Counter
import re


def generate_correction(word: str, vocab: list, prior: RelativeFrequency):
    """
    Generates a correction for the word using Bayes rule to approximate the posterior.
    p(m|word) = p(word|m)*p(m) where m is the original word we want to find. take argmax of candidate probs.
    :param word: the distorted (or not) observation for which we want to find the most likely original word
    :param vocab: the word list
    :param prior: generates probability of observing a given word
    """
    candidates = get_candidates(vocab, word)
    probs = []
    for candidate in candidates:
        likelihood = compute_exp_likelihood(word, candidate)
        p_m = prior.get_relative_frequency(candidate)
        probs.append((likelihood*p_m, candidate))
    return max(probs, key=lambda x:x[0])[1]

def words(text): # simple cleaner from Norvig 
    return re.findall(r'\w+', text.lower())

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', required=True, help='pick a dataset in archive to utilize as base vocabulary')
    args = parser.parse_args()
    dataset = Counter(words(open(f"./archive/{args.dataset}.txt").read()))
    rf = RelativeFrequency(dataset)
    correction = generate_correction("recieve", dataset.keys(), rf)
    print(correction)
