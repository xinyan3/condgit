FROM ubuntu:xenial
MAINTAINER Sky Cheng <sky831202@gmail.comcom>


RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list


RUN apt-get update && apt-get install --no-install-recommends -y ca-certificates curl openssh-server net-tools wget git build-essential  python python-pip iproute iproute-doc vim && rm -rf /var/lib/apt/lists/*

# https://github.com/Yelp/dumb-init
RUN curl -fLsS -o /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.0.2/dumb-init_1.0.2_amd64 && chmod +x /usr/local/bin/dumb-init

ENV MAVEN_VERSION=3.5.2

# Install Maven
RUN wget -q http://www-eu.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz && \
    mkdir /opt/maven && \
    tar xzf apache-maven-${MAVEN_VERSION}-bin.tar.gz -C /opt/maven && \
    rm apache-maven-${MAVEN_VERSION}-bin.tar.gz && \
    ln -s /opt/maven/apache-maven-${MAVEN_VERSION}/bin/mvn /usr/local/bin/mvn

ENV TOMCAT_VERSION=8.5.30
RUN wget -q http://mirrors.shu.edu.cn/apache/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz &&\
    mkdir /opt/tomcat8 && \
    tar xzf apache-tomcat-${TOMCAT_VERSION}.tar.gz -C /opt/tomcat8 && \
    rm apache-tomcat-${TOMCAT_VERSION}.tar.gz  


#Oracle JDK
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list && \
    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \
    apt-get update && \
    echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
    DEBIAN_FRONTEND=noninteractive  apt-get install -y oracle-java8-installer oracle-java8-set-default && \
    update-alternatives --remove java /usr/lib/jvm/java-9-openjdk-amd64/bin/java && \
    rm -rf /var/cache/oracle-jdk8-installer && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle


# 添加测试用户admin，密码admin，并且将此用户添加到sudoers里  
RUN groupadd admin && mkdir -p /home/admin
RUN useradd -d /home/admin -g admin admin && chown -R admin:admin /home/admin
RUN echo "admin:admin" | chpasswd  
RUN echo "admin   ALL=(ALL)       ALL" >> /etc/sudoers  
#change root password
RUN echo "root:root" | chpasswd  

COPY sshd_config /etc/ssh/sshd_config

COPY entrypoint.sh /entrypoint.sh


RUN chmod a+x /entrypoint.sh



ENTRYPOINT ["/usr/local/bin/dumb-init", "/entrypoint.sh"]



