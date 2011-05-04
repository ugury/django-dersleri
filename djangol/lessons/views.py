from lessons.models import Lesson,Category
from django.template import RequestContext
from django.shortcuts import render_to_response

def get_lesson(request,
               id,
               slug,
               template='get_lesson.html'):
    """ return lesson """
    try:
        lesson = Lesson.objects.get(pk=id,slug=slug)
    except Lesson.DoesNotExist:
        pass
    
    return render_to_response(template,
                              {'lesson':lesson},
                              context_instance=RequestContext(request))

def get_lessons(request,
                template='table_of_contents.html'):
    """ get lessons """
    try:
        cats = Category.objects.all()
    except:
        cats = None
    
    return render_to_response(template,
                              {'lessons':cats},
                              context_instance=RequestContext(request))