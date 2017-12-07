import os

#path =

def get_template_path(path):
    file_path = os.path.join(os.getcwd(), path)
    #os.path.join makes paths/directories system agnostic so it runs on mac/linux/windows or either system
    #os.getcwd - get_Current_Working_Directory and path should combine the path for our file_path
    if not os.path.isfile(file_path): #checking if the file exists
        #if doesn't exist
        raise Exception("%s this is not a valid template path" %(file_path)) #formatting Exception with %s -- %s is a file_path
    return file_path #if exists - it returns file path


#we'll use the template directory to get template
def get_template(path):
    file_path = get_template_path(path) #both function arguments are the same
    return open(file_path).read() #opens and reads the file for us


def render_context(template_to_render, context):
    #takes templates to render and renders it according to the context
    #context is always a dictionary which holds the values those are to be replaced
    return template_to_render.format(**context)
    # **context tells the template_rendering to format the template according to the context availabe later and not to raise an error if not available right now

file_ = 'mypy/email_messages.txt' #file_ denotes path
file_html = 'mypy/email_messages.html'

template_to_render = get_template(file_) #get_template runs get_template_path function and ultimately collects the template
template_to_render_html = get_template(file_html)
context = {
    "name": "pritom",
    "date": "1000 years later",
    "total": "whatever you see fit"
}

print(render_context(template_to_render, context))
print(render_context(template_to_render_html, context))
