#usd to inr conveter

def usd_to_inr(usd):
    rate=75.4
    inr_amount=usd*rate
    return inr_amount

usd= float(input("Enter the amount of USD: "))
inr = usd_to_inr(usd)
print(f"{usd} usd is equal to {inr} inr")
