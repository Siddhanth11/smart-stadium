-- ==========================================
-- Smart Stadium GenAI Database
-- ==========================================

CREATE DATABASE IF NOT EXISTS smart_stadium;

USE smart_stadium;

-- ==========================================
-- Users
-- ==========================================

CREATE TABLE users (

    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    email VARCHAR(100) UNIQUE NOT NULL,

    password VARCHAR(255) NOT NULL,

    role ENUM(
        'admin',
        'fan',
        'volunteer'
    ) DEFAULT 'fan',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

-- ==========================================
-- Teams
-- ==========================================

CREATE TABLE teams (

    id INT AUTO_INCREMENT PRIMARY KEY,

    team_name VARCHAR(100),

    country VARCHAR(100)

);

-- ==========================================
-- Stadium
-- ==========================================

CREATE TABLE stadium (

    id INT AUTO_INCREMENT PRIMARY KEY,

    stadium_name VARCHAR(100),

    city VARCHAR(100),

    capacity INT

);

-- ==========================================
-- Matches
-- ==========================================

CREATE TABLE matches (

    id INT AUTO_INCREMENT PRIMARY KEY,

    team1 VARCHAR(100),

    team2 VARCHAR(100),

    match_date DATE,

    match_time TIME,

    stadium VARCHAR(100),

    status VARCHAR(30)

);

-- ==========================================
-- Tickets
-- ==========================================

CREATE TABLE tickets (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT,

    match_id INT,

    seat_number VARCHAR(20),

    category VARCHAR(30),

    price DECIMAL(10,2),

    qr_code VARCHAR(255),

    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
        REFERENCES users(id),

    FOREIGN KEY (match_id)
        REFERENCES matches(id)

);

-- ==========================================
-- Volunteers
-- ==========================================

CREATE TABLE volunteers (

    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100),

    email VARCHAR(100),

    phone VARCHAR(20),

    assigned_area VARCHAR(100)

);

-- ==========================================
-- Emergency Reports
-- ==========================================

CREATE TABLE emergency (

    id INT AUTO_INCREMENT PRIMARY KEY,

    emergency_type VARCHAR(100),

    location VARCHAR(100),

    description TEXT,

    reported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

-- ==========================================
-- Parking
-- ==========================================

CREATE TABLE parking (

    id INT AUTO_INCREMENT PRIMARY KEY,

    parking_zone VARCHAR(50),

    total_slots INT,

    available_slots INT

);

-- ==========================================
-- Analytics
-- ==========================================

CREATE TABLE analytics (

    id INT AUTO_INCREMENT PRIMARY KEY,

    attendance INT,

    revenue DECIMAL(12,2),

    crowd_level VARCHAR(30),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

-- ==========================================
-- Chat History
-- ==========================================

CREATE TABLE chatbot_history (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT,

    question TEXT,

    answer TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
        REFERENCES users(id)

);