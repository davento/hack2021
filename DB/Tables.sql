CREATE TABLE user(
    firstname   text not NULL,
    lastname    text not NULL,
    username    text PRIMARY KEY,
    password    text not NULL
);

CREATE TABLE speciality(
    title    text PRIMARY KEY
);

CREATE TABLE r_user_speciality(
    firstname text FOREIGN KEY REFERENCES user(firstname),
    title text FOREIGN KEY REFERENCES user(firstname),
    CONSTRAINT pk_rus PRIMARY KEY (firstname,title)
);

CREATE TABLE achivement(
    title   text PRIMARY KEY,
    document bytea not NULL,
);

CREATE TABLE r_user_achivemet(
    firstname text FOREIGN KEY REFERENCES user(firstname),
    title   text FOREIGN KEY REFERENCES achivement(title),
    CONSTRAINT pk_rua PRIMARY KEY (firstname, title)
);

CREATE TABLE dpoint(
    id int PRIMARY KEY,
    fid int FOREIGN KEY REFERENCES dpoint(id),
    statement text not NULL,
    participation   int not NULL,
    totalscore  int not NULL,
    CONSTRAINT u_id_fid UNIQUE (id,fid),
    CHECK   (id <> fid)
);

CREATE TABLE comment(
    id  int PRIMARY KEY,
    dpoint  int FOREIGN KEY REFERENCES dpoint(id),
    content text not NULL,
    likes   int not NULL,
    dislikes    int not NULL
);

CREATE TABLE tag(
    name    text PRIMARY KEY
);

CREATE TABLE author(
    name    text PRIMARY KEY
);

CREATE TABLE paper(
    title text PRIMARY KEY,
    tags text FOREIGN KEY REFERENCES tag(name),
    author text FOREIGN KEY REFERENCES author(name),
    based_on text FOREIGN KEY REFERENCES paper(title),
    pusblisher text,
    pubd date
);
