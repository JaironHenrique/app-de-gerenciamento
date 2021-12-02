# -*- coding: utf-8 -*-
#import os
#import sys
import datetime
import numpy as np
import pandas as pd


# Foi utilizada uma query SQLite para selecionar as tabelas 
# do banco de dados e exportá-las como .csv

atividades = pd.read_csv("./db.sqlite3_atividade.csv", encoding='utf-8')
usuarios = pd.read_csv("./db.sqlite3_usuario.csv", encoding='utf-8')

print(atividades.head(), '\n\n\n', usuarios.head())

