from decimal import Decimal
import math

print("NOTICE: As we mourn the death of Pope Francis, let us continue to pray so that his soul may be worthy of the Lord's presence. He who has imitated Christ's death shall rise on the final day.")
print("")
print("POPE CONCLAVE 2025")

cardinals = int(input("Enter number of cardinals: "))
probability_buffer = input("Enter probability of the cardinal you enquire: ")
overhead = math.ceil(cardinals * 2/3)
if not probability_buffer.isdigit():
    probability = Decimal(1)/Decimal(cardinals)
else:
    probability = Decimal(probability_buffer)

actual_probability = Decimal(0)
for i in range(overhead, cardinals+1):
    c1 = Decimal(math.comb(cardinals, i))
    c2 = probability ** i
    c3 = (Decimal(1) - probability) ** (cardinals - i)
    actual_probability += c1*c2*c3

print("Probability of this cardinal getting elected Pope: ", actual_probability)