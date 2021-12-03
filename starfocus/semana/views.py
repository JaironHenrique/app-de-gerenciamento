from django.shortcuts import render
import pandas as pd
import numpy as np
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px
import os

import semana

def dias (request):
    '''Visualização correspondente à pergunta: Qual dia da semana teve a duração mais longa de atividades?'''

    #Organizando os dados
    dados = pd.read_csv(os.path.join('.','db.sqlite3_atividade.csv'))
    dados["data"] = pd.to_datetime(dados["data"])
    dados["dia da semana"]= dados["data"].dt.dayofweek
    dados["dia da semana"]= dados["dia da semana"].map({0: "segunda", 1: "terça", 2: "quarta", 3: "quinta", 4: "sexta", 5: "sábado", 6: "domingo", }, na_action=None)


    dados_agrupados = dados.groupby(["dia da semana"]).sum()
    dados_ordenados = dados_agrupados.sort_values(by=["duracao"], ascending=False)["duracao"]
    lista_dia_semana = list(dados_ordenados.index)
    lista_duracao = list(dados_ordenados.values)

    #Preparando Visualização
    graphs = []
    graphs.append(go.Bar(x=lista_dia_semana,
                        y=lista_duracao,
                        hovertemplate="<b>%{x}</b><br>Pomodoros: %{y}<br>",
                        name="",
                        ))

    layout = {
        "title": "Desempenho de cada dia da semana | Dezembro - 2021",
        "xaxis_title": "Dias da semana",
        "yaxis_title": "Pomodoros",
        "height": 500,
        "width": 1200,
    }

    #Gerando o HTML
    plot_div = plot({"data": graphs, "layout": layout}, output_type="div")

    return render(request, "semana/index.html", context={"plot_div": plot_div})