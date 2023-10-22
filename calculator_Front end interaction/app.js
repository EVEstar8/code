const express = require('express');
const bodyParser = require('body-parser');
const connection = require('./db');

const app = express();
app.use(bodyParser.json());

app.post('/api/calculator_history', (req, res) => {
  const { expression, result } = req.body;
  const sql = 'INSERT INTO history (expression, result) VALUES (?, ?)';
  connection.query(sql, [expression, result], (err, results, fields) => {
    if (err) {
      console.error('Error inserting data to MySQL database: ' + err.stack);
      res.status(500).send('Error inserting data to MySQL database');
      return;
    }
    console.log('Data inserted to MySQL database with ID ' + results.insertId);
    res.status(200).send('Data inserted to MySQL database');
  });
});

app.get('/api/calculator_history', (req, res) => {
  const sql = 'SELECT * FROM history';
  connection.query(sql, (err, results, fields) => {
    if (err) {
      console.error('Error querying data from MySQL database: ' + err.stack);
      res.status(500).send('Error querying data from MySQL database');
      return;
    }
    console.log('Data queried from MySQL database');
    res.status(200).json(results);
  });
});

module.exports = app;