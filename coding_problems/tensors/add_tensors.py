import torch

def add_tensors(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    result = x + y
    return result

    # Notes to self:
    # if x and y have similar shape then:
        # Memory Allocation: PyTorch allocates memory for the result tensor with size of x or y
        # Element-wise Addition: Each element of A is added to the corresponding element of B:
                # C[i,j]=A[i,j]+B[i,j]
        # Storage and Strides:
                # If the tensors are contiguous in memory, PyTorch can use vectorized operations for efficient computation.
    # else:
       # Tensors Have Different Shapes (Broadcasting)
       # Broadcasting Rules Check: 
              # PyTorch checks if one of the dimensions is 1 or missing. If so, it expands the tensor without copying data.
       # expand the tensor with y to match x
       

    # Key terms
    # Strides: (3,1), meaning: Move 3 elements in memory to jump to the next row. Move 1 element to jump to the next column.
    # Expanding Without Copying: When PyTorch expands a tensor, it does not allocate new memory. Instead, it modifies the strides so that the same value is reused across the expanded dimension.
              
       
        