 #!/usr/bin/env python
"""This script prompts a user to enter a message to encode or decodeusing a classic Caeser shift substitution (3 letter shift)"""
import numpy as np
import matplotlib.pyplot as plt

T_TIME = np.arange(0, 36, 0.5) #received time
LEN_T = len(T_TIME)

TS = np.zeros(LEN_T)
TA = np.arange(11.5, 17, 0.5)#fiRSt half of transmit signal
TB = np.arange(16.5, 10.5, -0.5) #second half of transmit signal
SIGNAL = np.concatenate([TA, [17], TB])
PERIOD = len(TA) + len(TB) + 1

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




     

RS = np.zeros(LEN_T)

R_OFF = 5 #offset time
R_PERIODS = (LEN_T-R_OFF) // PERIOD
R_REM = np.mod(LEN_T-R_OFF, PERIOD)

R_REPEAT = np.tile(SIGNAL, R_PERIODS)
R_REMAINDER = SIGNAL[0:R_REM]
R_OFFSET = np.zeros(R_OFF)

RS = np.concatenate([R_OFFSET ,R_REPEAT, R_REMAINDER])

F_D = 4       #offset frequency
RS = RS + F_D #received signal offset


#LEN_T = len(TA) + len(TB) + 1 #length of transmit vector
#LEN_R = LEN_T; 
#T_TIME = np.arange(0, LEN_T-1+1, 1) #received time



T_D = 2
R_TIME = T_TIME + T_D

# plt.figure()
# plt.plot(T_TIME, TS)

# plt.figure()
# plt.plot(T_TIME, RS)

plt.figure()
plt.plot(T_TIME, RS, T_TIME,TS)
plt.figure()
plt.plot(T_TIME,np.abs(TS- RS))

plt.show()