 #!/usr/bin/env python
"""This script prompts a user to enter a
message to encode or decodeusing a classic
Caeser shift substitution (3 letter shift)"""

from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/getSignalGraph")
def getSignalGraph():
    stime=int(request.args.get('stime'))
    etime=int(request.args.get('etime'))
    timeres=int(request.args.get('timeres'))
    period=int(request.args.get('period'))
    bw=10;

    T_TIME = np.arange(stime, etime, timeres) #received time
    LEN_T = len(T_TIME)
    
    FPoints = (period/2 - 0) / timeres
    

    TS = np.zeros(LEN_T)
    TA = np.arange( 0-bw/FPoints, bw-bw/FPoints, bw/FPoints ) #first half of transmit signal
    TB = np.arange(bw, 0, -bw/FPoints )    #second half of transmit signal

    SIGNAL = np.concatenate([TA,  TB])
    PERIOD = len(TA) + len(TB)
    
    T_OFF = 0;
    T_PERIODS = (LEN_T-T_OFF) // PERIOD
    T_REM = np.mod(LEN_T-T_OFF, PERIOD)

    T_REPEAT = np.tile(SIGNAL, T_PERIODS)
    print(len(T_REPEAT))
    T_REMAINDER = SIGNAL[0:T_REM]
    print(len(T_REMAINDER))
    T_OFFSET = np.zeros(T_OFF)
    print(len(T_OFFSET))

    
    TS = np.concatenate([T_OFFSET ,T_REPEAT, T_REMAINDER])

    return jsonify(
        x=T_TIME.tolist(),
        y=TS.tolist(),
        stime=stime,
        period=period
    );
