from decimal import Decimal
import math

print("NOTICE: As we mourn the death of Pope Francis, let us continue to pray so that his soul may be worthy of the Lord's presence. He who has imitated Christ's death shall rise on the final day.")
print("")
print("POPE CONCLAVE 2025")

cardinals_buffer = input("Enter number of cardinals: ")
while not cardinals_buffer.isdigit():
    print("Please enter valid number of cardinals. Only those aged below 80 are eligible to vote and be elected.")
    cardinals_buffer = input("Enter valid number of cardinals: ")
cardinals = int(cardinals_buffer)
probability_buffer = input("Enter probability of the cardinal you enquire: ")
overhead = math.ceil(cardinals * 2/3)
try:
    probability = Decimal(probability_buffer)
except:
    probability = Decimal(1) / Decimal(cardinals)

actual_probability = Decimal(0)
for i in range(overhead, cardinals+1):
    c1 = Decimal(math.comb(cardinals, i))
    c2 = probability ** i
    c3 = (Decimal(1) - probability) ** (cardinals - i)
    actual_probability += c1*c2*c3

print("Probability of this cardinal getting elected Pope (including probability of no cardinal elected): ", actual_probability)
print("Probability of this cardinal getting elected Pope (among his peers): ", probability)