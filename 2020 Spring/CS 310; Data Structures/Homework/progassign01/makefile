J = javac

H1 = progassign01

all: compile main

compile:
	{ \
	${J} -cp . ${H1}/Interface/QueueSpecs.java ;\
	${J} -cp . ${H1}/Interface/StackSpecs.java ;\
	${J} -cp . ${H1}/Data/DataClass.java ;\
	${J} -cp . ${H1}/Container/Node.java ;\
	${J} -cp . ${H1}/Container/LLStack.java ;\
	${J} -cp . ${H1}/Container/StackQ.java ;\
	}

main:
	${J} -cp . ${H1}/Driver/Driver.java

jar:
	jar cvfm ${H1}.jar ${H1}/META-INF/MANIFEST.MF ${H1}
	
ujar:
	jar uvf ${H1}.jar ${H1}

uMan:
	jar ufm ${H1}.jar progassign01/META-INF/MANIFEST.MF

check:
	jar tf ${H1}.jar
