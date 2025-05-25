const http = require('http');
const fs = require('fs').promises;

const app = http.createServer((req, res) => {
  const { url } = req;

  if (url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    const database = process.argv[2];

    fs.readFile(database, 'utf8')
      .then((data) => {
        const lines = data.split('\n').filter((line) => line.trim() !== '');
        const students = lines.slice(1);

        const fields = {};
        for (const student of students) {
          const [firstname, , , field] = student.split(',');
          if (!fields[field]) fields[field] = [];
          fields[field].push(firstname);
        }

        let responseText = 'This is the list of our students\n';
        responseText += `Number of students: ${students.length}\n`;

        for (const [field, names] of Object.entries(fields)) {
          responseText += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
        }

        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(responseText.trim()); // Trim para evitar \n final extra
      })
      .catch(() => {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('Cannot load the database');
      });
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not found');
  }
});

app.listen(1245);

module.exports = app;
