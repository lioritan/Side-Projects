
import numpy as np
from hmmlearn import hmm


def get_model(n_states=3, n_iter=100):
    #return hmm.GaussianHMM(n_components=n, covariance_type="full", n_iter=100)
    return hmm.MultinomialHMM(n_components=n_states, n_iter=n_iter)


def get_frequencies(freq_dist, n_states):
    frequencies = np.array([freq_dist.freq(i) for i in range(len(freq_dist.keys()))])
    emission_prob = np.stack([frequencies] * n_states)
    return emission_prob


def train_model(model, freqs, enc_words):
    model.emissionprob_ = freqs
    model.fit(enc_words)
    return model


def generate_words(trained_model, num_words, encoder):
    new_enc_words = trained_model.sample(num_words)[0]
    return np.squeeze(encoder.inverse_transform(new_enc_words))
