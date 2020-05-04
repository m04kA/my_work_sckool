-- My kod:
-- Это надо добавить в скрипт с 3-го урока

DROP TABLE IF EXISTS tegs;
CREATE TABLE tegs (
	id SERIAL PRIMARY KEY,
	user_id BIGINT UNSIGNED DEFAULT NULL,
	`text` varchar(255),
	
	FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS shop_produkts;
CREATE TABLE shop_produkts (
	id_produkt SERIAL PRIMARY KEY,
	user_id BIGINT UNSIGNED DEFAULT NULL,
	price BIGINT unsigned NOT NULL,
	
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (id_produkt) REFERENCES media(id)
);



DROP TABLE IF EXISTS stickers;
CREATE TABLE stickers (
	id_stiker SERIAL PRIMARY KEY,
	
	FOREIGN KEY (id_stiker) REFERENCES shop_produkts(id_produkt)
);


