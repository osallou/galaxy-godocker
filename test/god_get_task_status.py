
from godockercli.auth import Auth
from godockercli.httputils import HttpUtils
from godockercli.utils import Utils

def delete_task(job_id):
    #Delete a job
    job = False
    if Auth.authenticate():
        result = HttpUtils.http_delete_request("/api/1.0/task/"+str(job_id),Auth.server,{'Authorization':'Bearer '+Auth.token},Auth.noCert)
        job = result.json()
    return job

def suspend_task(job_id):
    #Get job status
    job = False
    if Auth.authenticate():
        result = HttpUtils.http_get_request("/api/1.0/task/"+str(job_id)+"/suspend",Auth.server,{'Authorization':'Bearer '+Auth.token},Auth.noCert)
        job = result.json()
    return job

def get_task_status(job_id):
    #Get job status
    job = False
    if Auth.authenticate():
        result = HttpUtils.http_get_request("/api/1.0/task/"+str(job_id)+"/status",Auth.server,{'Authorization':'Bearer '+Auth.token},Auth.noCert)
        job = result.json()
    return job

if __name__ == "__main__":
    #print get_task_status(30)
    #print suspend_task(30)
    #print delete_task(30)
    t = get_task_status(30)
    print t
    print t['status']['primary']
