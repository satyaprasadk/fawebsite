from django.shortcuts import render

def solutions(request):
    values = {}
    return render(request, 'site/solutions/solutions.html', values)

def retail(request):
    values = {}
    return render(request, 'site/solutions/retail.html', values)

def banking(request):
    values = {}
    return render(request, 'site/solutions/banking.html', values)

def financial_market(request):
    values = {}
    return render(request, 'site/solutions/financial_markets.html', values)

def manufacturing(request):
    values = {}
    return render(request, 'site/solutions/manufacturing.html', values)

def healthcare(request):
    values = {}
    return render(request, 'site/solutions/healthcare.html', values)

def telecom(request):
    values = {}
    return render(request, 'site/solutions/telecom.html', values)