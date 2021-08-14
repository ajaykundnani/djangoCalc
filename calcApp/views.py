from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        c = request.POST['k']
        a = int(request.POST['a'])
        b = int(request.POST['b'])
        if c == 'ADD':
            ans = a+b
            return render(request,'index.html',{'ans':ans})
        elif c == 'SUB':
            ans = a-b
            return render(request,'index.html',{'ans':ans})
    return render(request,'index.html')

def ans(request,c):
    c = c
    print('yoooo',c)
    return HttpResponse('Done')
