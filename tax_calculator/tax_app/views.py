from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def calculate_tax(request, number):
    tax_rate = 0.15
    total_price = number + (number * tax_rate)
    return render(request, 'calculate_tax.html', {'total_price': total_price})

def tax_rate(request):
    tax_rate = 0.15
    return render(request, 'tax_rate.html', {'tax_rate': f"{tax_rate*100:.2f}%"})
