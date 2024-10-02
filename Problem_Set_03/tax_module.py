# tax_module.py

def calculate_sales_tax(total):
    """Calculate the sales tax based on the total."""
    sales_tax_rate = 0.06  # 6% sales tax
    return round(total * sales_tax_rate, 2)

def calculate_total_after_tax(total):
    """Calculate the total amount after tax."""
    sales_tax = calculate_sales_tax(total)
    return round(total + sales_tax, 2)
