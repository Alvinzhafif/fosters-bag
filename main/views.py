from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Alvin Zhafif',
        'class': 'PBP KKI'
    }

    return render(request, 'main.html', context)

# Create your views here.
