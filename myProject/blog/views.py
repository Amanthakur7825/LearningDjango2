from django.http import HttpResponse

def post_details(request, post_id):
    return HttpResponse(f"<h1> Post details for post{post_id}</h1>")
def user_details(request, username):
    return HttpResponse(f"<h1> User details for user{username}</h1>")
def year_by_data(request, year):
    return HttpResponse(f"<h1> year know {year}")
def article_details(request, **kwargs):
    return HttpResponse(f"<h1>data: {kwargs}</h1>")