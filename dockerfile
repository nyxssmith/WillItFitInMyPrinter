FROM pymesh/pymesh:py3.7-slim

RUN apt update && apt install -y libstdc++6 python3-pip python3 

COPY main.py main.py

CMD ["sh", "-c", "python3 main.py"]

