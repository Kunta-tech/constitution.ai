import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt  # Disable CSRF for simplicity; consider a more secure approach for production
def chatbot_response(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            print(f"Received data: {data}")
            sentence = data.get('sentence')  # Extract the specific field

            if sentence:
                # Process the sentence (your chatbot logic)
                response_text = process_sentence(sentence)
                return JsonResponse({'response': response_text})
            else:
                return JsonResponse({'error': 'Invalid input'}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def process_sentence(sentence):
    # Placeholder chatbot logic - replace with actual processing
    return "You said: {}".format(sentence)

def page(request):
    return render(request, 'ab.html')