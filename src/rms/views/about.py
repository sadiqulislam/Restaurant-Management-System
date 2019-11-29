from django.shortcuts import render


def about(req):
    context = {

    }

    return render(req, 'rms/about.html', context)

