FROM python:3
RUN git clone https://github.com/FrancoBertoldiMariglio/sudoku-FrancoBertoldiMariglio.git
WORKDIR /4-in-line
#RUN pip install -r requirements.txt
#RUN pip install parameterized 
#SOLO SI LOS TESTS USAN parameterized
CMD ["python3 -m", "unittest"]

