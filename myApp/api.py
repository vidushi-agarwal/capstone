import sys
import base64
import requests
import json
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.latex import parse_latex

# put desired file path here
# file_path = './Untitled.png'

dict={}############
from sympy import *
init_printing(use_unicode=False, wrap_line=False)
# x = Symbol('x')
# integrate(x**2 + x + 1, x)

def func(file_path):
    image_uri = "data:image/jpg;base64," + \
        base64.b64encode(open(file_path, "rb").read()).decode()
    r = requests.post("https://api.mathpix.com/v3/latex",
                      data=json.dumps(
                          {'src': image_uri, 'formats': ['latex_normal', 'latex_simplified'], 'ocr':['math']}),
                      headers={"app_id": "madhavgoyal_live_com", "app_key": '691af155706c16392cff',
                               "Content-type": "application/json"})
    a = json.loads(r.text)['latex_normal']
    print(a)#this will give the result
    print(parse_expr(str(parse_latex(a))))
    dict["result"]=a######
    dict["latex1"]=parse_expr(str(parse_latex(a)))########
    # b=str(dict["latex1"])
    # b=b[9:-1]
    # x = Symbol('x')
    # print(integrate(eval(b)))
    return dict############


