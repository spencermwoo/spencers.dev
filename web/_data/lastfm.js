const cache = require('@11ty/eleventy-cache-assets');
require('dotenv').config();

const API = 'http://ws.audioscrobbler.com/2.0/'
const API_KEY = process.env.LASTFM_KEY;
const USERNAME = 'starfoxxy';

//https://www.last.fm/api/show/user.getRecentTracks

module.exports = async () => {
  try {
    const url = `${API}?method=user.getrecenttracks&user=${USERNAME}&limit=10&api_key=${API_KEY}&format=json`
    const data = {
      duration: '2h',
      type: 'json',
    }

    return await cache(url, data);
  } catch (e) {
    console.log(e);

    return [];
  }
};