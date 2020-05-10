import requests
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np


#request para evolución de demanda máxima mensual (Peninsular) - 2020
r = requests.get('https://apidatos.ree.es/es/datos/demanda/evolucion?start_date=2020-01-01T00:00&end_date=2020-03-29T22:00&time_trunc=day&geo_limit=peninsular&geo_ids=8741')
r_a = requests.get('https://apidatos.ree.es/es/datos/demanda/evolucion?start_date=2020-03-30T00:00&end_date=2020-04-30T22:00&time_trunc=day&geo_limit=peninsular&geo_ids=8741')

#request para evolución de demanda máxima mensual (Peninsular) - 2019
r1 = requests.get('https://apidatos.ree.es/es/datos/demanda/evolucion?start_date=2019-01-01T00:00&end_date=2019-03-31T22:00&time_trunc=day&geo_limit=peninsular&geo_ids=8741')
r1_a = requests.get('https://apidatos.ree.es/es/datos/demanda/evolucion?start_date=2019-04-01T00:00&end_date=2019-04-30T22:00&time_trunc=day&geo_limit=peninsular&geo_ids=8741')

#r = requests.get('https://apidatos.ree.es/es/datos/demanda/variacion-demanda?start_date=2020-01-01T00:00&end_date=2020-01-30T22:00&time_trunc=day&geo_limit=peninsular&geo_ids=8741')
#r = requests.get('https://apidatos.ree.es/es/datos/balance/balance-electrico?start_date=2019-01-01T00:00&end_date=2019-01-31T22:00&time_trunc=day')
#r = requests.get('https://apidatos.ree.es/es/datos/demanda/evolucion?start_date=2020-01-01T00:00&end_date=2020-03-08T22:00&time_trunc=day&geo_limit=peninsular&geo_ids=8741')

#normalización del fichero .json extraido de aplicación API
b=json.loads(r.text)
c=b['included']
d=c[0]
e=d['attributes']
f=e['values']

b_a=json.loads(r_a.text)
c_a=b_a['included']
d_a=c_a[0]
e_a=d_a['attributes']
f_a=e_a['values']

b1=json.loads(r1.text)
c1=b1['included']
d1=c1[0]
e1=d1['attributes']
f1=e1['values']

b1_a=json.loads(r1_a.text)
c1_a=b1_a['included']
d1_a=c1_a[0]
e1_a=d1_a['attributes']
f1_a=e1_a['values']

#generar objeto DataFrame
elect20=pd.DataFrame(f)
elect20_a=pd.DataFrame(f_a)
elect19=pd.DataFrame(f1)
elect19_a=pd.DataFrame(f1_a)

#renombrar/eliminar columnas del objeto DataFrame
elect20=elect20.rename(columns={'value':'ev_demanda','percentage':'percentage','datetime':'date'})
elect20=elect20.drop(['percentage'],axis=1)
elect20_a=elect20_a.rename(columns={'value':'ev_demanda','percentage':'percentage','datetime':'date'})
elect20_a=elect20_a.drop(['percentage'],axis=1)

elect19=elect19.rename(columns={'value':'ev_demanda','percentage':'percentage','datetime':'date'})
elect19=elect19.drop(['percentage'],axis=1)
elect19_a=elect19_a.rename(columns={'value':'ev_demanda','percentage':'percentage','datetime':'date'})
elect19_a=elect19_a.drop(['percentage'],axis=1)


#generación columnas con diferenciación mes-dia-año
elect20['year']=pd.DatetimeIndex(elect20['date']).year
elect20['month']=pd.DatetimeIndex(elect20['date']).month
elect20['day']=pd.DatetimeIndex(elect20['date']).day
elect20_a['year']=pd.DatetimeIndex(elect20_a['date']).year
elect20_a['month']=pd.DatetimeIndex(elect20_a['date']).month
elect20_a['day']=pd.DatetimeIndex(elect20_a['date']).day
elect20=elect20.append(elect20_a)
elect20.reset_index(drop=True, inplace=True)
elect20_jan=elect20[elect20['month'] == 1]
elect20_feb=elect20[elect20['month'] == 2]
elect20_mar=elect20[elect20['month'] == 3]
elect20_apr=elect20[elect20['month'] == 4]


