from django.http.response import HttpResponse
from django.shortcuts import render
import pandas as pd
import numpy as np
import os

def pagina(request, quant):
    dados = pd.read_csv(os.path.join('.','db.sqlite3_usuario.csv')).sort_values('tempo', ascending=False)
    dados.reset_index(drop=True, inplace=True)
    dados = dados.iloc[:quant]
    mostrar = [ f"Nome: {dados.iloc[i].nome}, Tempo: {dados.iloc[i].tempo}" for i in range(quant)]
    return render(request, 'top/index.html', 
                  context={'mostrar': mostrar})