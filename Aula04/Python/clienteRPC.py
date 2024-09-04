import xmlrpc.client 

proxy =xmlrpc.client.ServerProxy("http://localhost:8000/")

print("Soma 10 + 5 =", proxy.add(10,5))
print("Subtracao 10 - 5 =", proxy.substract(10,5))
print("Multipicao 10 * 5 =", proxy.multiply(10,5))
print("divisao 10 / 5 =", proxy.divide(10,5))
print("divisao 10 / 0 =", proxy.divide(10,0))