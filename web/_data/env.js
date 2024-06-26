const environment = process.env.ELEVENTY_ENV;
const PROD_ENV = 'prod';
const prodUrl = 'https://spencers.dev';
const devUrl = 'http://localhost:8080';
const baseUrl = environment === PROD_ENV ? prodUrl : devUrl;
const isProd = environment === PROD_ENV;

const folder = {
  assets: 'assets',
};

const dir = {
  img: `/${folder.assets}/images/`,
  css: `/${folder.assets}/css/`,
  favicons: `/${folder.assets}/images/favicons/`
}

const base = {
  site: baseUrl,
  img: `${baseUrl}${dir.img}`,
  css: `${baseUrl}${dir.css}`,
  favicons: `${baseUrl}${dir.favicons}`
}

module.exports = {
  siteName: 'spencers.dev',
  themeColor: '#ffffff',
  author: 'Spencer Woo',
  environment,
  isProd,
  folder,
  dir,
  base,
  tracking: {
    gtag: 'G-EX9S5Z1D7J'
  }
};
