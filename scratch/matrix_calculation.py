import torch
import time

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
size = 6000

#1. Warm-up run (allocates memory and compiles execution graph)
a = torch.randn(size, size, device=device)
b = torch.randn(size, size, device=device)
_ = a @ b
torch.mps.synchronize()

#2. Timed CPU benchmark
start = time.time()
for _ in range(5):
    _ = a @ b
torch.mps.synchronize() # Crucial: awaits for GPU async queue to flush
gpu_time = (time.time() - start) / 5
print(f"MPS GPU ({size}x{size}): {gpu_time:.4f}s")

# 3. CPU Benchmark
a_cpu, b_cpu = torch.randn(size, size), torch.randn(size, size)                    
start = time.time()                                                                
_ = a_cpu @ b_cpu                                                                  
cpu_time = time.time() - start                                                     
print(f"CPU ({size}x{size}):     {cpu_time:.4f}s")                                
print(f"Speedup:                {cpu_time / gpu_time:.2f}x")
