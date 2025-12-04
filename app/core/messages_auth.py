import copy

class authResponses:
  index =  {"code":1 , "message": "Bienvenido al Api de Authenticacion"}
  accessToken = {"code":1, "message":"Token de authenticacion de usuario"}
  accesoDenegado = {"code": 0, "message": "No esta permitido su acceso"}
  _404 = {"code": 0, "message": "Not Found"}
  _500 = {"code": 0, "message": "Error de Servidor"}
  
def addNextRoute(msj, nextRoute):
  message = copy.deepcopy(msj)
  message["next"] = nextRoute
  return message

def addObject(msj, key,val):
  message=  copy.deepcopy(msj)
  message[key] =val 
  return message

def messageToken(token, expires, nextRoute):
  msj = copy.deepcopy(authResponses.accessToken)
  msj["token"]= token
  msj["expires"]= expires
  msj = addNextRoute(msj, nextRoute)
  return msj