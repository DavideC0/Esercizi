create table Paziente (
    cf varchar not null,
    nome varchar not null,
    cognome varchar not null,
	primary key (cf)
);

create table Ricovero (
    id serial not null,
    inizio date not null,
    fine date check(fine>inizio),
    paziente varchar not null,
    primary key(id),
    foreign key (paziente) references Paziente(cf) deferrable
);

create table SpecializzazioneMedica (
    nome varchar not null,
    primary key(nome)
);

create table Medico (
    codice integer not null,
    specializzazione varchar not null,
    primary key (codice),
    foreign key (specializzazione) references SpecializzazioneMedica(nome) deferrable
);

create table medico_resp (
    medico integer not null,
    ricovero integer not null,
    primary key (medico,ricovero),
    foreign key (medico) references Medico(codice) deferrable,
    foreign key (ricovero) references Ricovero(id) deferrable
);