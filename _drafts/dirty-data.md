

I used "from difflib import get_close_matches" to define which restaurant in the dataset is the best match with the input. for example:
get_close_matches('In N Out', ["McDonald's", 'Subway', 'Taco Bell', 'In-n-Out'])
The result is: 'In-n-Out'

## String similarity

What do you mean by similarity?

Edit distance

Spacy [semantic similarity][1]

[difflib][5]
[difflib.get_close_matches()][6]
[difflib.ratio()][7] measures similarity

trigram, n-gram 

https://pypi.org/project/fuzzy-match/
https://github.com/darwinagain/fuzzy-match


https://bergvca.github.io/2017/10/14/super-fast-string-matching.html


[Methods for Matching English Language Addresses][8] Keshav Ramani and Daniel Borrajo



[1]: https://spacy.io/usage/linguistic-features#vectors-similarity
[2]: https://github.com/jamesturk/jellyfish
[3]: https://github.com/rapidfuzz/RapidFuzz
[4]: https://github.com/seatgeek/thefuzz
[5]: https://docs.python.org/3/library/difflib.html
[6]: https://docs.python.org/3/library/difflib.html#difflib.get_close_matches
[7]: https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.ratio
[8]: https://arxiv.org/html/2403.12092v1
[9]: https://github.com/dedupeio/dedupe

