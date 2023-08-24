# Below is an algorithm that counts the number of set bits in a binary value string. I find it pretty neat.

def count_set_bits(n):
    count = 0
    while n > 0:
        count += n & 1 # This increments `count` if the rightmost bit of n is set
        n >>= 1        # This shifts n bitwise once to the right
                       # Successive shifts may look like: 01101 --> 00110 --> 00011 --> 00001 --> 00000
    return count
n=6
print(count_set_bits(n))
