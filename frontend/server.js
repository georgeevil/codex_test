const express = require('express');
const multer = require('multer');
const path = require('path');
const axios = require('axios');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(express.static(path.join(__dirname, 'public')));

app.post('/upload', upload.single('image'), async (req, res) => {
  try {
    const fs = require('fs');
    const filePath = req.file.path;
    const image = fs.readFileSync(filePath);
    const response = await axios.post('http://localhost:8000/upload', image, {
      headers: { 'Content-Type': 'application/octet-stream' },
    });
    res.json(response.data);
  } catch (err) {
    console.error(err);
    res.status(500).send('Error processing image');
  }
});

app.listen(3000, () => console.log('Frontend running on port 3000'));
