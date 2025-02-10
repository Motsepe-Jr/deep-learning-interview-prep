import torch
import torch.nn
from torchtyping import TensorType

# Helpful functions:
# https://pytorch.org/docs/stable/generated/torch.reshape.html
# https://pytorch.org/docs/stable/generated/torch.mean.html
# https://pytorch.org/docs/stable/generated/torch.cat.html
# https://pytorch.org/docs/stable/generated/torch.nn.functional.mse_loss.html

# Round your answers to 4 decimal places using torch.round(input_tensor, decimals = 4)
class Solution:
    def reshape(self, to_reshape: TensorType[float]) -> TensorType[float]:
        # the intial element must be in the final reshape output

        # edge cases: m, and n must compliemnt each other ( divisble)
            # if n % 2 != 0:
            #     return False

        # determien the dimensions of row, and co
        m, n = to_reshape.shape
        row = m * (n // 2)
        col = 2

        return torch.round(torch.reshape(to_reshape, (row, col)), 4)


    def average(self, to_avg: TensorType[float]) -> TensorType[float]:
        # assuming to_avg is 2D
        return torch.mean(to_avg, dim=0)

    def concatenate(self, cat_one: TensorType[float], cat_two: TensorType[float]) -> TensorType[float]:
        
        return torch.concat((cat_one, cat_two), 1)

    def get_loss(self, prediction: TensorType[float], target: TensorType[float]) -> TensorType[float]:
        # torch.nn.functional.mse_loss() will be useful - check out the documentation
         return torch.round(torch.nn.functional.mse_loss(prediction, target), 4)
