CREATE TABLE user(
    firstname   text,
    lastname    text,
    username    text,
    password    text
);

CREATE TABLE r_user_speciality(
    firstname text FOREIGN KEY REFERENCES user(firstname),
    title text FOREIGN KEY REFERENCES user(firstname),
    CONSTRAINT pk_rus PRIMARY KEY (firstname,title)
);

CREATE TABLE speciality(
    title    text
);

CREATE TABLE achivement(

);