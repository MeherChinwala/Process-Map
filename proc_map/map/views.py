# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Bftbl, Proctbl, Domaintbl, Dombf, Bfproc, Procsubproc, Subproctbl

def selected_domain(request, domid):
    bfs_domain=Bftbl.objects.filter(domain=domid)
    domain_object=Domaintbl.objects.get(id=domid)
    domain_set=Domaintbl.objects.filter(id=domid)
    process=Proctbl.objects.filter(map0__domain=domid)
    sub_process = Subproctbl.objects.filter(map__domain=domid)

    process_high=Proctbl.objects.filter(map0__domain=domid).filter(complexity='High')
    process_medium=Proctbl.objects.filter(map0__domain=domid).filter(complexity='Medium')
    process_low=Proctbl.objects.filter(map0__domain=domid).filter(complexity='Low')
    process_unknown=Proctbl.objects.filter(map0__domain=domid).filter(complexity='Unknown')
    
    

    return render(request, 'map/dashboard.html', {'process_high':process_high,'process_medium':process_medium,'process_low':process_low,'process_unknown':process_unknown,'process':process,'sub_process':sub_process,'domain_object':domain_object, 'bfs_domain':bfs_domain, 'domain':domain_set})


def home(request):
    bf=Bftbl.objects.all()
    domain_select=Domaintbl.objects.all()
    return render(request, 'map/select_bfs.html',{'domain_select':domain_select})


def final(request, domid, bfid):
    
    bf_object=Bftbl.objects.get(id=bfid)
    bfs_domain=Bftbl.objects.filter(domain=domid)
    process=Proctbl.objects.filter(bus_func=bfid, map0__domain=domid)
    domain_set=Domaintbl.objects.filter(id=domid)
    domain_object=Domaintbl.objects.get(id=domid)
    
    return render(request, 'map/process.html', {'domain_object':domain_object, 'bfs_domain':bfs_domain, 'process':process, 'bf_object':bf_object, 'domain':domain_set})
    # Create your views here.

def sub_proc_view(request, domid, bfid, procid):
    
    bf_object=Bftbl.objects.get(id=bfid)
    bfs_domain=Bftbl.objects.filter(domain=domid)
    process=Proctbl.objects.filter(bus_func=bfid, map0__domain=domid)
    domain_set=Domaintbl.objects.filter(id=domid)
    domain_object=Domaintbl.objects.get(id=domid)
    sub_process = Subproctbl.objects.filter(map__domain=domid, proc=procid)
    proc_object=Proctbl.objects.get(id=procid)
    
    return render(request, 'map/sub_proc_template.html', {'proc_object':proc_object,'sub_process':sub_process,'domain_object':domain_object, 'bfs_domain':bfs_domain, 'process':process, 'bf_object':bf_object, 'domain':domain_set})
   
