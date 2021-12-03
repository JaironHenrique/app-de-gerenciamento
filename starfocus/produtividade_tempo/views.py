from django.http.response import HttpResponse
from django.shortcuts import render
import pandas as pd
import numpy as np
from plotly.offline import plot
import plotly.graph_objects as go
import os

import produtividade_tempo


def pagina(request):
    """ 
    View demonstrating how to display a graph object
    on a web page with Plotly. 
    """

    # Organizando os dados
    dados = pd.read_csv(os.path.join('.','db.sqlite3_atividade.csv'))
    produtividade = dados.groupby(['data']).duracao.sum().to_frame()
    #print(produtividade.head())

    #plot
    graphs = []

    # Gráfico
    graphs.append(
        go.Line(x=produtividade.index, y=produtividade.duracao, name='Line y1')
    )

    # Configração de layout.
    layout = {
        'title': 'Seu desempenho',
        'xaxis_title': 'Dia',
        'yaxis_title': 'Número de Pomodoros',
        'height': 600,
        'width': 1200,
    }

    # Getting HTML needed to render the plot.
    plot_div = plot({'data': graphs, 'layout': layout}, 
                    output_type='div')

    return render(request, 'produtividade_tempo_templates/index.html', 
                  context={'plot_div': plot_div})