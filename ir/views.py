from django.shortcuts import render
def ir(request):
    return render(request, "ir/ir.html", {
        'reading': '99',
    })
