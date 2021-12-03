from django.shortcuts import render
import pandas as pd
import numpy as np
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px
import os

import desempenho_atividades

# Create your views here.

def visualizacao(request):
    '''
    Cria uma visualização que responde à pergunta de negócio: "A quais atividades o usuário dedicou 
    mais tempo?"
    '''
    #Organizando os dados
    dados = pd.read_csv(os.path.join('.','db.sqlite3_atividade.csv'))
    dados_agrupados = dados.groupby(['nome']).sum()
    dados_ordenados = dados_agrupados.sort_values(by=['duracao'], ascending=False)['duracao']
    lista_atv = list(dados_ordenados.index)
    lista_duracao = list(dados_ordenados.values)

    #Preparando a visualização
    graphs = []
    graphs.append(go.Bar(x=lista_atv, 
                        y=lista_duracao, 
                        hovertemplate="<b>%{x}</b><br>Pomodoros: %{y}<br>",
                        name='',
                        ))
    layout = {
            'title': "Seu desempenho do mês | Dezembro - 2021",
            'xaxis_title': '',
            'yaxis_title': 'Pomodoros',
            'height': 500,
            'width': 1200
    }
    
    # Gerando o HTML
    plot_div = plot({'data': graphs, 'layout': layout}, output_type='div')
    return render(request, 'desempenho_atividades/index.html', 
                  context={'plot_div': plot_div})