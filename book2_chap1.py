unit_price = 49.99
quantity = 30

print(f"Subtotal: ${unit_price * quantity:.2f}")
print(f"Subtotal: ${unit_price * quantity:,.2f}")

sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate:.2%}")
print(f"Sales Tax Rate {sales_tax_rate:.1%}")


subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax

output = f"""
Subtotal:   ${subtotal:,.2f}
Sales Tax:  ${sales_tax:,.2f}
Total:      ${total:,.2f}
"""
print(output)  # ----------------------------------------------


output1 = f"""
Subtotal:       ${subtotal:>9,.2f}
Sales Tax:      ${sales_tax:>10,.2f}
Total:          ${total:>11,.2f}
"""
print(output1)  # ----------------------------------------------


s_subtotal = "$" + f"{subtotal:,.2f}"
s_sales_tax = "$" + f"{sales_tax:,.2f}"
s_total = "$" + f"{total:,.2f}"

output2 = f"""
Subtotal:       {s_subtotal:>9}
Sales Tax:      {s_sales_tax:>10}
Total:          {s_total:>11}
"""
print(output2)  # ----------------------------------------------

x = 255
print(x)                # 255
print(bin(x))           # 0b11111111
print(oct(x))           # 0o377
print(hex(x))           # 0xff

print(0b0111)           # 7
print(0b0111)           # 7

first_name = "Alan"
middle_init = "C"
last_name = "Simpson"
full_name = first_name + " " + middle_init + ". " + last_name   # Alan C. Simpson
print(full_name)

s1 = ""
s2 = " "
s3 = "A B C"
print(len(s1), len(s2), len(s3))    # 0 1 5



