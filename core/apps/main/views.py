from django.shortcuts import render



def home(request):

    context = dict()




    return render(request, 'main/home.html', context = context)



def testing(request):

    context = dict()



    return render(request, 'main/testing.html', context = context)

def projects(request):

    context = dict()



    return render(request, 'main/projects.html', context = context)




