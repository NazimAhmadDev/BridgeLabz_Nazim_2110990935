sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk_size = len(sample_list) // 3

chunk1 = sample_list[:chunk_size]
chunk2 = sample_list[chunk_size:2*chunk_size]
chunk3 = sample_list[2*chunk_size:]

print("Chunk 1", chunk1)
print("After reversing it", chunk1[::-1])
print("Chunk 2", chunk2)
print("After reversing it", chunk2[::-1])
print("Chunk 3", chunk3)
print("After reversing it", chunk3[::-1])
