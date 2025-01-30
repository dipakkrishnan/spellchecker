# spellchecker

# Project Impetus

This project contains Python code that builds a small spellchecker. I'm building this mostly out of curiosity as this problem is generally pretty interesting for a couple reasons. First, there isn't a "correct" solution. Approaches are empirical in nature. Unless you index the entire corpus of written human text, it is still theoretically possible to distort a word without the ability to correctly identify it. Second, there are many ways to approach the problem with different levels of complexity. For example, to implement a simple spellchecker, conceptually you could start with the idea of edits between words and then scale up algorithmically to fitting probabilistic models. You could also model language using the idea of prefix tree to store related words. Another approach could consider building a graph-like structure to store words with edge weights between nodes capturing similarity. Most of the approaches require evaluting tradeoffs between chosen heuristics. It's a rich problem domain and quite instructive to build a solution iteratively from simpler to more complex techniques - evaluating performance at each step.

# Dependency Management

The project uses uv as its package manager. Find more information about uv here: https://docs.astral.sh/uv/. uv.lock represents the ground truth dependency state.

Run the following to setup a venv and download the relevant dependencies:
```
uv sync
```

# Datasets

This project leverages open datasets that you can find here: https://www.kaggle.com/datasets/bittlingmayer/spelling?resource=download. Web-scale datasets and custom logic to find corrections in web content is out of scope. However, the modeling techniques used should scale to larger datasets well.
