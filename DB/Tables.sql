drop table if exists my_user;
CREATE TABLE my_user (
    firstname   text not NULL,
    lastname    text not NULL,
    username    text  PRIMARY KEY,
    password    text not NULL
);

drop table if exists speciality;
CREATE TABLE speciality(
    title    text PRIMARY KEY
);

drop table if exists r_user_speciality;
CREATE TABLE r_user_speciality(
    username text, 
    title text,
    CONSTRAINT pk_rus PRIMARY KEY (username,title),
    CONSTRAINT fk_ufn FOREIGN KEY (username) REFERENCES my_user(username),
    CONSTRAINT fk_st FOREIGN KEY (title) REFERENCES speciality(title)
);

drop table if exists achivement;
CREATE TABLE achivement(
    title   text PRIMARY KEY,
    document bytea not NULL
);

drop table if exists r_user_achivemet;
CREATE TABLE r_user_achivemet(
    username text,
    title   text,
    CONSTRAINT pk_rua PRIMARY KEY (username, title),
    CONSTRAINT fk_rufn FOREIGN KEY (username) REFERENCES my_user(username),
    CONSTRAINT fk_rat FOREIGN KEY (title) REFERENCES achivement(title)
);

drop table if exists dpoint;
CREATE TABLE dpoint(
    id int PRIMARY KEY,
    fid int,
    thecontent text not NULL,
    participation   int not NULL,
    totalscore  int not NULL,
    CONSTRAINT u_id_fid UNIQUE (id,fid),
    CHECK   (id <> fid)
);

drop table if exists comment;
CREATE TABLE comment(
    id  int PRIMARY KEY,
    dpoint  int,
    thecontent text not NULL,
    likes   int not NULL,
    dislikes    int not NULL,
    CONSTRAINT fk_cdpid FOREIGN KEY (dpoint) REFERENCES dpoint(id)
);

drop table if exists tag;
CREATE TABLE tag(
    name    text PRIMARY KEY
);

drop table if exists author;
CREATE TABLE author(
    name    text PRIMARY KEY
);

drop table if exists paper;
CREATE TABLE paper(
    title text PRIMARY KEY,
    tag text,
    author text,
    based_on text,
    pusblisher text,
    pubd date,
    CONSTRAINT fk_ptn FOREIGN KEY (tag) REFERENCES tag(name),
    CONSTRAINT fk_pan FOREIGN KEY (author) REFERENCES author(name),
    CONSTRAINT fk_ppt FOREIGN KEY (based_on) REFERENCES paper(title)
);
