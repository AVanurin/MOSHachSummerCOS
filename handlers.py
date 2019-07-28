from aiohttp import web
from aiohttp_session import get_session
import aiohttp_jinja2
import jinja2
import db
import utility
import aidoc
import styles


@aiohttp_jinja2.template('home.html')
async def home_page(request):
    session = await get_session(request)
    return {}

@aiohttp_jinja2.template('index.html')
async def index(request):
    return {}

@aiohttp_jinja2.template('form.html')
async def form(request):
    session = await get_session(request)
    return {}

@aiohttp_jinja2.template('form_success.html')
async def success(request):
    return {}

@aiohttp_jinja2.template('admin_tasks.html')
async def admin_all_task(request):
    tasks = db.all_tasks()
    context = [{"id": task[0], "sender": task[1],"text": task[2] ,"status": utility.status_to_str(task[3])} for task in tasks]
    return {"tasks": context}

async def static_pic_logo(request):
    return web.FileResponse("templates/res/cos_logo_3.png")
    #return web.FileResponse("templates/res/logo-COS.jpg")

async def static_pic_logo_cp(request):
    return web.FileResponse("templates/res/image.png")

@aiohttp_jinja2.template("solution.html")
async def solution(request):
    task_id = request.match_info.get('id')
    task_details = db.task(task_id)
    print(task_details)

    context = {
        "task": {
            "id": task_details[0],
            "sender": task_details[1],
            "text": task_details[2],
            "status": utility.status_to_str(task_details[3])
        }
    }
    
    if task_details[3]==2:
        solution_details = db.solution(task_id)
        context["solution"] = {
            "text": solution_details[2]
        }
        context["resolved"] = True
    else:
        context["resolved"] = False
        context["solution"] = None

    return context


async def post_form(request):
    data = await request.post()
        
    #sender = data["sender_id"]
    text = data["form-text"]
    if "flag" in data.keys():
        flag = True
    else:
        flag = False

    if text:
        if not flag:
            r = aidoc.send_xml(text)       
            prepared = styles.make_results(r)       
            _filtered = [x for x in prepared if float(x["chance"])>0.01]
            context = {"text": text, "result": _filtered}

            return aiohttp_jinja2.render_template("response.html", request, context=context)
        else:
            return web.HTTPFound("/")
    else:
        return web.HTTPFound("/")

    return web.HTTPFound('/')
