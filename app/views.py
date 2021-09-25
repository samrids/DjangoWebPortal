from django.shortcuts import render

from app.models import Project, PortalSoring, SYS_SORT_CHOICES

CUSTOM_SYS_SORTKIND_CHOICES = [
    (1,''),
    (2,'-'),
]

def Index (request):
    sys_sorting = PortalSoring.objects.all()[:1]
    try:
        sortby = dict(SYS_SORT_CHOICES)[sys_sorting[0].sortby]
        sortkind = dict(CUSTOM_SYS_SORTKIND_CHOICES)[sys_sorting[0].sortkind]
    except PortalSoring.DoesNotExist:
        sortby = 'Title'
        sortkind = ''

    ORDER_BY = '{0}{1}'.format(sortkind, sortby)
    data = Project.objects.all().order_by(ORDER_BY)


    return render(request, 'index.html', {'projects': data})