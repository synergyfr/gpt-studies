const express = require('express');
const fs = require('fs');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;
const DATA_FILE = 'meetups.json';

// Middleware
app.use(bodyParser.json());

// Helper functions
function readMeetups() {
  const rawData = fs.readFileSync(DATA_FILE);
  return JSON.parse(rawData);
}

function writeMeetups(meetups) {
  fs.writeFileSync(DATA_FILE, JSON.stringify(meetups, null, 2));
}

// Routes
app.post('/meetups', (req, res) => {
  const { id, title, summary, address } = req.body;

  if (!id || !title || !summary || !address) {
    return res.status(400).json({ error: 'All fields are required.' });
  }

  const meetups = readMeetups();
  const meetupExists = meetups.find(meetup => meetup.id === id);
  if (meetupExists) {
    return res.status(400).json({ error: 'Meetup with this id already exists.' });
  }

  meetups.push({ id, title, summary, address });
  writeMeetups(meetups);

  res.status(201).json({ message: 'Meetup created successfully.' });
});

app.get('/meetups', (req, res) => {
  const meetups = readMeetups();
  res.json(meetups);
});

app.patch('/meetups/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const { title, summary, address } = req.body;

  const meetups = readMeetups();
  const meetupIndex = meetups.findIndex(meetup => meetup.id === id);

  if (meetupIndex === -1) {
    return res.status(404).json({ error: 'Meetup not found.' });
  }

  meetups[meetupIndex] = { ...meetups[meetupIndex], title, summary, address };
  writeMeetups(meetups);

  res.json({ message: 'Meetup updated successfully.' });
});

app.delete('/meetups/:id', (req, res) => {
  const id = parseInt(req.params.id);

  const meetups = readMeetups();
  const filteredMeetups = meetups.filter(meetup => meetup.id !== id);

  if (meetups.length === filteredMeetups.length) {
    return res.status(404).json({ error: 'Meetup not found.' });
  }

  writeMeetups(filteredMeetups);

  res.json({ message: 'Meetup deleted successfully.' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
