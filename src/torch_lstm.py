"""
The main pytorch LSTM model.
"""
import torch.nn as nn


class LSTM(nn.Module):
    def __init__(self, input_dim, hidden_dim, batch_size, output_dim=1, num_layers=2):
        super(LSTM, self).__init__()
        self.hidden_dim = hidden_dim
        self.batch