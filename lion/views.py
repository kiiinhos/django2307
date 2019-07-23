from django.shortcuts import render

# Create your views here.
def pagina_inicial(request):
    context = {'nome':'eric',
     "cachorros": 
     ["mel","tobias","cacau","bob","madona"]}
    return render(request, 'index.html', context)