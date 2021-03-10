C = g++

all: passwordGame

passwordGame: passwordGame.cpp
	${C} -std=c++11 -o $@.exe $^ -pthread
	
gitpull: 
	git pull origin master

gitpush:
	git push origin master
	
test:
	./passwordGame.exe test.txt

words:
	./passwordGame.exe words.txt

leet:
	./passwordGame.exe 1337speak.txt
	
gener:
	./passwordGame.exe passwordGenerator.cpp
