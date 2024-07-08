from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor, BankDetail, StipendRate, StipendSlip, Status, PaymentHistory

# Create your views here.

def dashboard(request):
    pgr=Doctor.objects.all().count()
    apgr=Doctor.objects.filter(status__status="Active").count()
    ipgr=Doctor.objects.filter(status__status="Inactive").count()
    doctor=Doctor.objects.all()
    doctors = BankDetail.objects.select_related('doctor')
    ph=PaymentHistory.objects.filter(month=4).filter(year=2024)
    ph.count()
    phmay=PaymentHistory.objects.filter(month=5).filter(year=2024)
    phjune=PaymentHistory.objects.filter(month=6).filter(year=2024)
    ts4=0
    ts5=0
    ts6=0
    for p in ph:
        ts4 += p.gross_stipend
    tpg4=ph.count()
    for p in phmay:
        ts5 += p.gross_stipend
    for p in phjune:
        ts6 += p.gross_stipend
    ts=ts4+ts5+ts6
    tph=PaymentHistory.objects.all()
    od=0
    for t in tph:
        od +=t.others
    budget=2738365000
    bal=budget - ts + od -16900000
    tpg5=phmay.count()
    tpg6=phjune.count()
    ph_ids = set(ph.values_list('doctor_id', flat=True))
    phmay_ids = set(phmay.values_list('doctor_id', flat=True))
    # Find objects removed in May (present in April but not in May)
    removed_in_may = len(ph_ids - phmay_ids)
    # Find objects added in May (present in May but not in April)
    added_in_may = len(phmay_ids - ph_ids)
    #May & June comparision
    phjune_ids = set(phjune.values_list('doctor_id', flat=True))
    # Find objects removed in May (present in April but not in May)
    removed_in_june = len(phmay_ids - phjune_ids)
    # Find objects added in May (present in May but not in April)
    added_in_june = len(phjune_ids-phmay_ids)
    status=Status.objects.raw("select * from insbiz_doctor left join insbiz_status on insbiz_doctor.id = insbiz_status.doctor_id left join insbiz_bankdetail on insbiz_doctor.id = insbiz_bankdetail.doctor_id left join insbiz_stipendslip on insbiz_doctor.id = insbiz_stipendslip.doctor_id left join insbiz_stipendrate on insbiz_stipendslip.stipendrate_id = insbiz_stipendrate.id")
    return render(request, 'dashboard.html', {'ts6':ts6, 'tpg6':tpg6, 'doctors':doctors, 'status':status, 'pgr':pgr, 'doctor':doctor, 'apgr':apgr, 'ipgr':ipgr, 'ts4':ts4, 'tpg4':tpg4, 'ts5':ts5, 'tpg5':tpg5, 'removed_in_may':removed_in_may, 'added_in_may':added_in_may, 'ts':ts, 'removed_in_june':removed_in_june, 'added_in_june':added_in_june, 'bal':bal})

def payslip(request):
    if request.method=='POST':
        cnic=request.POST['cnic']
        month=request.POST['month']
        year=request.POST['year']
        ph=PaymentHistory.objects.select_related('doctor').filter(month=month).filter(year=year).filter(doctor__cnic=cnic)
        return render (request, 'payslip.html', {'ph':ph})
    else:
        return render(request, 'payslip.html')

def enddate(request):
    ph=PaymentHistory.objects.filter(month=4).filter(year=2024).filter(doctor__end_date__lte="2024-04-30")
    phmay=PaymentHistory.objects.filter(month=5).filter(year=2024)
    return render(request, 'enddate.html', {'ph':ph, 'phmay':phmay})

def removed(request):
    ph=PaymentHistory.objects.filter(month=4).filter(year=2024)
    phmay=PaymentHistory.objects.filter(month=5).filter(year=2024)
    aprils = set(ph.values_list('doctor_id', flat=True))
    mays = set(phmay.values_list('doctor_id', flat=True))
    removed_inmay=aprils - mays
    added_inmay=mays - aprils
    removed=PaymentHistory.objects.filter(month=4).filter(year=2024).filter(doctor_id__in=removed_inmay)
    added=PaymentHistory.objects.filter(month=5).filter(year=2024).filter(doctor_id__in=added_inmay)
    return render(request, 'variance.html', {'removed':removed})
def added(request):
    ph=PaymentHistory.objects.filter(month=4).filter(year=2024)
    phmay=PaymentHistory.objects.filter(month=5).filter(year=2024)
    aprils = set(ph.values_list('doctor_id', flat=True))
    mays = set(phmay.values_list('doctor_id', flat=True))
    removed_inmay=aprils - mays
    added_inmay=mays - aprils
    removed=PaymentHistory.objects.filter(month=4).filter(year=2024).filter(doctor_id__in=removed_inmay)
    added=PaymentHistory.objects.filter(month=5).filter(year=2024).filter(doctor_id__in=added_inmay)
    return render(request, 'variance.html', {'added':added})

def paymenthistory(request):
    if request.method=="POST":
        cnic=request.POST['cnic']
        ph=PaymentHistory.objects.filter(doctor__cnic=cnic)
        gt=0
        for p in ph:
            nts=p.net_stipend
            gt += nts
        return render(request, 'pyhis.html', {'ph':ph, 'gt':gt})
    else:
        return render(request, 'pyhis.html')