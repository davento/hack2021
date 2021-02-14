CREATE DATABASE ergo;

drop table if exists my_user cascade;
CREATE TABLE my_user (
    firstname text not NULL,
    lastname text not NULL,
    username text  PRIMARY KEY,
    password text not NULL
);

drop table if exists speciality cascade;
CREATE TABLE speciality(
    title text PRIMARY KEY
);

drop table if exists r_user_speciality cascade;
CREATE TABLE r_user_speciality(
    username text, 
    title text,
    CONSTRAINT pk_rus PRIMARY KEY (username,title),
    CONSTRAINT fk_ufn FOREIGN KEY (username) REFERENCES my_user(username),
    CONSTRAINT fk_st FOREIGN KEY (title) REFERENCES speciality(title)
);

drop table if exists achievement cascade;
CREATE TABLE achievement(
    title   text PRIMARY KEY,
    document bytea not NULL
);

drop table if exists r_user_achievement cascade;
CREATE TABLE r_user_achievement(
    username text,
    title text,
    CONSTRAINT pk_rua PRIMARY KEY (username, title),
    CONSTRAINT fk_rufn FOREIGN KEY (username) REFERENCES my_user(username),
    CONSTRAINT fk_rat FOREIGN KEY (title) REFERENCES achievement(title)
);

drop table if exists dpoint cascade;
CREATE TABLE dpoint(
    id serial,
    fid int,
    content text not NULL,
    participation int DEFAULT 0,
    totalscore int DEFAULT 0,
    username text,
    paper_title text,
    CONSTRAINT pk_dip PRIMARY KEY (id, paper_title),
    CONSTRAINT fk_dpp FOREIGN KEY (paper_title) REFERENCES paper(title),
    CONSTRAINT fk_dpu FOREIGN KEY (username) REFERENCES my_user(username),
    CONSTRAINT u_id_fid UNIQUE (id,fid),
);

drop table if exists comment cascade;
CREATE TABLE comment(
    id  int PRIMARY KEY,
    dpoint  int,
    thecontent text not NULL,
    likes   int not NULL,
    dislikes    int not NULL,
    CONSTRAINT fk_cdpid FOREIGN KEY (dpoint) REFERENCES dpoint(id)
);

drop table if exists tag cascade;
CREATE TABLE tag(
    name text PRIMARY KEY
);

drop table if exists author cascade;
CREATE TABLE author(
    name text PRIMARY KEY
);

drop table if exists paper cascade;
CREATE TABLE paper(
    title text PRIMARY KEY,
    pusblisher text,
    pubd date,
    link text,
);

drop table if exists r_tag_paper cascade;
CREATE TABLE r_tag_paper(
    name text,
    paper text,
    CONSTRAINT pk_rtp PRIMARY KEY (name, paper),
    CONSTRAINT fk_ptp FOREIGN KEY (paper) REFERENCES paper(title),
    CONSTRAINT fk_ntp FOREIGN KEY (name) REFERENCES tag(name)
);

drop table if exists r_author_paper cascade;
CREATE TABLE r_author_paper(
    name text,
    paper text,
    CONSTRAINT pk_rap PRIMARY KEY (name, paper),
    CONSTRAINT fk_pap FOREIGN KEY (paper) REFERENCES paper(title),
    CONSTRAINT fk_nap FOREIGN KEY (name) REFERENCES author(name)
);

drop table if exists react cascade;
CREATE TABLE react(
    name text,
    comment int,
    score int,
    CONSTRAINT pk_rnc PRIMARY KEY (name, comment),
    CONSTRAINT fk_pap FOREIGN KEY (comment) REFERENCES comment(id),
    CONSTRAINT fk_nap FOREIGN KEY (name) REFERENCES author(name)
);

drop table if exists likes cascade;
CREATE TABLE likes(
    name text,
    dp integer,
    lstatus boolean,
    CONSTRAINT pk_lnp PRIMARY KEY (name, paper),
    CONSTRAINT fk_dpi FOREIGN KEY (dp) REFERENCES dpoint(id),
    CONSTRAINT fk_nou FOREIGN KEY (name) REFERENCES my_user(username)
);

drop table if exists reference cascade;
CREATE TABLE reference(
    paper1 text,
    paper2 text,
    CONSTRAINT pk_rpp PRIMARY KEY (paper1, paper2),
    CONSTRAINT fk_pap1 FOREIGN KEY (paper1) REFERENCES paper(title),
    CONSTRAINT fk_pap2 FOREIGN KEY (paper2) REFERENCES paper(title)
);