elect19['year']=pd.DatetimeIndex(elect19['date']).year
elect19['month']=pd.DatetimeIndex(elect19['date']).month
elect19['day']=pd.DatetimeIndex(elect19['date']).day
elect19_a['year']=pd.DatetimeIndex(elect19_a['date']).year
elect19_a['month']=pd.DatetimeIndex(elect19_a['date']).month
elect19_a['day']=pd.DatetimeIndex(elect19_a['date']).day
elect19=elect19.append(elect19_a)
elect19.reset_index(drop=True, inplace=True)
elect19_jan=elect19[elect19['month'] == 1]
elect19_feb=elect19[elect19['month'] == 2]
elect19_mar=elect19[elect19['month'] == 3]
elect19_apr=elect19[elect19['month'] == 4]


#maximo evoluciOn demanda por mes
#elect_month20=elect20.groupby(['month'])['ev_demanda'].max()
#elect_month19=elect19.groupby(['month'])['ev_demanda'].max()

#generamos gráfico para la comparar curvas de demanda

#gráfico anual
fig, ax1=plt.subplots()
elect20['ev_demanda'].plot(label='2020')
elect19['ev_demanda'].plot(label='2019')
ax1.set_xlabel("Days")
ax1.set_ylabel("ev_demanda")
ax1.legend(loc='center', title='año', bbox_to_anchor=(1, 0.5))
fig.suptitle('ev_demanda enero-febrero-marzo-abril 2020/2019', fontsize=15)
# Guardamos el gráfico
plt.savefig("Grafico_anual.png")

#gráfico mensual - enero
fig, ax2=plt.subplots()
elect20_jan['ev_demanda'].plot(label='2020')
elect19_jan['ev_demanda'].plot(label='2019')
ax2.set_xlabel("Days")
ax2.set_ylabel("ev_demanda")
ax2.legend(loc='center', title='año', bbox_to_anchor=(1, 0.5))
fig.suptitle('ev_demanda enero 2020/2019', fontsize=15)
# Guardamos el gráfico
plt.savefig("Grafico_enero.png")

#gráfico mensual-febrero
fig, ax3=plt.subplots()
elect20_feb['ev_demanda'].plot(label='2020')
elect19_feb['ev_demanda'].plot(label='2019')
ax3.set_xlabel("Days")
ax3.set_ylabel("ev_demanda")
ax3.legend(loc='center', title='año', bbox_to_anchor=(1, 0.5))
fig.suptitle('ev_demanda febrero 2020/2019', fontsize=15)
# Guardamos el gráfico
plt.savefig("Grafico_febrero.png")

#gráfico mensual-marzo
fig, ax4=plt.subplots()
elect20_mar['ev_demanda'].plot(label='2020')
elect19_mar['ev_demanda'].plot(label='2019')
ax4.set_xlabel("Days")
ax4.set_ylabel("ev_demanda")
ax4.legend(loc='center', title='año', bbox_to_anchor=(1, 0.5))
fig.suptitle('ev_demanda marzo 2020/2019', fontsize=15)
# Guardamos el gráfico
plt.savefig("Grafico_marzo.png")

#gráfico mensual-abril
fig, ax5=plt.subplots()
elect20_apr['ev_demanda'].plot(label='2020')
elect19_apr['ev_demanda'].plot(label='2019')
ax5.set_xlabel("Days")
ax5.set_ylabel("ev_demanda")
ax5.legend(loc='center', title='año', bbox_to_anchor=(1, 0.5))
fig.suptitle('ev_demanda abril 2020/2019', fontsize=15)
# Guardamos el gráfico
plt.savefig("Grafico_abril.png")

# Convertimos el df en un csv
elect20.to_csv('Consumo_elect_COVID_2020.csv') 
elect19.to_csv('Consumo_elect_COVID_2019.csv')
