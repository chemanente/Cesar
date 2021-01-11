import pymqi
import sys
import os

###################Create Channel Server##################

def CRT_CHANNEL(qmgr,channel_name):

    channel_type = pymqi.CMQXC.MQCHT_SVRCONN

    args = {pymqi.CMQCFC.MQCACH_CHANNEL_NAME: channel_name,
            pymqi.CMQCFC.MQIACH_CHANNEL_TYPE: channel_type}

    pcf = pymqi.PCFExecute(qmgr)
    pcf.MQCMD_CREATE_CHANNEL(args)


###################Create Queue Local##################

def CRT_QUEUE(qmgr, queue_name):
    queue_type = pymqi.CMQC.MQQT_LOCAL
    max_depth = 1000

    args = {pymqi.CMQC.MQCA_Q_NAME: queue_name,
            pymqi.CMQC.MQIA_Q_TYPE: queue_type,
            pymqi.CMQC.MQIA_MAX_Q_DEPTH: max_depth}

    pcf = pymqi.PCFExecute(qmgr)
    pcf.MQCMD_CREATE_Q(args)


######################################variavel###############

MQ_NAME = os.environ['MQ_NAME']
CHANNEL_SRV = os.environ['CHANNEL_SRV']
HOST = os.environ['HOST']
PORT = os.environ['PORT']
queue_name = os.environ['QUEUE_NAME']
channel_name = os.environ['CHANNEL_NAME']

conn_info = '%s(%s)' % (HOST,PORT)
qmgr = pymqi.connect(MQ_NAME, CHANNEL_SRV, conn_info)

if queue_name != 'QUEUE':
    if queue_name and len(queue_name) > 0:
        print("Criando Filas")
        #Verifica se for apenas uma fila ou uma lista
        find_coma = queue_name.find(',')
        if find_coma > 0:
            queue_list = queue_name.split(',')
        else:
            queue_list = [queue_name]
        for queue in queue_list:
            print("criando Fila: ",queue.rstrip("\n"))
            CRT_QUEUE(qmgr,queue.rstrip("\n"))
            print("Fila Criado com successo")
else:
    print("Nao ha fila a ser criada")


if channel_name != 'CHANNEL':
    if channel_name and len(channel_name) > 0:
        print("Criando Canais")
        #Verifica se for apenas uma fila ou uma lista
        find_coma = channel_name.find(',')
        if find_coma > 0:
            channel_list = channel_name.split(',')
        else:
            channel_list = [channel_name]
        for channel in channel_list:
            print("criando Canal: ",channel.rstrip("\n"))
            CRT_CHANNEL(qmgr,channel.rstrip("\n"))
            print("Canal Criado com successo")
else:
    print("Nao ha canal a ser criado")

qmgr.disconnect()
