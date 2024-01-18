# Constants
SELLER_DISCOUNT = True # True when there's one of those promotions
# Promotion Types:
SEVENTY_OFF = 0.7
EIGHTY_OFF = 0.8 # At the time of pushing this script, this was the latest promotion
NINETY_OFF = 0.9
# eBay static fee %
FVF = 0.1066667   # 10.66667%, this value is between 10.7% and 12% depending on the product
FIXED_FEE = 0.25  # this is a fixed fee for any product
VAT = 0.2         # 20% ...ye :)


price = float(input('Enter the product price: '))
# pnp = int(input('Enter the shipping price: ')) # P&P: Postage & Packaging
pnp = 2.70 # CUSTOM VALUE; you can set this manually

if input('+ post? 0: yes; 1: FREE POST >>> ') == '0': # specify whether your item has free shipping or not
    total_price = price + pnp
else:
    total_price = price

# Calculating the total eBay Fees
if SELLER_DISCOUNT:
    total_fee = FIXED_FEE + (total_price - total_price * EIGHTY_OFF ) * FVF
else:
    total_fee = FIXED_FEE + total_price * FVF
total_fee += total_fee * VAT # VAT 20% on top of all fees :3
total_fee = round(total_fee, 2) # round the result because eBay only takes 2 values after the decimal

print('Total fee = ', total_fee)
print('Your profit is: £' + str(round((total_price - total_fee - pnp), 2)))