from django.http import JsonResponse
from django.shortcuts import render
from ajexapp.models import SelectLanguage


def Home(request):
    language=SelectLanguage.objects.values('language').distinct()
    topics=SelectLanguage.objects.values('topic').distinct()
    return render(request, 'index.html',{'language':language,'topics':topics})

def Get_form(request):
        language = request.GET.get('language',None)
     
        if language:
            topics=SelectLanguage.objects.filter(language=language).values('topic')
            topic_list=list(topics)
            return JsonResponse({'topics':topic_list})
        return JsonResponse({'error': 'Invalid request'}, status=400)
