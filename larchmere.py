"""Text statistics helpers for the Larchmere library."""


def word_frequencies(text):
    """Count how often each word appears in text, case-insensitive."""
    counts = {}
    for raw in text.split():
        word = raw.lower().strip(".,!?;:\"'()[]")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def top_n(text, n):
    """Return the n most common words as (word, count), ties broken alphabetically."""
    freqs = word_frequencies(text)
    ranked = sorted(freqs.items(), key=lambda kv: (-kv[1], kv[0]))
    return ranked[:n]
