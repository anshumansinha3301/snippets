def swapOddEvenBits(n):
    # 0xAAAAAAAA = 101010...10 (32 bits), mask to extract even-positioned bits
    even_bits = n & 0xAAAAAAAA
    # 0x55555555 = 010101...01 (32 bits), mask to extract odd-positioned bits
    odd_bits = n & 0x55555555
    
    # Right shift even bits, left shift odd bits
    even_bits >>= 1
    odd_bits <<= 1
    
    return even_bits | odd_bits

print(swapOddEvenBits(23))  # Output would be 43 for input 23 (0b10111 -> 0b101011)
