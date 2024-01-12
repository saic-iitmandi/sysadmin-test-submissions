const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello from Node.js App!\n');
});

server.listen(3000, '0.0.0.0', () => {
    console.log('Server running at http://0.0.0.0:3000/');

    // Simulating a delay of 45 seconds before exiting
    setTimeout(() => {
        console.log('Exiting Node.js App after 60 seconds');
        process.exit(100); // Exit with code 130
    }, 60000); // 60 seconds in milliseconds
});
