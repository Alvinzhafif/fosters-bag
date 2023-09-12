from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Alvin Zhafif Afilla',
        'class': 'PBP KKI',
        'general': 'This is a project that is under work, this will be an rpg-themed inventory management project',
        'lore': 'Foster is a merchant in the city of sorus, he is known to be the best trader in the city with never before seen items and weapons.However, currently he has problems with managing his inventory and needs your help',
        'status': 'here is one of his most priced item',
        'weapon': 'Blade of the damned',
        'weapon_desc': 'a weapon found in the edge of the underworld',
        'amount' : '1'
    }

    return render(request, 'main.html', context)

# Create your views here.
