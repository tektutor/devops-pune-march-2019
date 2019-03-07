FROM ubuntu:16.04
MAINTAINER Jeganathan Swaminathan <jegan@tektutor.org>

ENV http_proxy http://10.19.16.165:8080
ENV https_proxy http://10.19.16.165:8080

RUN apt-get update && apt-get install -y openssh-server python-minimal git 
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

#This copies the public key to the docker image under the specified directory location
COPY authorized_keys /root/.ssh/authorized_keys

#Opening up ports 22 for SSH Server and 80 for any web/app servers we may later install via Ansible.
EXPOSE 22 
EXPOSE 80 

#Configuring SSH Server as the default start-up application on containers created out of this Docker image.
CMD ["/usr/sbin/sshd", "-D"]
