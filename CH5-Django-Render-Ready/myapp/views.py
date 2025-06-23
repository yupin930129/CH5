from django.shortcuts import render

def post(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        return render(request, 'post_form.html', {'message': f'收到：{name}, {age}'})
    return render(request, 'post_form.html')