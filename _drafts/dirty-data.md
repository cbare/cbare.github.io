

I used "from difflib import get_close_matches" to define which restaurant in the dataset is the best match with the input. for example:
get_close_matches('In N Out', ["McDonald's", 'Subway', 'Taco Bell', 'In-n-Out'])
The result is: 'In-n-Out'

## String similarity

What do you mean by similarity?

Edit distance

Spacy [semantic similarity][1]

[1]: https://spacy.io/usage/linguistic-features#vectors-similarity
[2]: https://github.com/jamesturk/jellyfish
[3]: https://github.com/rapidfuzz/RapidFuzz
[4]: https://github.com/seatgeek/thefuzz
