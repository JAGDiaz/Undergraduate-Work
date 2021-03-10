
J = javac

P = Practice

all: euclid sum menu pyramid

euclid: euclid.java
	${J} $^

sum: sum.java
	${J} $^

menu: menu.java
	${J} $^

pyramid: pyramid.java
	${J} $^

jar:
	{ \
	cd .. ;\
	jar cvf ${P}.jar ${P} ;\
	mv ${P}.jar ${P} ;\
	} 

check:
	jar tf ${P}.jar


