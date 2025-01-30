const express = require('express');
const multer = require('multer');
const unzipper = require('unzipper');
const fs = require('fs');
const path = require('path');
const serveIndex = require('serve-index');
const cors = require('cors');
const archiver = require('archiver');
const rimraf = require('rimraf').default;

const app = express();
const upload = multer({ dest: 'uploads/' });

const EXTRACTED_FOLDER = path.join(__dirname, 'extracted');

app.use(cors());

app.use('/files', express.static(EXTRACTED_FOLDER), serveIndex(EXTRACTED_FOLDER, { icons: true }));

app.post('/upload', upload.single('zipfile'), async (req, res) => {
    const { file } = req;
    const userIp = req.ip.replace(/:/g, '_');
    const timestamp = Date.now();

    if (!file) {
        return res.status(400).send('No file uploaded.');
    }

    const uniqueDir = path.join(EXTRACTED_FOLDER, `${userIp}_${timestamp}`);
    const zipFilePath = path.join(__dirname, file.path);

    try {
        if (!fs.existsSync(uniqueDir)) {
            fs.mkdirSync(uniqueDir, { recursive: true });
        }

        fs.createReadStream(zipFilePath)
          .pipe(unzipper.Extract({ path: uniqueDir }))
          .on('close', () => {
              console.log(`Extracted to: ${uniqueDir}`);
              fs.unlink(zipFilePath, () => {});
              
              const fileUrl = `${req.protocol}://${req.get('host')}/files/${userIp}_${timestamp}/`;
              res.send({ message: 'File extracted successfully.', url: fileUrl });
          })
          .on('error', (err) => {
              console.error('Error unzipping file:', err);
              res.status(500).send('Error unzipping file.');
          });
    } catch (err) {
        console.error('Error handling file:', err);
        return res.status(500).send('Error processing file.');
    }
});

app.get('/download/:folderName', (req, res) => {
    const folderName = req.params.folderName;
    const folderPath = path.join(EXTRACTED_FOLDER, folderName);

    if (!fs.existsSync(folderPath)) {
        return res.status(404).send('Folder not found.');
    }

    const zipFileName = `${folderName}.zip`;
    res.set({
        'Content-Type': 'application/zip',
        'Content-Disposition': `attachment; filename=${zipFileName}`
    });

    const archive = archiver('zip', { zlib: { level: 9 } });
    archive.pipe(res);
    archive.directory(folderPath, false);
    archive.finalize();
});

app.get('/deleteall', (req, res) => {
   try{
    fs.rmSync(EXTRACTED_FOLDER, { recursive: true, force: true });
    fs.mkdirSync(EXTRACTED_FOLDER, { recursive: true });
    res.send({ message: 'All extracted files deleted successfully.' });

   }catch (err){
    res.send({ message: 'All extracted files not deleted successfully.' });
   }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
