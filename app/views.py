from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Samples

# Create your views here.

'''
def index(request):
    samples = Samples.objects.all()

    html = "<h1>Lista de Amostras</h1>"
    for sample in samples:
        html += f"<p> ID: {sample.id}</p>"
        html += f"<p> MP10: {sample.mp10}</p>"
        html += f"<p> MP25: {sample.mp25}</p>"
        html += f"<p> O3: {sample.o3}</p>"
        html += f"<p> CO: {sample.co}</p>"
        html += f"<p> NO2: {sample.no2}</p>"
        html += f"<p> SO2: {sample.so2}</p>"
        html+= "<hr>"
    
    return HttpResponse(html)

Certo inicialmente quero explicar esse código primeiramente eu criei um uma request, depois puxei os objetos do Sample model, assim fiz um arquivo em HTML, e rodei a response.
'''

def index(request):
    samples = Samples.objects.all()
    context = {'samples': samples}
    return render(request, 'index.html', context)

def save(request):
    if request.method == 'POST':
        mp10 = request.POST.get('mp10')
        mp25 = request.POST.get('mp25')
        o3 = request.POST.get('o3')
        co = request.POST.get('co')
        no2 = request.POST.get('no2')
        so2 = request.POST.get('so2')
        Samples.objects.create(mp10 = mp10, mp25 = mp25, o3 = o3, co = co, no2 = no2, so2 = so2)
        return redirect('index')

    samples = Samples.objects.all()
    context = {'samples': samples}
    return render(request, 'index.html', context)

def edit(request, sample_id):
    if request.method == 'POST':
        # Busque a amostra pelo ID
        sample = Samples.objects.get(id=sample_id)
        
        # Atualize os campos da amostra
        sample.mp10 = request.POST.get('mp10')
        sample.mp25 = request.POST.get('mp25')
        sample.o3 = request.POST.get('o3')
        sample.co = request.POST.get('co')
        sample.no2 = request.POST.get('no2')
        sample.so2 = request.POST.get('so2')
        
        # Salve as alterações no banco de dados
        sample.save()
        
        # Redirecione para a página desejada (ou para a página de detalhes da amostra, se preferir)
        return redirect('index')  # Lembre-se de ajustar o nome da URL

    # Se não for uma solicitação POST, renderize a página de edição com os detalhes da amostra
    try:
        sample = Samples.objects.get(id=sample_id)
    except Samples.DoesNotExist:
        # Lide com o caso em que a amostra não existe
        return redirect('index')  # Ou renderize uma página de erro

    context = {'sample': sample}
    return render(request, 'index.html', context)

def delete(request, sample_id):
    sample = Samples.objects.get(id=sample_id)
    sample.delete()
    return redirect(index)
        
    