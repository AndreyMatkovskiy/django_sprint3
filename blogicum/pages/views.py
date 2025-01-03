from django.shortcuts import render


def about(request):
    """Функция для просмотра информации о сайте"""
    template_dir = 'pages/about.html'
    return render(request, template_dir)


def rules(request):
    """Функция для просмотра правил"""
    template_dir = 'pages/rules.html'
    return render(request, template_dir)
