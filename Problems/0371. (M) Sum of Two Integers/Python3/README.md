## 371. (M) Sum of Two Integers

### `solution.py`
As the use of the `+` operator is not allowed, the problem is essentially asking us to design an adder using bit manipulation. The [half adder](https://en.wikipedia.org/wiki/Adder_(electronics)#Half_adder) takes two bits as input and outputs two bits; with one bit being the sum of the input bits and the other being the carry bit. The two bits are XORed to get the initial sum, and are then ANDed to compute the carry. We want to move the carry over to the next digit though, and so we need to remember to shift the carry to the left by 1 bit. Thankfully we can assume that the sum is not larger than a signed 4-byte integer given the constraints on the input. Thus we can simply apply bit manipulation on the entirety of `a` and `b` instead of doing it digit by digit. This also tells us that if the sum *is* larger than a signed 4-byte integer we should flip the sign according to [two's complement](https://en.wikipedia.org/wiki/Two%27s_complement#Procedure). 
   
#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `b` in binary. The space complexity is $O(1)$.  
  

