// const outdent = require('outdent')({ newline: ' ' });
module.exports = (id) => {
    return `<iframe src="https://docs.google.com/document/d/e/${id}/pub?embedded=true" style="border: none; width: 100vh; height: 80vh"></iframe>`;
};