J = javac

H1 = homework01

all: compile main

compile:
	{ \
	${J} -cp . ${H1}/Classes/Person.java ;\
	${J} -cp . ${H1}/Classes/Student.java ;\
	${J} -cp . ${H1}/Interfaces/Studentmethods.java ;\
	}

main:
	${J} -cp . ${H1}/MainClasses/MainClass.java

jar:
	jar cvfm ${H1}.jar ${H1}.MF ${H1}
	
ujar:
	jar uvf ${H1}.jar ${H1}
uMan:
	jar cfm ${H1}.jar ${H1}.MF

check:
	jar tf ${H1}.jar
