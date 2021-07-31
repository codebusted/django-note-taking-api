from django.shortcuts import redirect, render

# Create your views here.
from .models import Notes

def editor(request):
	id = int(request.GET.get('id', 0))
	notes = Notes.objects.all()

	if request.method == 'POST':
		id = int(request.POST.get('id', 0))
		title = request.POST.get('title')
		content = request.POST.get('content')

		if id > 0:
			note = Notes.objects.get(pk=id)
			note.title = title
			note.content = content
			note.save()
			return redirect('/?id=%i' % id)
		else:
			if title == '' or content == '':
				return redirect('/?id=0')
			note = Notes.objects.create(title=title, content=content)
			return redirect('/?id=%i' % note.id)

	if id > 0:
		note = Notes.objects.get(pk=id)
	else:
		note = ''

	context = {
		'id': id,
		'notes': notes,
		'note': note
	}

	return render(request, 'editor.html', context)

def deleteNote(request, id):
	note = Notes.objects.get(pk=id)
	note.delete()
	return redirect('/?id=0')