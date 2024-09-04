from xmlrpc.server import SimpleXMLRPCServer

def add(x,y):
        return x + y

def substract(x,y):
        return x - y

def multiply(x,y):
        return x * y

def divide(x,y):
        if y == 0:
            return "Erro de divisao por zero"
        return x / y

#Configuracao do servidor RPC
server = SimpleXMLRPCServer(('localhost', 8000))
print("Servidor RPC aguardando requisicoes...")

#registrando funcoes para serem chamadas remotamente
server.register_function(add, "add")
server.register_function(substract, "substract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")

#mantendo o servidor
server.serve_forever()