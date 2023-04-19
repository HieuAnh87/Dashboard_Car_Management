CREATE TABLE car_mnt.graph ( 
    user_id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(20) NOT NULL , 
    major VARCHAR(40) NOT NULL , 
    status VARCHAR(20) NOT NULL , 
    PRIMARY KEY (user_id)
) ENGINE = InnoDB;


INSERT INTO graph(name, major, status) VALUES ("Hòa","An toàn thông tin","Đồng ý");
INSERT INTO graph(name, major, status) VALUES ("Huy","Công nghệ thông tin","Từ chối");
INSERT INTO graph(name, major, status) VALUES ("Hùng","Điện tử viễn thông","Đang chờ");
INSERT INTO graph(name, major, status) VALUES ("Hải","Điện tử viễn thông","Đồng ý");
INSERT INTO graph(name, major, status) VALUES ("Nam","Công nghệ thông tin","Đang chờ");
INSERT INTO graph(name, major, status) VALUES ("Đông","Điện tử viễn thông","Đang chờ");
