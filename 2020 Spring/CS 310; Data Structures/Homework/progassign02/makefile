J = javac

H1 = progassign02

all: compile main

compile:
	{ \
	${J} -cp . ${H1}/Sorting/Sorting.java ;\
	${J} -cp . ${H1}/Sorting/SortingTest.java ;\
	}

main:
	${J} -cp . ${H1}/Sorting/SortingTest.java

jar:
	jar cvfm ${H1}.jar ${H1}/META-INF/MANIFEST.MF ${H1}
	
ujar:
	jar uvf ${H1}.jar ${H1}

uMan:
	jar ufm ${H1}.jar progassign02/META-INF/MANIFEST.MF

check:
	jar tf ${H1}.jar
