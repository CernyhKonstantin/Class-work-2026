import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

def home(request):
    return render(request, 'main/home.html')

def registration_page(request):
    return render(request, 'main/registration.html')

@require_POST
def register_api(request):
    if request.content_type != 'application/json':
        return JsonResponse({'success': False, 'message': 'Content-Type must be application/json.'}, status=415)
    try:
        data = json.loads(request.body.decode('utf-8'))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({'success': False, 'message': 'Invalid JSON data.'}, status=400)
    fields = ['first_name', 'last_name', 'email', 'age', 'address']
    if not isinstance(data, dict) or any(not str(data.get(k, '')).strip() for k in fields):
        return JsonResponse({'success': False, 'message': 'Please complete all required fields.'}, status=400)
    try:
        age = int(data['age'])
        if not 1 <= age <= 120:
            raise ValueError
    except (TypeError, ValueError):
        return JsonResponse({'success': False, 'message': 'Age must be between 1 and 120.'}, status=400)
    received = {'first_name':str(data['first_name']).strip(),'last_name':str(data['last_name']).strip(),'email':str(data['email']).strip(),'age':age,'address':str(data['address']).strip(),'newsletter':bool(data.get('newsletter', False))}
    print('\n--- NEW REGISTRATION (JSON) ---', flush=True)
    print(json.dumps(received, ensure_ascii=False, indent=4), flush=True)
    print('-------------------------------\n', flush=True)
    return JsonResponse({'success':True,'message':'Registration data received successfully. Check the server terminal.','registration':received})
