from django.shortcuts import render


from . import util
from django.http import HttpResponse, HttpResponseRedirect

from markdown2 import Markdown
import secrets
from django.urls import reverse
from django import forms


class NewEntryForm(forms.Form):
    title = forms.CharField(
        required=True,
        label="Title",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={"class": "form-control", "rows": 10, "placeholder": "Content..."}
        ),
    )
    edit = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput())


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry(request, entry):
    def covert2html(entryname):
        validentry = util.get_entry(entryname)
        if validentry is None:
            return None
        else:
            markdowner = Markdown()
            out = markdowner.convert(validentry)
            return out

    entryhtml = covert2html(entry)
    if entryhtml is None:

        return render(
            request, "encyclopedia/error.html", {"errMsg": "Oops. Page Not Found (404)"}
        )
    else:
        return render(
            request,
            "encyclopedia/entry.html",
            {"entry": entryhtml, "entryTitle": entry},
        )


def random(request):
    entries = util.list_entries()
    randomEntry = secrets.choice(entries)
    return HttpResponseRedirect(reverse("entry", kwargs={"entry": randomEntry}))


def search(request):
    query = request.GET.get("q", "")
    # Exact match
    # empty search is prevented by using input required in index.html
    if util.get_entry(query) is not None:
        return HttpResponseRedirect(reverse("entry", kwargs={"entry": query}))

    # Partial match
    else:
        allentries = util.list_entries()
        partialMatches = [
            entry for entry in allentries if query.lower() in entry.lower()
        ]

        return render(
            request,
            "encyclopedia/index.html",
            {"entries": partialMatches, "partialMatch": len(partialMatches)},
        )


# see
# https://stackoverflow.com/questions/53594745/what-is-the-use-of-cleaned-data-in-django
# to understand cleaned_data


def addEntry(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) is None or form.cleaned_data["edit"] is True:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("entry", kwargs={"entry": title}))
            else:
                return render(
                    request,
                    "encyclopedia/addEntry.html",
                    {
                        "form": form,
                        "message": f'This entry <a href="/wiki/{title}">already exists.</a>',
                        "entry": title,
                    },
                )

        return render(
            request,
            "encyclopedia/addEntry.html",
            {"form": form, "message": "Invalid form."},
        )
    else:
        return render(request, "encyclopedia/addEntry.html", {"form": NewEntryForm()})


def edit(request, entry):
    validEntry = util.get_entry(entry)
    if validEntry is None:
        return render(
            request, "encyclopedia/error.html", {"errMsg": "Oops. Page Not Found (404)"}
        )
    else:
        form = NewEntryForm()
        form.fields["title"].initial = entry
        form.fields["title"].widget = forms.HiddenInput()
        form.fields["content"].initial = validEntry
        form.fields["edit"].initial = True
        return render(
            request,
            "encyclopedia/addEntry.html",
            {
                "form": form,
                "edit": form.fields["edit"].initial,
                "entryTitle": form.fields["title"].initial,
            },
        )
