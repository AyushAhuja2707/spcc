.MODEL SMALL
.STACK
.DATA
M1 DB 10,13,"WELCOME$"
M2 DB 10,13,"TCET$"
.CODE
.STARTUP
DISP M1
DISP M2
DISP1 M2,M1
.EXIT