def reverse_words(s: str) -> str:
    # split() without args trims ends and collapses multiple spaces
    words = s.split()
    return " ".join(reversed(words))

# Quick tests from the sheet
tests = [
    "the sky is blue",
    "  hello world  ",
    "a   good   example",
    "word",
    "    "
]
for t in tests:
    print(f"IN : {repr(t)}")
    print(f"OUT: {reverse_words(t)}\n")
