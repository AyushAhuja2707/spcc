LABEL	OPCODE	OPERAND	**
BEG:	START	100
	USING	*,15
	L	1,FIVE
	A	1,FOUR
	S	T1,TEMP
FIVE	DC	F'5'
FOUR	DC	F'4'
TEMP	DS	1'F'
	END