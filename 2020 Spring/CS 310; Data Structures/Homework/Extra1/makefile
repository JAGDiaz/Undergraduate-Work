J = javac

H1 = LinkedLists

all: compile

compile:
	{ \
	${J} -cp . ${H1}/linkedlists/DataClass.java ;\
	${J} -cp . ${H1}/linkedlists/DuoNode.java ;\
	${J} -cp . ${H1}/linkedlists/DuoLinkedList.java ;\
	${J} -cp . ${H1}/linkedlists/LinkedListDemo.java ;\
	}

jar:
	jar cvfm ${H1}.jar ${H1}/META-INF/MANIFEST.MF ${H1}
	
ujar:
	jar uvf ${H1}.jar ${H1}

uMan:
	jar ufm ${H1}.jar progassign02/META-INF/MANIFEST.MF

check:
	jar tf ${H1}.jar
