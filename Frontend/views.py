from __future__ import unicode_literals
from django.shortcuts import render
import requests, json

#View to retrieve user data from GithubAPI.
def darkintel_retrieval(request):
    content = {}
    if request.method == 'POST':
        username = request.POST.get('query')

    return render(request, 'DarkIntel/userdata.html', content)
