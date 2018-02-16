
import data_reader
import hmm_model


def train_word_generator(source_path, n_states, n_iter):
    print("reading data!")
    words = data_reader.read_data_as_words(source_path)

    unique_words = data_reader.get_unique_words(words)
    print("encoding words")
    encoder = data_reader.get_encoder(unique_words)
    print("getting encoded words")
    encoded_words = data_reader.get_encoded_words(words, encoder)

    word_frequencies = data_reader.get_word_frequencies(encoded_words)
    model = hmm_model.get_model(n_states, n_iter)
    print("training model")
    trained_model = hmm_model.train_model(model,
                                          hmm_model.get_frequencies(word_frequencies, n_states),
                                          encoded_words)
    return trained_model, encoder


def generate_words(num_words_per_line, trained_model, encoder):
    print("generating new text!")
    generated_words = hmm_model.generate_words(trained_model, num_words_per_line, encoder)
    generated_text = " ".join(generated_words)
    return generated_text.split(".")


if __name__ == '__main__':
    trained_model, encoder = train_word_generator(r"data/test_data1.txt", 50, n_iter=500)
    print(generate_words(50, trained_model, encoder))
