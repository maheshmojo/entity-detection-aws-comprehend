RUN apt-get update && apt-get install -y  \
    sudo \
    gdebi-core \

RUN wget https://download2.rstudio.org/server/bionic/amd64/rstudio-server-1.4.1106-amd64.deb

RUN sudo gdebi rstudio-server-1.4.1106-amd64.deb

RUN wget https://download3.rstudio.org/ubuntu-14.04/x86_64/shiny-server-1.5.16.958-amd64.deb

RUN sudo gdebi shiny-server-1.5.16.958-amd64.deb

EXPOSE 3838 8787
