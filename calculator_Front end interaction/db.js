const mysql = require('mysql2');

const connection = mysql.createConnection({
  host: 'LAPTOP-NH9UT8J0',
  user: 'root',
  password: 'pyx2015771',
  database: 'calculator'
});

connection.connect((err) => {
  if (err) {
    console.error('Error connecting to MySQL database: ' + err.stack);
    return;
  }
  console.log('Connected to MySQL database with ID ' + connection.threadId);
});

module.exports = connection;