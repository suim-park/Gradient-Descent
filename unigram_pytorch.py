"""Pytorch."""
import nltk
import numpy as np
from numpy.typing import NDArray
import torch
from typing import List, Optional
from torch import nn
import matplotlib.pyplot as plt


FloatArray = NDArray[np.float64]


def onehot(vocabulary: List[Optional[str]], token: Optional[str]) -> FloatArray:
    """Generate the one-hot encoding for the provided token in the provided vocabulary."""
    embedding = np.zeros((len(vocabulary), 1))
    try:
        idx = vocabulary.index(token)
    except ValueError:
        idx = len(vocabulary) - 1
    embedding[idx, 0] = 1
    return embedding


def logit(x: FloatArray) -> FloatArray:
    """Compute logit (inverse sigmoid)."""
    return np.log(x) - np.log(1 - x)


def normalize(x: torch.Tensor) -> torch.Tensor:
    """Normalize vector so that it sums to 1."""
    return x / torch.sum(x)


def loss_fn(p: float) -> float:
    """Compute loss to maximize probability."""
    return -p


class Unigram(nn.Module):
    def __init__(self, V: int):
        super().__init__()

        # construct initial s - corresponds to uniform p
        s0 = logit(np.ones((V, 1)) / V)
        self.s = nn.Parameter(torch.tensor(s0.astype("float32")))

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        # convert s to proper distribution p
        p = normalize(torch.sigmoid(self.s))

        # compute log probability of input
        return torch.sum(input, 1, keepdim=True).T @ torch.log(p)


def gradient_descent_example():
    """Demonstrate gradient descent."""
    # generate vocabulary
    vocabulary = [chr(i + ord("a")) for i in range(26)] + [" ", None]

    # generate training document
    text = nltk.corpus.gutenberg.raw("austen-sense.txt").lower()

    # tokenize - split the document into a list of little strings
    tokens = [char for char in text]

    # generate one-hot encodings - a V-by-T array
    encodings = np.hstack([onehot(vocabulary, token) for token in tokens])

    # convert training data to PyTorch tensor
    x = torch.tensor(encodings.astype("float32"))

    # define model
    model = Unigram(len(vocabulary))

    # set number of iterations and learning rate
    num_iterations = 1000  # SET THIS
    learning_rate = 0.01  # SET THIS

    # make an empty list to store loss value of each iteration
    loss_all = []

    # train model
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    for _ in range(num_iterations):
        p_pred = model(x)
        loss = -p_pred
        loss.backward(retain_graph=True)
        optimizer.step()
        optimizer.zero_grad()

        # store every loss value to the list, use append(), item() to save it
        loss_all.append(loss.item())

    # find the optimal probabilities
    sum_char = [1 for _ in range(len(encodings))]
    for i in range(len(encodings)):
        sum_char[i] = sum(encodings[i])
    sum_all = sum(sum_char)
    optimal_prob = (
        torch.tensor(sum_char) / sum_all
    )  # optimal probabilities = (frequncies of each alphabet / the total size)

    # find the minimal possible loss
    log_oppo_prob = loss_fn(torch.log(optimal_prob))
    optimal_value = torch.tensor(sum_char) @ log_oppo_prob

    # the final token probabilities
    # use Unigram Class and normalize function to find final token probabilities
    final_token_prob = normalize(torch.sigmoid(model.s))
    # compatibility between numpy and PyTorch Tensor for grad(gradient) + transpose to row vector
    transpose_prob = final_token_prob.view(-1).clone().detach().numpy()

    # Display loss function result
    plt.subplot(121)  # loss function
    plt.plot(range(num_iterations), loss_all, label="Loss History")
    plt.xlabel("Iteration")
    plt.ylabel("Loss")
    plt.title("The Loss as a Function of Time/Iteration")
    plt.axhline(  # draw the minimum possible line
        optimal_value, color="r", linestyle="--", label="Minimum Possible Loss"
    )
    plt.legend()

    # Display probabilities result (the final token probabilites and optimal probabilities)
    plt.subplot(122)  # probabilities bar graph
    x_axis = np.arange(len(vocabulary))  # set x-axis
    alpha = 0.15  # set the stride to avoid overlap
    width = 0.25  # bar width
    plt.bar(
        x_axis + alpha,
        transpose_prob,
        width,
        color="Red",
        label="Final Token Probabilities",
    )
    plt.bar(
        x_axis - alpha,
        optimal_prob,
        width,
        color="Blue",
        label="Optimal Probabilities",
    )
    plt.xticks(x_axis, vocabulary)  # x-axis range
    plt.yticks([0.00, 0.05, 0.10, 0.15])  # y-axis range
    plt.xlabel("Optimal(Blue) and Token(Red)")  # x-labels
    plt.ylabel("Probabilities")  # y-labels
    plt.title("Comparison Between Two Probabilities")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    gradient_descent_example()
