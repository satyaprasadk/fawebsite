from django.shortcuts import render

def solution_by_role(request):
    values = {}
    return render(request, 'site/role/by_role.html', values)