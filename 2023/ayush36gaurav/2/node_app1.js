const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello from Node.js App!\n');
});

server.listen(3500, '0.0.0.0', () => {
    console.log('Server running at http://0.0.0.0:3500/');

    // Simulating a delay of 45 seconds before exiting
    setTimeout(() => {
        console.log('Exiting Node.js App after 45 seconds');
        process.exit(200); // Exit with code 200
    }, 45000); // 45 seconds in milliseconds
});
