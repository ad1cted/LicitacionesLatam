import json
import requests
import urllib

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.handlers.wsgi import WSGIRequest
from urllib.parse import parse_qs
from selenium import webdriver
import time
import urllib.parse as urlparse
from bs4 import BeautifulSoup


def init_chromedriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options, executable_path=r'C:\chromedriver.exe')
    return driver


@csrf_exempt
def get_denue(request: WSGIRequest) -> JsonResponse:
    """
    :rtype: JsonResponse
    :param request: WSGIRequest
    :return: Este servicio permite obtener una list a de correos asociadas a una razon social
    """
    body: dict = json.loads(request.body)
    business_name: str = body.get("business_name", "")
    business_name: str = urllib.parse.quote(business_name.encode(encoding='UTF-8', errors='strict'))
    url: str = f"https://www.inegi.org.mx/app/api/denue/v1/consulta/Nombre/{business_name}/00/1/10/2086f9f0-045d-408f-b99e-0ac210f0fef3"
    req: requests.models.Response = requests.get(url=url)
    req_json: dict = req.json()
    email: list = []
    for establishment in req_json:
        if isinstance(establishment, dict) and establishment["Correo_e"] != "":
            email.append(establishment["Correo_e"])
    return JsonResponse(
        {"response": email
         }, status=200
    )


@csrf_exempt
def get_data_by_codigo_expediente(request: WSGIRequest) -> JsonResponse:
    body: dict = json.loads(request.body)
    codigo_expediente: str = body.get("codigo_expediente", None)
    status = 200
    if codigo_expediente:
        driver = init_chromedriver()
        driver.get("https://compranet.hacienda.gob.mx/esop/guest/go/public/opportunity/past?locale=es_MX")
        driver.get("https://compranet.hacienda.gob.mx/esop/toolkit/opportunity/opportunityList.do?reset=true&resetstored=true&oppList=CURRENT")
        driver.find_element_by_xpath('//*[@id="widget_filterPickerSelect"]/div[1]/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="filterPickerSelect_popup1"]/span[2]').click()
        driver.find_element_by_xpath('//*[@id="projectInfo_FILTER"]').send_keys(codigo_expediente)
        driver.find_element_by_xpath('//*[@id="projectInfo_FILTER_OPERATOR_ID"]').click()
        driver.execute_script("javascript:submitForm('opportunityListFilterForm','search');")
        try:
            driver.find_element_by_xpath('//*[@id="cntList"]/form/div/table/tbody/tr[2]/td[5]/a').click()
            url = driver.current_url
            url = urlparse.urlparse(url)
            retorno = parse_qs(url.query)['opportunityId'][0]
        except IOError:
            retorno = None
        driver.close()
    else:
        retorno = "Falta codigo_expediente"
        status = 400
    return JsonResponse(
        {"response": retorno
         }, status=status
    )


@csrf_exempt
def get_data_by_opportunity_id(request: WSGIRequest) -> JsonResponse:
    body: dict = json.loads(request.body)
    opportunity_id: str = body.get("opportunity_id", None)
    status = 200
    if opportunity_id:
        response = {}
        driver = init_chromedriver()
        driver.get("https://compranet.hacienda.gob.mx/esop/guest/go/public/opportunity/past?locale=es_MX")
        driver.get(f"https://compranet.hacienda.gob.mx/esop/toolkit/opportunity/opportunityDetail.do?opportunityId={opportunity_id}")
        source_code = driver.page_source
        driver.close()
        soup = BeautifulSoup(source_code, "lxml")
        tablas = soup.find_all("div", class_="form_answer")
        response["codigo_expediente"] = tablas[0].text.strip()
        response["descripcion_expediente"] = tablas[1].text.strip()
        response["descripcion_del_anuncio"] = tablas[2].text.strip()
        response["notas"] = tablas[3].text.strip()
        response["tipo_de_contratacion"] = tablas[4].text.strip()
        response["entidad_federativa"] = tablas[5].text.strip()
        response["plazo_de_participacion"] = tablas[6].text.strip()
        response["unidad_compradora"] = tablas[7].text.strip()
        response["nombre_operador_uc"] = tablas[8].text.strip()
        response["correo_operador_uc"] = tablas[9].text.strip()
        retorno = response
    else:
        retorno = "Falta opportunity_id"
        status = 400
    return JsonResponse(
        {"response": retorno
         }, status=status
    )
