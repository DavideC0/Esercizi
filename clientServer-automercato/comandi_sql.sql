INSERT INTO filiale (nome) VALUES
('Filiale Milano'),
('Filiale Roma'),
('Filiale Napoli'),
('Filiale Torino'),
('Filiale Firenze');

INSERT INTO automobile (targa, marca, modello, prezzo_base, filiale) VALUES
('AA111BB', 'Fiat', 'Panda', 9500.00, 1),
('CC222DD', 'Ford', 'Focus', 12000.00, 2),
('EE333FF', 'Volkswagen', 'Golf', 20000.00, 3),
('GG444HH', 'Toyota', 'Yaris', 18000.00, 4),
('II555JJ', 'Tesla', 'Model 3', 45000.00, 5);

INSERT INTO motocicletta (targa, marca, modello, prezzo_base, filiale) VALUES
('MM111NN', 'Yamaha', 'MT-07', 7500.00, 1),
('OO222PP', 'Kawasaki', 'Ninja 650', 8900.00, 2),
('QQ333RR', 'Ducati', 'Panigale V4', 23000.00, 3),
('SS444TT', 'Honda', 'CB500F', 6500.00, 4),
('UU555VV', 'BMW', 'R 1250 GS', 17000.00, 5);

INSERT INTO vendita_auto (targa_auto, data_vendita, prezzo_vendita) VALUES
('AA111BB', '2024-01-10', 9700.00),
('CC222DD', '2024-02-15', 12500.00),
('EE333FF', '2024-03-20', 20500.00),
('GG444HH', '2024-04-25', 18200.00),
('II555JJ', '2024-05-30', 46000.00);

INSERT INTO vendita_moto (targa_moto, data_vendita, prezzo_vendita) VALUES
('MM111NN', '2024-02-12', 7600.00),
('OO222PP', '2024-03-18', 9000.00),
('QQ333RR', '2024-04-22', 23500.00),
('SS444TT', '2024-05-28', 6700.00),
('UU555VV', '2024-06-15', 17500.00);

INSERT INTO Acessorio (nome, tipo_veicolo_compatibilità, descrizione, prezzo) VALUES
('Portapacchi', 'Auto', 'Portapacchi universale per auto di medie dimensioni', 120.50),
('Navigatore GPS', 'Auto', 'Navigatore GPS touchscreen con mappe aggiornate', 250.00),
('Coperture sedili', 'Auto', 'Set di coperture in pelle ecologica per sedili anteriori', 85.75),
('Catene da neve', 'Auto', 'Catene da neve per pneumatici di misura standard', 75.00),
('Tappetini in gomma', 'Auto', 'Set di tappetini resistenti all’acqua e facili da pulire', 40.00),
('Supporto smartphone', 'Moto', 'Supporto per smartphone resistente alle intemperie', 35.90),
('Casco modulare', 'Moto', 'Casco modulare con doppia visiera anti-graffio', 150.00),
('Guanti riscaldati', 'Moto', 'Guanti da moto con sistema di riscaldamento a batteria', 80.00);