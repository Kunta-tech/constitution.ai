import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .api_com import get_api_response

@csrf_exempt  # Disable CSRF for simplicity; consider a more secure approach for production
def chatbot_response(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            sentence = data.get('sentence')  # Extract the specific field

            if sentence:
                # Process the sentence (your chatbot logic)

                response_text = get_api_response(sentence)
                return JsonResponse({'response': response_text})
            else:
                return JsonResponse({'error': 'Invalid input'}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def page(request):
    return render(request, 'ab.html')