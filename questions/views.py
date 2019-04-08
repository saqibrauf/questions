from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Category, Question, Answer
from django.views.decorators.csrf import csrf_exempt

def index(request):
	questions = Question.objects.all().order_by('-date')

	context = {
		'questions' : questions,
	}
	return render(request, 'questions/index.html', context)


def question(request, id, slug=''):
	question = Question.objects.get(id=id)
	answers = question.answers.all()
	related = question.category.questions.all()
	context = {
		'question' : question,
		'answers' : answers,
		'related' : related,
	}
	return render(request, 'questions/question.html', context)

@csrf_exempt
def brainly_last_q(request):
	if request.method == 'POST':
		lastq = Question.objects.filter(source='brainly').order_by('-id')
		if lastq:
			lastq = lastq[0]		
			data = {
				'lastq' : lastq.source_id,
			}
			return JsonResponse(data)
		else:
			data = {
				'lastq' : '0',
			}
			return JsonResponse(data)
	else:
		return HttpResponse('Not Allowed')

@csrf_exempt
def add_question(request):
	if request.method == 'POST':
		source = request.POST.get('source')
		source_id = request.POST.get('source_id')
		question = request.POST.get('question')
		answer = request.POST.get('answer')
		category = request.POST.get('category')

		try:
			category = Category.objects.get(name__icontains=category)
		except:
			category = Category.objects.create(name=category)
			category.save()


		question = Question.objects.create(category=category, question=question, source=source, source_id=source_id)
		question.save()

		answer = Answer.objects.create(question=question, answer=answer)
		answer.save()

		saved = 'Question Number ' + source_id + ' Saved.'
		data = {
			'message' : saved,
		}
		
		return JsonResponse(data)