from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import Blog, Job
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def check_job_desc(jobs, user_desc):
    relevant_job_id = []
        
    for i in jobs:                           
        content_list = [user_desc, i.job_description]
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(content_list)
        matrix = cosine_similarity(count_matrix)
        result = (matrix[1][0]*100).round(2)
            
        if round(result) > 45:
            relevant_job_id.append(i.id)
        
    if len(relevant_job_id) == 0:
        return False
    
    return relevant_job_id
    
    
# Home View
def home(request):
    data = {"Endpoints": "Below are the Endpoints for the usage of this API", 
            "/getAllJobs": "Returns all the Existing Objects from the Database",
            "/get/id": "Returns Specific Objects from the Database",
            "/getRelevantJobs": "Returns the Status after screening the Data From the User." 
            
            }
    
    return JsonResponse(data)

# Get All Objects from the Database
def getAllJobs(request):
    all_blogs = Job.objects.all()
    data = {"results": list(all_blogs.values("id", "company_name", "title", "job_description"))}
    print(data)
    return JsonResponse(data)

# Get Specific Objects from the Database
def get(request, id):
    job = get_object_or_404(Job, id=id)
    data = {"results": {
        "id": job.id,
        "company": job.company_name,
        "title": job.title,
        "job_desc": job.job_description,
    }}
    return JsonResponse(data)
    
  
@csrf_exempt  
# Get Specific Jobs Relevant to the User
def getRelevantJobs(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        
        jobs = Job.objects.filter(title=title)
        
        check = check_job_desc(jobs, desc)
        print(check)
        if check == False:
            return JsonResponse({"Error":"No Relevant Jobs Found"})
        else:
            data = {"results": list(check)}
            return JsonResponse(data)
        
    return JsonResponse({"Invalid Request": "POST request expected"})
        

# cURL -X POST -d "title=Frontend Developer&desc=Design, UI, UX, HTML, CSS, JS" http://localhost:8000/getRelevantJobs


@csrf_exempt
# Searchs Through the Fields and Returns Blogs based on that        
def search(request):
    query = request.GET['query']
    job = Job.objects.filter(title__icontains=query) or Job.objects.filter(company_name__icontains=query) or Job.objects.filter(job_description__icontains=query)
    data = {"results" : list(job.values("id", "company_name", "title", "job_description"))} 
    return JsonResponse(data)
    