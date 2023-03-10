from django.http import HttpResponse
import pyqrcode
from ..constants.utils import *

def qrGenerate(request):
    jsons = json.loads(request.body)
    try:
        inputdata = jsons['inputdata']
        usernum = jsons['usernum']
        qrData = pyqrcode.create(inputdata)
        b64 = qrData.png_as_base64_str(scale=10)
        con = connectDB()
        cursor = con.cursor()
        cursor.execute("INSERT INTO t_qrcode "
                        f"VALUES (DEFAULT, '{b64}', '{usernum}','{inputdata}', NOW());")
        resp = sendResponse(200,'Success',jsons["action"])
        cursor.close()
        con.commit()
    except Exception as e:
        resp = sendResponse(400,str(e),jsons["action"])
    return resp
    # qrGenerate

def qrList(request):
    jsons = json.loads(request.body)
    try:
        usernum = jsons['usernum']
        con = connectDB()
        cursor = con.cursor()
        cursor.execute(f"SELECT qrdata,date FROM t_qrcode WHERE usernum = {usernum}")
        columns = cursor.description
        respRow = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        resp = sendResponse(200,respRow,jsons["action"])
        cursor.close()
    except Exception as e:
        resp = sendResponse(400,str(e),jsons["action"])
    return resp
    # qrList

def qrInfo(request):
    jsons = json.loads(request.body)
    try:
        qrnum = jsons['qrnum']
        con = connectDB()
        cursor = con.cursor()
        cursor.execute(f"SELECT qrdata,rawdata,date FROM t_qrcode WHERE qrnum = {qrnum}")
        columns = cursor.description
        respRow = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        resp = sendResponse(200,respRow,jsons["action"])
        cursor.close()
    except Exception as e:
        resp = sendResponse(400,str(e),jsons["action"])
    return resp
    # qrInfo

def qrEdit(request):
    jsons = json.loads(request.body)
    try:
        qrnum = jsons['qrnum']
        newdata= jsons["newdata"]
        qrData = pyqrcode.create(newdata)
        b64 = qrData.png_as_base64_str(scale=10)       
        con = connectDB()
        cursor = con.cursor()
        cursor.execute(f"UPDATE t_qrcode SET rawdata = '{newdata}', qrdata = '{b64}' WHERE qrnum = '{qrnum}'")
        resp = sendResponse(200,'Success',jsons["action"])
        cursor.close()
        con.commit()
    except Exception as e:
        resp = sendResponse(400,str(e),jsons["action"])
    return resp
    # qrEdit

def qrDelete(request):
    jsons = json.loads(request.body)
    try:
        qrnum = jsons['qrnum']      
        con = connectDB()
        cursor = con.cursor()
        cursor.execute(f"DELETE FROM t_qrcode WHERE qrnum = {qrnum}")
        resp = sendResponse(200,'Success',jsons["action"])
        cursor.close()
        con.commit()
    except Exception as e:
        resp = sendResponse(400,str(e),jsons["action"])
    return resp
    # qrDelete

def mainFunction(reqeust):
    json = checkreg(reqeust)
    if json == False:
        resp = sendResponse(400,'Json болгоход алдаа гарлаа',json)
        return HttpResponse(json, content_type="application/json")
    else:
        try:
            if json['action'] == 'qrGenerate':
                resp = qrGenerate(reqeust)
            if json['action'] == 'qrList':
                resp = qrList(reqeust)
            if json['action'] == 'qrInfo':
                resp = qrInfo(reqeust)
            if json['action'] == 'qrEdit':
                resp = qrEdit(reqeust)
            if json['action'] == 'qrDelete':
                resp = qrDelete(reqeust)
        except Exception as e:
            resp = str(e)
    return HttpResponse(resp, content_type="application/json")


