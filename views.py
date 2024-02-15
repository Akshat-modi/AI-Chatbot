from django.shortcuts import render
from django.http import JsonResponse
import openai

openai_key = "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"
openai.api_key = openai_key

def ask_openai(message):
    response= openai.Completion.create(
        model = "ada",
        prompt = message,
        max_token = 50,
    )
    answer= response.choice[0].text.strip()
    return answer
# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message= request.POST.get('message')
        response= ask_openai(message)
        return JsonResponse({'message': message, 'response':response})
    return render(request,'chatbot.html')