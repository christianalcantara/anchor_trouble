from django.shortcuts import render
from .forms import SendFileForm


def index(request):
    ctx = {}
    if request.method == 'POST':
        form = SendFileForm(request, request.FILES)
        if form.is_valid():
            data = form.gas_station
            print '>>>>>>>>>', data
            ctx.update({'data': data})
    else:
        form = SendFileForm()

    ctx.update({'form': form})

    return render(request, 'website/base.html', ctx)
