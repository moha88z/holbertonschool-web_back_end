// server.js
import http from 'http';

const app = http.createServer((req, res) => {
  res.end('Hello Node');
});

app.listen(1245);
