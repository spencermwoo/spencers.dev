// const outdent = require('outdent')({ newline: ' ' });
module.exports = (id) => {
    return `<iframe src="https://docs.google.com/document/d/${id}/pub?embedded=true" style="border: none; width: 80%; height: 80vh"></iframe>`;
};